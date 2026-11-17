from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    vip: bool
    years_as_customer: int

    def is_vip(self) -> bool:
        return self.vip

    def loyalty_discount(self) -> float:
        discount = 0.0
        if self.is_vip():
            discount += 25.0
        if self.years_as_customer >= 5:
            discount += 15.0
        return discount


class Order:

    def __init__(self, customer: Customer, total: float, discount_rate: float):
        self._customer = customer
        self._total = total
        self._discount_rate = discount_rate

    def final_total(self) -> float:
        discount = self._total * self._discount_rate + self._customer.loyalty_discount()
        return max(0.0, self._total - discount)
