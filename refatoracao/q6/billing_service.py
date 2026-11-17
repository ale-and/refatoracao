from abc import ABC, abstractmethod
from enum import Enum


class Plan(Enum):
    FREE = "FREE"
    STUDENT = "STUDENT"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"


class PlanPricing(ABC):
    support_fee = 59.90

    @abstractmethod
    def base_price(self, active_users: int) -> float: ...

    def priority_support_price(self, priority_support: bool) -> float:
        return self.support_fee if priority_support else 0.0

    def adjust(self, price: float, active_users: int) -> float:
        return price

    def monthly_price(self, active_users: int, priority_support: bool) -> float:
        price = self.base_price(active_users) + self.priority_support_price(priority_support)
        return round(self.adjust(price, active_users), 2)


class FreePricing(PlanPricing):
    def base_price(self, active_users: int) -> float:
        return 0.0

    def priority_support_price(self, priority_support: bool) -> float:
        return 0.0


class StudentPricing(PlanPricing):
    def base_price(self, active_users: int) -> float:
        return 19.90


class ProPricing(PlanPricing):
    def base_price(self, active_users: int) -> float:
        return 49.90 + (active_users * 1.25)

    def adjust(self, price: float, active_users: int) -> float:
        return price * 0.95 if active_users > 200 else price


class EnterprisePricing(PlanPricing):
    def base_price(self, active_users: int) -> float:
        return 199.90 + (active_users * 0.90)


_PRICING = {
    Plan.FREE: FreePricing(),
    Plan.STUDENT: StudentPricing(),
    Plan.PRO: ProPricing(),
    Plan.ENTERPRISE: EnterprisePricing(),
}


class BillingService:

    def monthly_price(self, plan: Plan, active_users: int, priority_support: bool) -> float:
        pricing = _PRICING.get(plan)
        if pricing is None:
            raise ValueError()
        return pricing.monthly_price(active_users, priority_support)
