from __future__ import annotations

import re


class ContactInfo:

    def __init__(self, email: str | None, phone: str | None):
        self._email = email
        self._phone = phone

    def is_valid(self) -> bool:
        if self._email is None or "@" not in self._email:
            return False
        if self._phone is None or len(self._phone) < 10:
            return False
        return True

    def formatted(self) -> str:
        return f"{self._email} | {self._phone}"


class Address:

    def __init__(self, city: str | None, zip_code: str | None):
        self._city = city
        self._zip_code = zip_code

    def is_valid(self) -> bool:
        if self._zip_code is None or not re.fullmatch(r"\d{5}-\d{3}", self._zip_code):
            return False
        return True

    def formatted(self) -> str:
        return f"{self._city} - {self._zip_code}"


class StudentRegistration:

    def __init__(self, name: str | None, email: str | None, phone: str | None,
                 city: str | None, zip_code: str | None):
        self._name = name
        self._contact = ContactInfo(email, phone)
        self._address = Address(city, zip_code)

    def is_valid(self) -> bool:
        if self._name is None or self._name.strip() == "":
            return False
        return self._contact.is_valid() and self._address.is_valid()

    def formatted_contact(self) -> str:
        return f"{self._name} | {self._contact.formatted()} | {self._address.formatted()}"
