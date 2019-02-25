from typing import Type
from .packet import Packet


class DataSaver:

    def __init__(
        self,
        log_dir: str
    ):
        self._log_dir = log_dir

    def save(
        self,
        packet: Type[Packet]
    ):
        print(packet)
        print('='*50)
