import logging
import os
import sys
import time


class Log(object):
    def __init__(self, logger=None, log_cate="schedule"):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = time.strftime("%Y_%m_%d")

        ch = logging.StreamHandler(sys.stdout)
        if os.getenv("DEBUG"):
            ch.setLevel(logging.DEBUG)
        else:
            ch.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] %(message)s"
        )
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

        ch.close()

    def get_log(self):
        return self.logger
