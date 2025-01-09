from flask import Flask
import os
app = Flask(__name__)

PORT = os.environ.get("PORT", "8080")

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
