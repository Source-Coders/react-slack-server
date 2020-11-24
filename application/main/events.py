import json
from flask import request
from flask_socketio import emit, join_room, close_room 
from .. import socketio
from .services import client_service, socket_service, message_service, user_service
import json
from .. import db
from .. models.User import User
from ..models.Message import Message, MessageSchema, message_schema
from ..models.ChannelMessages import channel_messages

@socketio.on("connect")
def on_connect():
    username = request.args.get("username")
    print(f"Client connected! username: {username}")
    user = User.query.filter_by(username=username).one()
    channels = user.channels
    for channel in channels:
        channel_id = channel.channel_id
        join_room(channel_id)
    for org in user.orgs:
        join_room(org.org_id)
    room = request.sid
    client_service.on_client_connected(username, room)
    emit("user-joined-chat", {"username": username},
         broadcast=True, include_self=False)

@socketio.on("send-message")
def on_send_message(clientMessage):
    print(clientMessage)
    if clientMessage["type"] == "channel":
        message_service.store_channel_message(clientMessage)
        channel_room = clientMessage['channel_id']
        emit("message-received", clientMessage, room=channel_room)
    elif clientMessage["type"] == "private":
        message_service.store_private_message(clientMessage)
        receiver_username = clientMessage['receiver']
        sender_username = clientMessage['sender']
        receiver_client = client_service.get_client(receiver_username)
        is_receiver_online = receiver_client is not None
        if is_receiver_online:
            receiver_room = receiver_client.room
            emit("message-received", clientMessage, room=receiver_room)
        sender_client = client_service.get_client(sender_username)
        is_sender_online = sender_client is not None
        if is_sender_online:
            sender_room = sender_client.room
            emit("message-received", clientMessage, room=sender_room)

@socketio.on("join-channel")
def on_join_channel(info):
    org_name, channel_name = info["org_name"], info["channel_name"]
    room = socket_service.compute_room(org_name, channel_name)
    print("join_channel:", room)
    join_room(room) 

@socketio.on("disconnect")
def on_disconnect():
    print("Client disconnected")
    room = request.sid
    username = client_service.get_username_by_room(room)
    client_service.remove_client_by_room(room)
    user = user_service.get_user(username)
    for org in user.orgs:
        socketio.emit("org-member-offline", username, room=org.org_id)

