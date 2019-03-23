import struct
from ctypes import (
    Structure,
    c_uint8,
    c_uint16,
    c_uint32
)
import socket


class TCP(Structure):

    _fields_ = [
        ("src_port", c_uint16),
        ("dst_port", c_uint16),
        ("seq", c_uint32),
        ("ack_seq", c_uint32),
        ("res1", c_uint16, 4),
        ("doff", c_uint16, 4),
        ("fin", c_uint16, 1),
        ("syn", c_uint16, 1),
        ("rst", c_uint16, 1),
        ("psh", c_uint16, 1),
        ("ack", c_uint16, 1),
        ("urg", c_uint16, 1),
        ("ece", c_uint16, 1),
        ("cwr", c_uint16, 1),
        ("window", c_uint16),
        ("check", c_uint16),
        ("urg_ptr", c_uint16),
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        self._parse2pydata()

    def __str__(self):
        return str(self._packet_dict)

    def _parse2pydata(self):
        self._packet_dict = {
            'src_port': self.src_port,
            'dst_port': self.dst_port
        }
