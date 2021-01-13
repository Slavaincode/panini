import time

from anthill.sandbox import Sandbox
from anthill import app as ant_app


app = ant_app.App(
    service_name='test_publish',
    host='127.0.0.1',
    port=4222,
    app_strategy='asyncio',
)


@app.task()
async def publish():
    await app.aio_publish({'data': 1}, topic='foo')


class Global:
    def __init__(self):
        self.public_variable = 0


global_object = Global()


def foo_handler(topic, message):
    global_object.public_variable = message['data']


# emulate topic subscription
listen_topics_callbacks = {
    'foo': [foo_handler]
}

Sandbox(app, listen_topics_callbacks=listen_topics_callbacks)

# wait 0.1 sec (for app to publish message)
# TODO: invent some better way to test callback
time.sleep(0.1)


def test_publish():
    assert global_object.public_variable == 1
