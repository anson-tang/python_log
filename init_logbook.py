#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Anson Tang <anson.tkg@gmail.com>
# License: Copyright(c) 2015 Anson.Tang
# Summary: 

import os
import sys
import logbook


logger = None 
def init_logbook(filename, level, count=100, max_size=10485760):
    global logger
    logger = logbook.Logger()

    logbook.RotatingFileHandler(filename,
            level = level,
            backup_count = count,
            max_size = max_size,
            format_string=u'[{record.time}] {record.message}'
            ).push_application()


class Log(object):
    @staticmethod
    def error(*args):
        logger.error("{} {}: {} {}".format("\033[31m[ E ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)),  "\033[0m"))

    @staticmethod
    def warn(*args):
        logger.warn("{} {}: {} {}".format("\033[33m[ W ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)), "\033[0m"))

    @staticmethod
    def info(*args):
        logger.info("{} {}: {} {}".format("\033[32m[ I ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)), "\033[0m"))

    @staticmethod
    def debug(*args):
        logger.debug("{} {}: {} {}".format("\033[37m[ D ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)), "\033[0m"))

