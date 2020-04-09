# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, is_light=False):
        self.name = name
        self.description = description

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

        self.is_light = is_light

        self.items = []

    def __getitem__(self, arg):
        return getattr(self, arg)
