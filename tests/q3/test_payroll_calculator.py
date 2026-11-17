import pytest

from refatoracao.q3.payroll_calculator import Employee, Overtime, PayrollCalculator


def test_net_salary_examples():
    calc = PayrollCalculator()

    e1 = Employee(
        2800,
        [Overtime(10, 25)],
        True,
        120,
    )
    salary1 = calc.monthly_net_salary(e1)
    assert salary1 == pytest.approx(
        2800 + (10 * 25) - ((2800 + (10 * 25)) * 0.12) - 120 + 450, abs=0.01
    )

    e2 = Employee(
        7500,
        [],
        False,
        200,
    )
    salary2 = calc.monthly_net_salary(e2)
    assert salary2 == pytest.approx(7500 - (7500 * 0.18) - 200, abs=0.01)


def test_refactor_goal_replace_temps_with_queries():
    calc = PayrollCalculator()
    # faixa intermediária (12%) com várias horas extras
    e = Employee(5000, [Overtime(10, 20), Overtime(5, 40)], True, 100)
    gross = 5000 + 200 + 200
    assert calc.monthly_net_salary(e) == pytest.approx(
        gross - gross * 0.12 - 100 + 450, abs=0.01
    )
    # limite exato da faixa de 8%
    e = Employee(3000, [], False, 0)
    assert calc.monthly_net_salary(e) == pytest.approx(3000 * 0.92, abs=0.01)
