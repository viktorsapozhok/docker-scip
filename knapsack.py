from pyscipopt import Model, quicksum


class Item:
    def __init__(self, index, weight, value):
        self.index = index
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item {self.index}: weight {self.weight}, value {self.value}"


class Bin:
    def __init__(self, index, capacity):
        self.index = index
        self.capacity = capacity

    def __repr__(self):
        return f"Bin {self.index}"


if __name__ == "__main__":
    items = [
        Item(1, 48, 10), Item(2, 30, 30), Item(3, 42, 25),
        Item(4, 36, 50), Item(5, 36, 35), Item(6, 48, 30),
        Item(7, 42, 15), Item(8, 42, 40), Item(9, 36, 30),
        Item(10, 24, 35), Item(11, 30, 45), Item(12, 30, 10),
        Item(13, 42, 20), Item(14, 36, 30), Item(15, 36, 25)
    ]

    bins = [
        Bin(1, 100), Bin(2, 100), Bin(3, 100), Bin(4, 100), Bin(5, 100)
    ]

    model = Model()
    x = dict()

    for _item in items:
        for _bin in bins:
            x[_item.index, _bin.index] = model.addVar(vtype="B")

    for _item in items:
        model.addCons(
            quicksum(x[_item.index, _bin.index] for _bin in bins) <= 1)

    for _bin in bins:
        model.addCons(
            quicksum(
                _item.weight * x[_item.index, _bin.index] for _item in items
            ) <= _bin.capacity)

    model.setObjective(
        quicksum(
            _item.value * x[_item.index, _bin.index]
            for _item in items for _bin in bins
        ),
        sense="maximize")

    model.optimize()
    print("\n")

    for _bin in bins:
        bin_weight = 0
        bin_value = 0
        print(_bin)
        for _item in items:
            if model.getVal(x[_item.index, _bin.index]) > 0.5:
                bin_weight += _item.weight
                bin_value += _item.value
                print(_item)

        print(f"Packed bin weight: {bin_weight}")
        print(f"Packed bin value : {bin_value}\n")

    print(f"Total packed value: {model.getObjVal():.1f}\n")
