from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Provides a simple hello world message for the specified repo and branch."""
    message = "Hello World from repo 'my-hello-repo' on branch 'my-hello-branch'"
    return jsonify(message=message)

@app.route('/health')
def health():
    """Provides a basic health check endpoint."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # This block is for local development and is not used by Gunicorn.
    app.run(host='0.0.0.0', port=5000)
