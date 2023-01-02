app = Flask(__main__)

@app.route('/')
def hello_world():
    return 'GreyMatters'


if __name__ == "__main__":
    app.run()
