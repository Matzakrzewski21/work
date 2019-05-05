from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


f= open("config.json", "r")
data = json.loads(f.read())
print (data["port"])
print (data["index"])

@app.route('/')

def hello_world():
    return render_template(data["index"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=data["port"])
