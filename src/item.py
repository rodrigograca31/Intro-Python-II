from colored import fg, bg, attr


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def on_take(self):
        print("%sYou have picked up %s%s" % (fg(46), self.name, attr(0)))

    def on_drop(self):
        print("%sYou have dropped %s%s" % (fg(46), self.name, attr(0)))
