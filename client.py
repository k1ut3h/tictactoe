#! /usr/bin/env python3
import socketio

sio = socketio.Client()

@sio.event
def intro(data):
  print("A message was received")
