import yaml
import select
import threading
import logging
import json

from app import Aplication
from socket import socket
from argparse import ArgumentParser
from handlers import handle_default_request

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

args = parser.parse_args()

defaul_config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        defaul_config.update(file_config)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s %(asctime)s %(message)s',
    handlers=[
        logging.FileHandler('log/server.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

app = Aplication(
    defaul_config.get('host'),
    defaul_config.get('port'),
    defaul_config.get('buffersize'),
    handle_default_request
)

app.bind()
app.run()
