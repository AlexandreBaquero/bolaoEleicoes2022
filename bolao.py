from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Bolão das Eleições 2022</h1>'

app.run()

