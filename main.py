class Product:
    def __init__(self, pid, name, price, qty):
        self.pid   = pid
        self.name  = name
        self.price = price
        self.qty   = qty

    def __str__(self):
        return f"[{self.pid}] {self.name} — {self.price:,} so'm x{self.qty}"

class Inventory:
    def __init__(self):
        self._items = {}

    def add(self, pid, name, price, qty):
        if pid in self._items:
            self._items[pid].qty += qty
        else:
            self._items[pid] = Product(pid, name, price, qty)

    def sell(self, pid, qty):
        p = self._items.get(pid)
        if not p:             raise KeyError("Mahsulot topilmadi")
        if p.qty < qty:       raise ValueError("Yetarli miqdor yo'q")
        p.qty -= qty
        return p.price * qty

    def low_stock(self, threshold=5):
        return [p for p in self._items.values() if p.qty <= threshold]

    def total_value(self):
        return sum(p.price * p.qty for p in self._items.values())

    def report(self):
        print(f"\n{'='*45}")
        for p in self._items.values(): print(" ", p)
        print(f"  Jami qiymat: {self.total_value():,} so'm")
        print(f"{'='*45}")

if __name__ == "__main__":
    inv = Inventory()
    inv.add(1, "Olma",    3000, 50)
    inv.add(2, "Banan",   5000, 4)
    inv.add(3, "Gilos",  12000, 20)

    inv.report()
    earned = inv.sell(1, 10)
    print(f"Tushum: {earned:,} so'm")

    print("Kam qolganlar:")
    for p in inv.low_stock():
        print(" ", p)
