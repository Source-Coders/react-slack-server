from . import user
from . import message
from . import channel
from . import car
from .. import main

__all__ = ["user", "message", "channel", "car"]

@main.route("/")
def index():
    return "<h1>Hello World!</h1>"

