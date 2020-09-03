class Appliances:
    def __init__(self, weight, height, width):
        self._weight = weight
        self._height = height
        self._width = width
        self._info = f"Appliance's weight = {self._weight},\n height = {self._height},\n width = {self._width}"

    def set_location(self, place):
        if place != 'flat' or place != 'house':
            self._place = None
        self._place = place

    def get_location(self):
        return self._place

    location = property(get_location, set_location)


class KitchenInventory(Appliances):
    def __init__(self, weight, height, width, purpose):
        super().__init__(weight, height, width)
        self.purpose = purpose
        self._info = f"Kitchen inventory is purposed to {purpose}"

    def room_setter(self, room):
        if room != 'kitchen':
            self._room = None
        self._room = room

    def room_getter(self):
        return self._room

    room = property(room_getter, room_setter)


class Oven(KitchenInventory):
    def __init__(self, weight, height, width, f1, f2, f3):
        super().__init__(weight, height, width, f1)
        self.purpose = f1, f2, f3
        self._info = f"Oven's weight = {weight},\n height = {height},\n width = {width}\nOven can:{f1}, {f2}, {f3}"


class ElectricStove(Oven):
    def __init__(self, weight, height, width, f1):
        super().__init__(weight, height, width, f1, None, None)
        self.purpose = f1
        self._info = f"Electric stove's weight = {weight},\n height = {height},\n width = {width}\n" \
                     f"Electric stove is used to {f1}"


class GasStove(Oven):
    def __init__(self, weight, height, width, f1):
        super().__init__(weight, height, width, f1, None, None)
        self.purpose = f1
        self._info = f"Gas stove's weight = {weight},\n height = {height},\n width = {width}\nGas stove can {f1} dishes"


class Microwave(Oven):
    def __init__(self, weight, height, width, f1):
        super().__init__(weight, height, width, f1, None, None)
        self.purpose = f1
        self._info = f"Microwave's weight = {weight},\n height = {height},\n width = {width}\nMicrowave can {f1} dishes"


class Combine(KitchenInventory):
    def __init__(self, weight, height, width, purpose):
        super().__init__(weight, height, width, purpose)
        self.purpose = purpose
        self._info = f"Combine's weight = {weight},\n height = {height},\n width = {width}\n" \
                     f"Kitchen inventory is purposed to {purpose}"


class Iron(Appliances):
    def __init__(self, weight, height, width, purpose):
        super().__init__(weight, height, width)
        self.purpose = purpose
        self._info = f"Iron's weight = {self._weight},\n height = {self._height},\n width = {self._width}\n" \
                     f"With iron you can {purpose} clothes"


class WashingMachine(Appliances):
    def __init__(self, weight, height, width, purpose):
        super().__init__(weight, height, width)
        self.purpose = purpose
        self._info = f"Washing machine's weight = {self._weight},\n height = {self._height},\n width = {self._width}\n"\
                     f"Washing machine is purposed to {purpose} clothes"

def classes():
    A = Appliances(3, 4, 5)
    print(A._info)

    K = KitchenInventory(1, 2, 3, 'coocking')
    print(K._info)

    O = Oven(6, 7, 8, 'fry', 'boil', 'warm')
    print(O._info)

    E = ElectricStove(11, 22, 33, 'boil')
    print(E._info)

    G = GasStove(12, 23, 34, 'fry')
    print(G._info)

    M = Microwave(33, 44, 55, 'warm')
    print(M._info)

    I = Iron(21, 2, 4, 'iron')
    print(I._info)

    W = WashingMachine(40, 50, 30, 'wash')
    print(W._info)
