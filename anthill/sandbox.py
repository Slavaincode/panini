from .nats_client.nats_client import NATSClient
from anthill.utils.helper import start_process


class Sandbox(NATSClient):
    def __init__(self, app, listen_topics_callbacks=None):
        if listen_topics_callbacks is None:
            listen_topics_callbacks = {}

        self.nats_config = {
            'host': '127.0.0.1',
            'port': 4222,
            'client_id': 'sandbox',
            'listen_topics_callbacks': listen_topics_callbacks,
            'publish_topics': [],
            'allow_reconnect': False,
            'queue': '',
            'max_reconnect_attempts': 60,
            'reconnecting_time_wait': 2,
            'client_strategy': 'sync',
        }

        NATSClient.__init__(
            self,
            **self.nats_config
        )

        start_process(app.start)


