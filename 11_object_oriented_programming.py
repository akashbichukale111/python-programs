"""
Module 11: Object-Oriented Programming (OOP)
Contains 5 programs ranging from basic classes to advanced OOP patterns:
1. Class, constructor (__init__), and instance methods
2. Inheritance (single and multi-level)
3. Encapsulation using private variables and @property getters/setters
4. Polymorphism and method overriding
5. Class methods (@classmethod) and static methods (@staticmethod)
"""

# Program 1: Basic Class & Methods
class Vehicle:
    def __init__(self, brand: str, speed_limit: int):
        self.brand = brand
        self.speed_limit = speed_limit

    def describe(self) -> str:
        return f"{self.brand} vehicle with max speed {self.speed_limit} km/h"

# Program 2: Inheritance
class ElectricCar(Vehicle):
    def __init__(self, brand: str, speed_limit: int, battery_kwh: int):
        super().__init__(brand, speed_limit)
        self.battery_kwh = battery_kwh

    def describe(self) -> str:
        base = super().describe()
        return f"{base} [Electric: {self.battery_kwh} kWh pack]"

# Program 3: Encapsulation & Properties
class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        self.__balance = max(0.0, initial_balance)

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__balance += amount
            return True
        return False

# Program 4: Polymorphism
class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height

# Program 5: Classmethod & Staticmethod
class GovernanceLedger:
    total_entries = 0

    def __init__(self, name: str):
        self.name = name
        GovernanceLedger.total_entries += 1

    @classmethod
    def get_ledger_count(cls) -> int:
        return cls.total_entries

    @staticmethod
    def is_valid_signature(sig: str) -> bool:
        return len(sig) == 64 and all(c in "0123456789abcdefABCDEF" for c in sig)

if __name__ == "__main__":
    print("=== Module 11: Object-Oriented Programming ===")
    v = Vehicle("Standard", 120)
    print("[P1]", v.describe())
    ev = ElectricCar("Tesla", 250, 100)
    print("[P2]", ev.describe())
    acc = BankAccount("Akash", 500.0)
    acc.deposit(250.0)
    print("[P3] Protected balance:", acc.balance)
    shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]
    areas = [round(s.area(), 2) for s in shapes]
    print("[P4] Polymorphic areas:", areas)
    g1 = GovernanceLedger("Audit-01")
    g2 = GovernanceLedger("Audit-02")
    print("[P5] Total ledgers:", GovernanceLedger.get_ledger_count(),
          "| Valid hash?", GovernanceLedger.is_valid_signature("a" * 64))
