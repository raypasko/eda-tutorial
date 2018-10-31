class Bus:
    def __init__(self, listeners=None):
        if listeners is None:
            listeners = {}
        self.listeners = dict(listeners)

    def emit(self, event):
        name, payload = event
        for listener in self.listeners.get(name, []):
            listener(event)

    def add_listener(self, name, listener):
        self.listeners.setdefault(name, [])
        self.listeners[name].append(listener)

