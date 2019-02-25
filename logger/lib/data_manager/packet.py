

class Packet:

    def __init__(
        self,
        protocol=None,
        header=None,
        content=None
    ):
        self._protocol = protocol
        self._header = header
        self._content = content

    def __str__(self):
        s = f'protocol : {self._protocol}\n'
        s += f'header   : {self._header}\n'
        s += f'content  : {self._content}'
        return s
