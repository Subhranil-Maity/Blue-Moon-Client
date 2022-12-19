from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os

@app.route('/')
def root():
    return {
        "Name": os.environ['COMPUTERNAME']
    }
