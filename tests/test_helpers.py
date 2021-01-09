from validator.helpers import get_swagger_routes, get_yaml_routes


def test_get_swagger_routes():
    assert [] == get_swagger_routes(None)


def test_get_yaml_routes():
    assert [] == get_yaml_routes({}, '')
