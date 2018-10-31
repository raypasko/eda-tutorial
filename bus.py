class Bus:
    def __init__(self, listeners=None):
        if listeners is None:
            listeners = []
        self.listeners = list(listeners)

    def emit(self, event):
        for listener in self.listeners:
            listener(event)

    def add_listener(self, listener):
        self.listeners.append(listener)
