from . import component

class Entity(object):
    entities = []
    """The base Entity for Scroll. Game objects should inherit from this."""
    def __init__(self):
        super().__init__()
        self.components = {}
        self.__class__.entities.append(self)

    def update(self):
        map(lambda x: x.update(), self.components.values())

    def add_component(self, component):
        """Adds a component to the Entity"""

        self.components[component.__class__] = component

    def get_component(self, component):
        component_class = component.__class__

        if component_class in self.components:
            return self.components[component_class]
        else:
            return None

    def draw(self):
        print("Entity drawing")
        #print(self.components[component.Sprite].draw())
        for component in self.components.values():
            component.draw()
        #map(lambda x: x.draw(), self.components.values())

