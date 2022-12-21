from BlueMoon.app import app
from BlueMoon import VERSION
import os

@app.route('/')
def root():
    return {
        "Name": os.environ['COMPUTERNAME'],
        "version": VERSION
    }
