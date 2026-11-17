import importlib

import pytest

from refatoracao.q5.password_reset_notification import PasswordResetNotification


def test_render_should_contain_subject_and_body():
    n = PasswordResetNotification("Joelma")
    r = n.render()

    assert "Redefinição de senha" in r
    assert "Olá Joelma" in r


def test_refactor_goal_collapse_hierarchy_remove_redundant_subclass():
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("refatoracao.q5.vip_password_reset_notification")
