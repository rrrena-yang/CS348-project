from SQLService import get_connector
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

cursor = get_connector()

@app.route('/')
def index():
    return render_template('index.html')
# Example route for a simple GET request

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

# Example route for a POST request
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    # Process the data here
    return jsonify(received_data=data), 201

if __name__ == '__main__':
    app.run(debug=True)
