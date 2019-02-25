from lib.packet_capture import PacketCapture
from lib.util.status_reporter import StatusReporter
from lib.util.config_reader import load_config


def main():
    config = load_config()

    pc = PacketCapture(
        log_dir=config['LOGGER']['LOCAL_LOG_FILE_DIR']
    )
    pc.capture(
        host=config['LOGGER']['TARGET_IP']
    )

    sr = StatusReporter()
    sr.report()


if __name__ == '__main__':
    main()
