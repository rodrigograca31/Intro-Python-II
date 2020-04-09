# Write a class to hold player information, e.g. what room they are in
# currently.
from colored import fg, bg, attr


class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.inventory = []
        self.score = 0

    def __str__(self):
        return (
            self.name
            + " has "
            + str(self.score)
            + " score"
            + " and is at: "
            + self.current_room.name
            + ", "
            + self.current_room.description
            + "\n"
        )

    def move(self, direction):

        # if this direction property is not None
        if self.current_room[f"{direction}_to"] != None:
            self.current_room = self.current_room[f"{direction}_to"]
            self.score += 1
        else:
            print("%sYou can't go in that direction %s" % (fg(1), attr(0)))

        # if direction == "n":
        #     if self.current_room.n_to:
        #         self.current_room = self.current_room.n_to
        #     else:
        #         print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
        # elif direction == "s":
        #     if self.current_room.s_to:
        #         self.current_room = self.current_room.s_to
        #     else:
        #         print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
        # elif direction == "w":
        #     if self.current_room.w_to:
        #         self.current_room = self.current_room.w_to
        #     else:
        #         print("%sYou can't go in that direction %s" % (fg(1), attr(0)))
        # elif direction == "e":
        #     if self.current_room.e_to:
        #         self.current_room = self.current_room.e_to
        #     else:
        #         print("%sYou can't go in that direction %s" % (fg(1), attr(0)))

    def pickItem(self, item_name):

        item = [x for i, x in enumerate(
            self.current_room.items) if x.name == item_name]

        if item:
            self.inventory.append(item[0])
            self.current_room.items.remove(item[0])
            item[0].on_take()
        else:
            print("%sThere's no item on the ground called: %s%s" %
                  (fg(1), item_name, attr(0)))

    def dropItem(self, item_name):

        item = [x for i, x in enumerate(
            self.inventory) if x.name == item_name]

        if item:
            self.current_room.items.append(item[0])
            self.inventory.remove(item[0])
            item[0].on_drop()
        else:
            print("%sThere's no item in your inventory called: %s%s" %
                  (fg(1), item_name, attr(0)))
