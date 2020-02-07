

class Field:
    tiles = None
    before = None
    after = None

    def __init__(self, tiles):
        self.tiles = tiles
        pass

    def add_field(self, field):
        self.after = field

    def get_after(self):
        return self.after

    def get_before(self):
        return self.before

    def draw(self, screen, offset):
        self.tiles.draw(screen, offset)
        if self.after is not None:
            self.after.draw(screen, offset + 1)
