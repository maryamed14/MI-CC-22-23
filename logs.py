import logging
import sys


class Temp:
    def __init__(self, is_verbose=False):
        # configuring log
        if (is_verbose):
            self.log_level = logging.DEBUG
        else:
            self.log_level = logging.INFO

        log_format = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] - %(message)s')
        self.log = logging.getLogger(__name__)
        self.log.setLevel(self.log_level)

        # writing to stdout
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self.log_level)
        handler.setFormatter(log_format)
        self.log.addHandler(handler)

        # here
        self.log.debug("test")


if __name__ == "__main__":
    t = Temp(True)
