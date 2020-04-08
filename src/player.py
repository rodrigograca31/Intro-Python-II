# Write a class to hold player information, e.g. what room they are in
# currently.
from colored import fg, bg, attr


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return (
            "\n"
            + self.name
            + " is at: "
            + self.room.name
            + ", "
            + self.room.description
            + "\n"
        )

    def move(self, direction):
        # self.room = room

        if direction == "n":
            if self.room.n_to:
                self.room = self.room.n_to
            else:
                print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
        elif direction == "s":
            if self.room.s_to:
                self.room = self.room.s_to
            else:
                print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
        elif direction == "w":
            if self.room.w_to:
                self.room = self.room.w_to
            else:
                print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
        elif direction == "e":
            if self.room.e_to:
                self.room = self.room.e_to
            else:
                print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
