from flask import Flask, render_template, jsonify, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8002')
PORT = int(os.environ.get('PORT', 8001))
HOST = os.environ.get('HOST', '0.0.0.0')

@app.route('/')
def index():
    try:
        response = requests.get(f'{BACKEND_URL}/api/get')
        if response.status_code == 200:
            names = response.json()
        else:
            names = []
    except Exception as e:
        print(f"Error fetching data: {e}")
        names = []
    return render_template('index.html', data=names, backend_url='')

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

# Proxy routes for API calls
@app.route('/api/get')
def proxy_get():
    try:
        response = requests.get(f'{BACKEND_URL}/api/get')
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": "Failed to retrieve names"}), 500

@app.route('/api/add/<name>', methods=['POST'])
def proxy_add(name):
    try:
        response = requests.post(f'{BACKEND_URL}/api/add/{name}')
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": "Failed to add name"}), 500

@app.route('/api/delete/<name>', methods=['DELETE'])
def proxy_delete(name):
    try:
        response = requests.delete(f'{BACKEND_URL}/api/delete/{name}')
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": "Failed to delete name"}), 500

@app.route('/api/search/<query>')
def proxy_search(query):
    try:
        response = requests.get(f'{BACKEND_URL}/api/search/{query}')
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": "Failed to search names"}), 500

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
