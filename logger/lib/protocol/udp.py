import struct
from ctypes import (
    Structure,
    c_uint8,
    c_uint16,
    c_uint32
)
import socket


class UDP(Structure):

    _fields_ = [
        ('src_port', c_uint16),
        ('dst_port', c_uint16),
        ('len', c_uint16),
        ('sum', c_uint16)
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
            'dst_port': self.dst_port,
            'len': self.len,
            'sum': self.sum
        }
