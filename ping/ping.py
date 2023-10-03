from flask import Flask

app = Flask(__name__)

# Define a route for the "ping" endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return 'Pong!'

if __name__ == '__main__':
    # Run the Flask app on port 5000 (you can change the port as needed)
    app.run(host='0.0.0.0', port=5000)
