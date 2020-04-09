from item import Item
from colored import fg, bg, attr


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print("%sIt's not wise to drop your source of light!%s" %
              (fg(1), attr(0)))
        super().on_drop()
