import yaml
import json
import logging
from socket import socket
from argparse import ArgumentParser
from datetime import datetime

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

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(f'%(levelname)-10s %(asctime)s %(message)s')

handler = logging.FileHandler('log/client.log')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)



host, port = defaul_config.get('host'), defaul_config.get('port')

sock = socket()
sock.connect((host, port))

logger.info(f'Client was started')

action = input('Enter action:')
data = input('Enter data:')

request = {
    'action': action,
    'time': datetime.now().timestamp(),
    'data': data,
}

s_request = json.dumps(request)
sock.send(s_request.encode())
logger.info(f'Client send data: {data}')
b_response = sock.recv(defaul_config.get('buffersize'))
logger.info(b_response.decode())

