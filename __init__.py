import os
from flask import Flask
@app.route('/hello')
def hello():
    return 'Hello, World!'