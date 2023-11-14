# src/networking/error_handling/logs/nb_logging.py
import datetime


class NorthboundLogger:
    LOG_FILE = "src/networking/error_handling/logs/northbound_log.txt"

    @staticmethod
    def log_message(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(NorthboundLogger.LOG_FILE, "a+") as log_file:
            log_file.write(f"{timestamp}: {message}\n")

    @staticmethod
    def log_error(error):
        NorthboundLogger.log_message(f"ERROR: {error}")
