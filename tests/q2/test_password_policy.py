from refatoracao.q2.password_policy import PasswordPolicy


def test_valid_password_examples():
    policy = PasswordPolicy()
    assert policy.is_valid("SenhaForte1")
    assert policy.is_valid("OutraSenha99")


def test_invalid_password_examples():
    policy = PasswordPolicy()
    assert not policy.is_valid(None)            # nula
    assert not policy.is_valid("curta1A")       # < 10
    assert not policy.is_valid("senhaforte1")   # sem maiúscula
    assert not policy.is_valid("SenhaForteX")   # sem dígito
    assert not policy.is_valid("Senha Forte1")  # espaço


def test_refactor_goal_inline_some_helpers():
    policy = PasswordPolicy()
    assert not hasattr(policy, "_has_min_length")
    assert not hasattr(policy, "_has_upper")
    assert not hasattr(policy, "_has_digit")
    assert not hasattr(policy, "_has_no_spaces")
