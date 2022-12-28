"""
Notification structure.
"""


# First, the cycle we want to break

class M0:
    def __init__(self):
        self.the_V = None

    def hook_up(self, v: 'V'):
        self.the_V = v

    def f(self):
        self.the_V.g(self)

    def h(self):
        print("What goes around, comes around")


class V0:
    def __init__(self):
        pass

    def g(self, an_m: M0):
        an_m.h()


v = V0()
m = M0()
m.hook_up(v)
m.f()


class Listener:
    """Abstract base class for classes in View component"""

    def notify(self, event: str):
        raise NotImplementedError("Notify has not been implemented")


class ModelElement:
    """Abstract base class for classes in Model component"""

    def __init__(self):
        self.listeners = []

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, event: str):
        for listener in self.listeners:
            listener.notify(self, event)


class M(ModelElement):

    def __init__(self):
        super().__init__()
        # Might have more of its own initialization here

    def f(self):
        # Instead of self.the_V.g()
        self.notify_all("g")

    def h(self):
        print("What goes around, comes around")


class V(Listener):
    def __init__(self):
        pass

    def notify(self, an_m: M, event: str):
        # Instead of a call to method g, we
        # might get an event "g"
        if event == "g":
            an_m.h()


v = V()
m = M()
m.add_listener(v)
m.f()
