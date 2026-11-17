from refatoracao.q8.student_registration import Address, ContactInfo, StudentRegistration


def test_validity_examples():
    ok = StudentRegistration("Juremilda", "n@x.com", "9199999999", "Belém", "66000-000")
    assert ok.is_valid()

    bad_zip = StudentRegistration("Juremilda", "n@x.com", "9199999999", "Belém", "66000000")
    assert not bad_zip.is_valid()


def test_invalid_fields_are_rejected():
    assert not StudentRegistration("  ", "n@x.com", "9199999999", "Belém", "66000-000").is_valid()
    assert not StudentRegistration(None, "n@x.com", "9199999999", "Belém", "66000-000").is_valid()
    assert not StudentRegistration("Ana", "nx.com", "9199999999", "Belém", "66000-000").is_valid()
    assert not StudentRegistration("Ana", "n@x.com", "999", "Belém", "66000-000").is_valid()
    assert not StudentRegistration("Ana", "n@x.com", "9199999999", "Belém", None).is_valid()


def test_formatted_contact_example():
    s = StudentRegistration("Max", "v@ufpa.br", "91988887777", "Belém", "66000-000")
    assert s.formatted_contact() == "Max | v@ufpa.br | 91988887777 | Belém - 66000-000"


def test_refactor_goal_extract_class_contact_and_address():
    assert ContactInfo("a@b.com", "9199999999").is_valid()
    assert not ContactInfo("ab.com", "9199999999").is_valid()
    assert Address("Belém", "66000-000").is_valid()
    assert not Address("Belém", "66000000").is_valid()
    assert Address("Belém", "66000-000").formatted() == "Belém - 66000-000"
