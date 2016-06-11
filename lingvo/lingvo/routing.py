# In routing.py
from channels.routing import route
from channels.staticfiles import StaticFilesConsumer

from lingvo import consumers
from lingvo.consumers import ws_disconnect, ws_connect

channel_routing = {
    # archivos staticos
    'http.request': StaticFilesConsumer(),
    # mensajes websocket ejecutados por los consumidores de django:
    'websocket.connect': ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
}
