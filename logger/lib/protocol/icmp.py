import struct
from ctypes import (
    Structure,
    c_uint8,
    c_uint16,
    c_uint32
)
import socket


class ICMP(Structure):

    _fields_ = [
        ('type',         c_uint8),
        ('code',         c_uint8),
        ('checksum',     c_uint16),
        ('unused',       c_uint16),
        ('next_hop_mtu', c_uint16)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass
