from flask import Flask
from flask_cors import CORS
import random


# Khởi tạo server
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
def run_server():
    return "Hihi Haha Huhu =))"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return f"Random number: {int(random.uniform(0, 10))}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)