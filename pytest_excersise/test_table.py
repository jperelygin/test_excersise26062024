import pytest


@pytest.mark.parametrize("expected_value", [10e7, 1.5 * 10e7, 5 * 10e7, 10e8, 5 * 10e8, 10e9, 1.5 * 10e9])
def test_popularity(parse_languages, expected_value):
    langs = parse_languages
    expected_value = int(expected_value)
    for lang in langs:
        assert_text =  f"{lang.website} (Frontend:{lang.frontend}|Backend:{lang.backend}) has {lang.popularity} unique visitors per month. (Expected more then {expected_value})"
        assert lang.popularity >= expected_value, assert_text