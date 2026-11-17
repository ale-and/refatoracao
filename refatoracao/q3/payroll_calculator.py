from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Overtime:
    hours: int
    hour_rate: float


@dataclass(frozen=True)
class Employee:
    base_salary: float
    overtimes: list[Overtime]
    has_meal_voucher: bool
    health_plan_deduction: float


class PayrollCalculator:

    def monthly_net_salary(self, e: Employee) -> float:
        net = (
            self._gross(e)
            - self._tax(e)
            - self._health_plan(e)
            + self._meal_voucher(e)
        )
        return round(net, 2)

    def _overtime(self, e: Employee) -> float:
        return sum(ot.hours * ot.hour_rate for ot in e.overtimes)

    def _gross(self, e: Employee) -> float:
        return e.base_salary + self._overtime(e)

    def _tax(self, e: Employee) -> float:
        gross = self._gross(e)
        if gross <= 3000:
            return gross * 0.08
        if gross <= 7000:
            return gross * 0.12
        return gross * 0.18

    def _meal_voucher(self, e: Employee) -> float:
        return 450.0 if e.has_meal_voucher else 0.0

    def _health_plan(self, e: Employee) -> float:
        return e.health_plan_deduction
