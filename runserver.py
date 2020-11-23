from decouple import config
from server import app

def runappserver():
    HOST = config("HOST_SERVER", default="localhost")
    try:
        PORT = int(config("HOST_SERVER", default=8080))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)

if __name__ == '__main__':
    runappserver()
