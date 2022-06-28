###############################
# run_driver.py
#
# Desc: Running driver menggunakan format minimal tanpa threading
#
# Auth: Yose
# Date: 29 Maret 2018
#

import os
from e411 import e411
import logging.config
import yaml
import ConfigParser
import sys


#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir("C:\\SIMDONDAR-e601")
#print 'Working dir:%s' % dname

PORT_COM = 'COM0'
SERVER = '127.0.0.1'
DB_OFFLINE = True
VERSION = '0.0.0.1'

config = ConfigParser.ConfigParser()
config.read('run_driver.ini')
SERVER = config.get('General','server')
TCP_HOST = config.get('General','tcp_host')
TCP_PORT = config.get('General','tcp_port')
DB_OFFLINE = config.get('General','db_offline')

if DB_OFFLINE=='True':
    DB_OFFLINE = True
else:
    DB_OFFLINE = False

DEV = False



def main():
    logging.info('VERSION:%s' % VERSION)
    logging.info('TCP_HOST:%s' % TCP_HOST)
    logging.info('TCP_PORT:%s' % TCP_PORT)
    logging.info('SERVER SIMDONDAR:%s' % SERVER)
    try:
        con = e411(tcp_host = TCP_HOST, tcp_port = TCP_PORT, server = SERVER, db_offline=DB_OFFLINE)
    except Exception as e:
        logging.error('[!!!] Gagal:%s' % str(e))
        sys.exit(0)


    if DEV:
        logging.info('Sending test connection..')
        logging.info('Run driver..')
        con.open()
    else:
        logging.info('Run driver..')
        con.open()

if __name__ == "__main__":
    with open('run_driver.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    logging.info('Starting program.')
    main()
