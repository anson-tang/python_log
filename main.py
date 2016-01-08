#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Anson Tang <anson.tkg@gmail.com>
# License: Copyright(c) 2015 Anson.Tang
# Summary: 

from init_logbook import init_logbook, Log
from init_logging import init_logging, Log

from test_1.test_2.test_log import *

def test():
    Log.error('==========error:{}.'.format('hi, error!'))
    Log.warn('===========warn:{}.'.format('hi, warn!'))
    Log.info('===========info:{}.'.format('hi, info!'))
    Log.debug('==========debug:{}.'.format('hi, debug!'))

if __name__ == "__main__":
    # init logging
    init_logging('./error.log', 'WARNING')
    
    # or init logbook
    #init_logbook('./error.log', 'ERROR')

    test()
