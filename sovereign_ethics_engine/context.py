
# context.py
#
# Defines the Request and Context classes.
# These wrap the raw text and doctrinal anchors.

class Request:
    def __init__(self, text, meta=None):
        self.text = text
        self.meta = meta or {}


class Context:
    def __init__(self, doctrine=None):
        self.doctrine = doctrine or {}
