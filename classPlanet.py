XCR = 0; YCR = 1

class Planet:
    def __init__(self, name, typ, coordinates):
        self.name = name
        self.typ = typ
        self.coordinates_x = coordinates[XCR]
        self.coordinates_y = coordinates[YCR]
