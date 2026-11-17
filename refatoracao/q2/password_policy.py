from __future__ import annotations


class PasswordPolicy:

    def is_valid(self, password: str | None) -> bool:
        return (
            password is not None
            and len(password) >= 10
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and " " not in password
        )
