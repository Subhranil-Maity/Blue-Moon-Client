from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os

@app.route('/')
def root():
    return {
        "Name": os.environ['COMPUTERNAME']
    }
