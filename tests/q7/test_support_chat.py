from refatoracao.q7.support_chat import GUEST, GuestUser, SupportChat, User


def test_greeting_examples():
    chat = SupportChat()

    assert chat.greeting(None) == "Olá! Quer continuar como visitante?"
    assert chat.greeting(User("Ana", True)) == "Conta bloqueada. Contate o suporte."
    assert chat.greeting(User("  ", False)) == "Olá! Como posso ajudar?"
    assert chat.greeting(User("Victor", False)) == "Olá, Victor! Como posso ajudar?"


def test_refactor_goal_introduce_null_object_remove_null_check():
    chat = SupportChat()

    assert isinstance(GUEST, User)
    assert not GUEST.is_banned()
    assert chat.greeting(GuestUser()) == chat.greeting(None)
    assert chat.greeting(User(None, False)) == "Olá! Como posso ajudar?"
