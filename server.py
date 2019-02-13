#!/usr/bin/python3.6

import socketio
import engineio
import eventlet
import sys

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'},
    '/bootstrap.css': {'content_type': 'text/css', 'filename': 'bootstrap.css'},
    '/main.css': {'content_type': 'text/css', 'filename': 'main.css'},
    '/main.js': {'content_type': 'application/javascript', 'filename': 'main.js'},
    '/socket.io.js': {'content_type': 'application/javascript', 'filename': 'socket.io.js'},
    '/popper.min.js': {'content_type': 'application/javascript', 'filename': 'popper.min.js'},
    '/jquery-3.3.1.slim.min.js': {'content_type': 'application/javascript', 'filename': 'jquery-3.3.1.slim.min.js'},
    '/bootstrap.min.js': {'content_type': 'application/javascript', 'filename': 'bootstrap.min.js'},

})

@sio.on('connect')
def connect(sid, environ):
    pass

@sio.on('message')
def message(sid, data):
    name = data["name"]
    msg = data["msg"]
    sio.emit('message', {"msg":msg,"name":name})

@sio.on('typing')
def typing(sid, data):
    name = data["name"]
    sio.emit('typing', {"name":name})

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost" 
    eventlet.wsgi.server(eventlet.listen((host, 3457)), app)
