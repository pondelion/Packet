import os
import socket
from ctypes import sizeof
from .protocol import IP, TCP, UDP, ICMP
from .data_manager.packet import Packet
from .data_manager.file_tracker import FileTracker
from .data_manager.data_saver import DataSaver
from .util.logger import get_logger


class PacketCapture:

    def __init__(
        self,
        log_dir: str
    ):
        self._socket_protcol = socket.IPPROTO_IP if os.name == 'nt' else socket.IPPROTO_ICMP
        self._finish = False
        self._data_saver = DataSaver(
            log_dir=log_dir
        )
        self._logger = get_logger()
        # self._file_tracker

    def capture(
        self,
        host: str
    ):
        try:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_RAW,
                self._socket_protcol
            )
        except OSError as e:
            self._logger.debug('You need to run as administrator.')
            raise e

        sock.bind((host, 0))
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == 'nt':
            sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        while self._finish is False:
            data = sock.recvfrom(65565)[0]

            packet = self._parse_data(data)

            self._data_saver.save(packet)

        if os.name == 'nt':
            sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    def _parse_data(self, data):
        ip_header = IP(data[0:20])

        offset = ip_header.ihl * 4

        if ip_header.protocol == 'ICMP':
            header = ICMP(data[offset:offset+sizeof(ICMP)])
            content = data[offset+sizeof(ICMP):]
        elif ip_header.protocol == 'TCP':
            header = TCP(data[offset:offset+sizeof(TCP)])
            content = data[offset+sizeof(TCP):]
        elif ip_header.protocol == 'UDP':
            header = UDP(data[offset:offset+sizeof(UDP)])
            content = data[offset+sizeof(UDP):]

        header_dict = {
            'ip': ip_header,
            'tr': header
        }

        packet = Packet(
            protocol=ip_header.protocol,
            headers=header_dict,
            content=content
        )

        return packet

    def finish(self):
        self._finish = True
