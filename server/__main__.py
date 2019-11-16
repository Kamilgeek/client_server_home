import yaml, json, logging
from socket import socket
from argparse import ArgumentParser
from resolvers import resolve
from protocol import validate_request, make_response

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
host, port = defaul_config.get('host'), defaul_config.get('port')

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(f'%(levelname)-10s %(asctime)s %(message)s')

handler = logging.FileHandler('log/server.log')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)

try:
    sock = socket()
    sock.bind((host, port))
    sock.listen(5)

    logger.info(f'Server was started with {host}:{port}')

    while True:
        client, addres = sock.accept()
        logger.info(f'client was connected with {addres[0]}:{addres[1]}')
        b_request = client.recv(defaul_config.get('buffersize'))
        request = json.loads(b_request.decode())

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)

            if controller:
                try:
                    logger.debug(f'Controller {action_name} resolved with request{request}')
                    response = controller(request)
                except Exception as err:
                    logger.critical(f'Controller {action_name} error: {err}')
                    response = make_response(request, 500, 'Internal server error')
            else:
                logger.error(f'Controller {action_name} not found')
                response = make_response(request, 404, f'Action with name {action_name} not supported')
        else:
            logger.error(f'Controller wrong request {request}')
            response = make_response(request, 400, 'wrong request format')

        client.send(
            json.dumps(response).encode()
        )

        client.close()
except KeyboardInterrupt:
    logger.info('server shutdown')
