from flask import Blueprint

main = Blueprint("main", __name__)

from . import events
from .routes import user, message, channel


