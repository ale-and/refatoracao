from datetime import date

from refatoracao.q1.purchase_email_service import (
    Address,
    Purchase,
    PurchaseEmailService,
    PurchaseItem,
)


def test_build_email_should_keep_same_output_after_refactor():
    svc = PurchaseEmailService()

    purchase = Purchase(
        "123",
        "Victor",
        [
            PurchaseItem("Caderno", 2, 15.0),
            PurchaseItem("Caneta", 3, 3.5),
        ],
        False,
        "VIP-20",
        Address("Rua A", "10", "Belém", "66000-000"),
    )

    email = svc.build_email(purchase)

    expected = (
        "Olá, Victor!\n\n"
        f"Seu pedido #123 foi confirmado em {date.today()}.\n\n"
        "Itens:\n"
        "- Caderno (2x) : R$ 30.00\n"
        "- Caneta (3x) : R$ 10.50\n"
        "\nSubtotal: R$ 40.50\n"
        "Frete: R$ 14.90\n"
        "Descontos: R$ 20.00\n"
        "TOTAL: R$ 35.40\n\n"
        "Endereço de entrega:\n"
        "Rua A, 10\n"
        "Belém - 66000-000\n\n"
        "Obrigado por comprar com a gente!\n"
    )
    assert email == expected


def test_build_email_with_express_shipping_and_high_subtotal_discount():
    svc = PurchaseEmailService()

    purchase = Purchase(
        "456",
        "Ana",
        [PurchaseItem("Livro", 3, 100.0)],
        True,
        None,
        Address("Av. Nazaré", "200", "Belém", "66035-000"),
    )

    email = svc.build_email(purchase)

    assert "Subtotal: R$ 300.00" in email
    assert "Frete: R$ 29.90" in email
    assert "Descontos: R$ 30.00" in email
    assert "TOTAL: R$ 299.90" in email
