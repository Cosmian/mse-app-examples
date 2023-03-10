"""`Helloworld` example."""

from http import HTTPStatus

from flask import Flask, Response

app = Flask(__name__)


@app.get("/health")
def health_check():
    """Health check of the application."""
    return Response(response="OK", status=HTTPStatus.OK)


@app.route("/")
def hello():
    """Get a simple example."""
    return "Hello world"
