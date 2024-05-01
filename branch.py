class Branch:
    def __init__(self, name):
        self.name = name
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)
