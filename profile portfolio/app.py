import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html', profile=read_profile())

def read_profile():
    with open('profile.json', 'r') as f:
        data = json.load(f)
        return data.get('profile')

if __name__=="__main__":
    app.run(debug=True)