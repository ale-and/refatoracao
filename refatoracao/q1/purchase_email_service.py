from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PurchaseItem:
    name: str
    quantity: int
    unit_price: float

    def total_price(self) -> float:
        return self.unit_price * self.quantity


@dataclass(frozen=True)
class Address:
    street: str
    number: str
    city: str
    zip_code: str


@dataclass(frozen=True)
class Purchase:
    id: str
    customer_name: str
    items: list[PurchaseItem]
    is_express: bool
    coupon: str | None
    address: Address


class PurchaseEmailService:

    def build_email(self, purchase: Purchase) -> str:
        subtotal = self._calculate_subtotal(purchase)
        shipping = self._calculate_shipping(purchase)
        discount = self._calculate_discount(purchase, subtotal)
        total = subtotal + shipping - discount

        return "".join([
            self._build_header(purchase),
            self._build_items_section(purchase),
            self._build_summary_section(subtotal, shipping, discount, total),
            self._build_address_section(purchase.address),
            self._build_footer(),
        ])

    def _build_header(self, purchase: Purchase) -> str:
        return (
            f"Olá, {purchase.customer_name}!\n\n"
            f"Seu pedido #{purchase.id} foi confirmado em {date.today()}.\n\n"
        )

    def _build_items_section(self, purchase: Purchase) -> str:
        lines = ["Itens:\n"]
        for item in purchase.items:
            lines.append(
                f"- {item.name} ({item.quantity}x) : R$ {item.total_price():.2f}\n"
            )
        return "".join(lines)

    def _calculate_subtotal(self, purchase: Purchase) -> float:
        return sum(item.total_price() for item in purchase.items)

    def _calculate_shipping(self, purchase: Purchase) -> float:
        return 29.90 if purchase.is_express else 14.90

    def _calculate_discount(self, purchase: Purchase, subtotal: float) -> float:
        discount = subtotal * 0.10 if subtotal >= 300.0 else 0.0
        if purchase.coupon is not None and purchase.coupon.startswith("VIP"):
            discount += 20.0
        return discount

    def _build_summary_section(
        self, subtotal: float, shipping: float, discount: float, total: float
    ) -> str:
        return (
            f"\nSubtotal: R$ {subtotal:.2f}\n"
            f"Frete: R$ {shipping:.2f}\n"
            f"Descontos: R$ {discount:.2f}\n"
            f"TOTAL: R$ {total:.2f}\n\n"
        )

    def _build_address_section(self, address: Address) -> str:
        return (
            "Endereço de entrega:\n"
            f"{address.street}, {address.number}\n"
            f"{address.city} - {address.zip_code}\n\n"
        )

    def _build_footer(self) -> str:
        return "Obrigado por comprar com a gente!\n"
