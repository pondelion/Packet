

class Packet:

    def __init__(
        self,
        protocol=None,
        headers=None,
        content=None
    ):
        self._protocol = protocol
        self._headers = headers
        self._content = content

    def __str__(self):
        s = f'protocol : {self._protocol}\n'
        s += f'ip_header   : {self._headers["ip"]}\n'
        s += f'{self._protocol}_header   : {self._headers["tr"]}\n'
        s += f'content  : {self._content}'
        return s
