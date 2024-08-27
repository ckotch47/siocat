import asyncio
import json
import threading
import socketio
from distlib.compat import raw_input
from print_color import print

from siocat.utils.parser import m_arguments


def get_config_from_file(argument):
    try:
        file = open(argument.conf, 'r')
        return json.loads(file.read())
    except:
        exit(101)


config = get_config_from_file(m_arguments)
sio = socketio.AsyncClient(
    logger=bool(config.get('logger')),
    engineio_logger=bool(config.get('engineio_logger'))
)


@sio.on('*', namespace='*')
async def any_event_any_namespace(event=None, namespace=None, data=None):
    print('\n' + json.dumps(data, indent=1) if data else ' ', color='magenta', tag_color='white',
          tag=f"{namespace} {event}")
    pass


class SioCat:
    argument = m_arguments

    def emit_event(self, namespace, event, data):
        try:
            asyncio.run(sio.emit(
                event=event,
                data=json.loads(data),
                namespace=namespace
            ))
        except Exception as e:
            exit(101)
            pass
        self.get_event()

    def parse_and_send_get_event_from_str(self, event: str):
        tmp = event.split(' ')
        data = event.replace(f"{tmp[0]} {tmp[1]}", '')
        self.emit_event(tmp[0], tmp[1], data)

    def parse_and_send_get_event_from_file(self, file_path: str):
        file = open(file_path, 'r')
        res: dict = json.loads(file.read())
        self.emit_event(res.get('namespace'), res.get('event'), json.dumps(res.get('data')))

    def get_event(self):
        try:
            user_event = raw_input()
            print(user_event)
            if user_event.find('.json') != -1:
                self.parse_and_send_get_event_from_file(user_event)
            else:
                self.parse_and_send_get_event_from_str(user_event)
        except Exception as e:
            print(e)
            self.get_event()




    async def connect(self, config: dict):
        await sio.connect(
            url=config.get('url'),
            headers=config.get('headers'),
            auth=config.get('auth'),
            transports=config.get('transports'),
            namespaces=config.get('namespaces'),
            wait_timeout=config.get('wait_timeout')
        )

    async def run(self):
        conf = get_config_from_file(self.argument)

        await self.connect(conf)

        thread = threading.Thread(target=self.get_event)
        thread.daemon = True
        thread.start()

        await sio.wait()
