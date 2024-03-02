from myport import app
from flask_socketio import SocketIO

if __name__ == '__main__':
    app.config.from_pyfile("config.py")
    socketio = SocketIO(app)
    socketio.run(app, host='0.0.0.0', debug=True, port=8050, use_reloader=True)
