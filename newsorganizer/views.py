from newsorganizer import app
from flask import render_template


@app.route('/')

def index():
    list = [
            "https://vk.com/codehipsters",
            "https://vk.com/forwebdev"
            ]
    return render_template('index.html')


