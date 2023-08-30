# -*- coding:utf-8 -*-
# File: Logger.py
# Time: 2023/8/1 10:46
# Author: GG Bond

import logging
import colorlog
import os
import time
from Core.PathHandle import LOG_DIR


class GetLog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.file = os.path.join(LOG_DIR, time.strftime("%Y-%m-%d", time.localtime()) + ".log")
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        self._set_formatter()
        self._set_handlers()

    def _set_formatter(self):
        self.formatter_log = colorlog.ColoredFormatter(
            fmt="%(log_color)s %(asctime)s %(filename)s %(module)s %(funcName)s [line:%(lineno)d] %(levelname)s: %(message)s")
        self.formatter_cmd = colorlog.ColoredFormatter(
            fmt="%(log_color)s %(asctime)s %(filename)s %(module)s %(funcName)s [line:%(lineno)d] %(levelname)s: %(message)s")

    def _set_handlers(self):
        stream_handle = logging.StreamHandler()
        stream_handle.setFormatter(self.formatter_log)

        filehandle = logging.FileHandler(filename=self.file, mode="a", encoding="utf8")
        filehandle.setFormatter(self.formatter_cmd)

        self.log.addHandler(stream_handle)
        self.log.addHandler(filehandle)

    def get_logger(self):
        return self.log


def logger():
    log_instance = GetLog()
    logger = log_instance.get_logger()
    return logger

if __name__ == '__main__':
    logger = logger()
    logger.info("info")
    logger.error("error")
    logger.warning("warning")
    logger.debug("debug")
    logger.critical("critical")
