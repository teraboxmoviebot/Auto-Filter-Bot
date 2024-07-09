from flk import flask
app = Flask(__name__)

@app.route('/')
def hello_world():
      return 'CineMax'


if __name__ == "__main__":
        app.run()
