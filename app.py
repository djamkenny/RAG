
from flask import Flask, render_template, request, jsonify
from main import get_user_info
from trenanalyzer import respond
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route for the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')  # This serves the HTML file

# Route for analyzing the YouTube video
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    region = data.get('region')

    try:
        get_user_info(url, region)
        result = respond()
        return jsonify({'message': result})
    except Exception as e:
        return jsonify({'message': 'Invalid YouTube URL or video ID not found.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
