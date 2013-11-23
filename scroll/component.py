
class Component(object):
    instances = []

    def __init__(self):
        super().__init__()
        self.__class__.instances.append(self)
