from flask import Flask, render_template, send_from_directory
from flask_api import status
app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html'), 200

@app.route('/css/<path:filename>')
def static_stylesheets(filename):
    return send_from_directory('css', filename)

if __name__ == '__main__':
    app.run()
