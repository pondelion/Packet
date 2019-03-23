from typing import Type
from .packet import Packet
from ..util.logger import get_logger


class DataSaver:

    def __init__(
        self,
        log_dir: str
    ):
        self._log_dir = log_dir
        self._logger = get_logger()

    def save(
        self,
        packet: Type[Packet]
    ):
        self._logger.debug(packet)
        self._logger.debug('='*50)
