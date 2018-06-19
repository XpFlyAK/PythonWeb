# -*- coding: UTF-8 -*-
from web_demo.models import Model


class Message(Model):
    def __init__(self, form):
        self.author = form.get('author', '')
        self.message = form.get('message', '')
