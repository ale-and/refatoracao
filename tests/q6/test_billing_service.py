import pytest

from refatoracao.q6.billing_service import BillingService, Plan


def test_price_table_examples():
    svc = BillingService()

    assert svc.monthly_price(Plan.FREE, 10, False) == pytest.approx(0.0, abs=0.001)
    assert svc.monthly_price(Plan.STUDENT, 10, False) == pytest.approx(19.90, abs=0.001)

    assert svc.monthly_price(Plan.PRO, 10, False) == pytest.approx(49.90 + 10 * 1.25, abs=0.01)
    assert svc.monthly_price(Plan.PRO, 250, False) == pytest.approx(
        (49.90 + 250 * 1.25) * 0.95, abs=0.01
    )

    assert svc.monthly_price(Plan.ENTERPRISE, 10, True) == pytest.approx(
        199.90 + 10 * 0.90 + 59.90, abs=0.01
    )


def test_refactor_goal_replace_conditional_with_polymorphism():
    svc = BillingService()

    # suporte prioritário não cobra no FREE
    assert svc.monthly_price(Plan.FREE, 10, True) == pytest.approx(0.0, abs=0.001)
    assert svc.monthly_price(Plan.STUDENT, 10, True) == pytest.approx(19.90 + 59.90, abs=0.01)

    # desconto de 5% do PRO vale só acima de 200 usuários e inclui o suporte
    assert svc.monthly_price(Plan.PRO, 200, False) == pytest.approx(49.90 + 200 * 1.25, abs=0.01)
    assert svc.monthly_price(Plan.PRO, 250, True) == pytest.approx(
        (49.90 + 250 * 1.25 + 59.90) * 0.95, abs=0.01
    )
    # ENTERPRISE não tem desconto por volume
    assert svc.monthly_price(Plan.ENTERPRISE, 500, False) == pytest.approx(
        199.90 + 500 * 0.90, abs=0.01
    )
