from flask import Flask, jsonify

from . import app


@app.route("/", methods=["GET"])
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({
        'app': 'Flask Microservice Starter',
        'version': 1.0
    })
