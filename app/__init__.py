from flask import Flask, abort, request

app = Flask(__name__)
from app import routes