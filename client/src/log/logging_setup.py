import logging
import os


class LoggingSetup:
    def __init__(self, log_dir="logs", error_dir="errors"):
        self.log_dir = log_dir
        self.error_dir = error_dir

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        if not os.path.exists(error_dir):
            os.makedirs(error_dir)

        self._configure_logging()

    def _configure_logging(self):
        log_filename = os.path.join(self.log_dir, "app.log")
        error_log_filename = os.path.join(self.error_dir, "error.log")

        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

        error_log_handler = logging.FileHandler(error_log_filename)
        error_log_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        error_log_handler.setFormatter(formatter)

        logging.getLogger().addHandler(error_log_handler)


if __name__ == "__main__":
  log_setup = LoggingSetup()