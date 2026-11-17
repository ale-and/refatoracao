from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str | None
    banned: bool

    def is_banned(self) -> bool:
        return self.banned

    def greeting(self) -> str:
        if self.is_banned():
            return "Conta bloqueada. Contate o suporte."
        if self.name is None or self.name.strip() == "":
            return "Olá! Como posso ajudar?"
        return f"Olá, {self.name}! Como posso ajudar?"


class GuestUser(User):
    """Null Object: representa a ausência de usuário."""

    def __init__(self):
        super().__init__(name=None, banned=False)

    def greeting(self) -> str:
        return "Olá! Quer continuar como visitante?"


GUEST = GuestUser()


class SupportChat:

    def greeting(self, user: User | None) -> str:
        return (user or GUEST).greeting()
