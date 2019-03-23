import threading
from lib.packet_capture import PacketCapture
from lib.util.status_reporter import StatusReporter
from lib.util.config_reader import load_config


def main():
    config = load_config()

    pc = PacketCapture(
        log_dir=config['LOGGER']['LOCAL_LOG_FILE_DIR']
    )
    cap_thread = threading.Thread(
        target=pc.capture,
        args=(config['LOGGER']['TARGET_IP'],)
    )

    cap_thread.start()

    try:
        sr = StatusReporter()
        sr.report()
    except KeyboardInterrupt:
        pc.finish()


if __name__ == '__main__':
    main()
