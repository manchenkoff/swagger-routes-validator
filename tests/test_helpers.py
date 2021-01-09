from openapi_parser.enumeration import OperationMethod
from openapi_parser.specification import Info, Operation, Path, PathItem, Response, Specification

from validator.helpers import get_swagger_routes, get_yaml_routes


def test_get_swagger_routes():
    specification = Specification(
        version='3.0.0',
        info=Info(
            title='Some example service',
            version='1.0.0',
            description='Example service specification'
        ),
        paths=[
            Path(
                pattern='/some/url',
                item=PathItem(
                    operations={
                        OperationMethod.GET: Operation(
                            summary='Operation description',
                            operation_id='getSomeItem',
                            responses={
                                200: Response(
                                    description='Successful response'
                                )
                            }
                        ),
                        OperationMethod.POST: Operation(
                            summary='Operation description',
                            operation_id='createSomeItem',
                            responses={
                                200: Response(
                                    description='Successful response'
                                )
                            }
                        ),
                    }
                ),
            )
        ],
    )

    assert ['GET /some/url', 'POST /some/url'] == get_swagger_routes(specification)


def test_get_yaml_routes():
    yaml = {
        'project.some_url': {
            'path': '/some/url',
            'defaults': {
                '_controller': 'project.controller.name'
            },
            'methods': ['GET', 'POST']
        }
    }

    assert ['GET /some/url', 'POST /some/url'] == get_yaml_routes(yaml)
