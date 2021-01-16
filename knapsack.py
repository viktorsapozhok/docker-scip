from pyscipopt import Model, quicksum


class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item '{self.name}' (weight {self.weight})"


if __name__ == "__main__":
    # maximum weight capacity to be included in knapsack
    max_weight = 67
    # list of all items
    items = [
        Item("A", 505, 23), Item("B", 352, 26), Item("C", 458, 20),
        Item("D", 220, 18), Item("E", 354, 32), Item("F", 414, 27),
        Item("G", 498, 29), Item("H", 545, 26), Item("I", 473, 30),
        Item("J", 543, 27)
    ]

    model = Model()

    # init variables
    x = dict()
    for item in items:
        x[item.name] = model.addVar(vtype="B")

    model.addCons(
        quicksum(item.weight * x[item.name] for item in items) <= max_weight)

    model.setObjective(
        quicksum(item.value * x[item.name] for item in items),
        sense="maximize")

    model.optimize()

    print("\nsolution:")
    for item in items:
        if model.getVal(x[item.name]) > 0.5:
            print(str(item) + " in knapsack")
        else:
            print(str(item))
