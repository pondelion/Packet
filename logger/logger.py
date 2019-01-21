from .lib.packet_capture import PacketCapture
from .lib.util.status_reporter import StatusReporter


def main():
    pc = PacketCapture()
    pc.capture()

    sr = StatusReporter()
    sr.report()


if __name__ == '__main__':
    main()
