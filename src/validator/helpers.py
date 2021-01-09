from typing import List

import yaml
from openapi_parser.specification import Specification


def get_swagger_routes(specification: Specification) -> List[str]:
    path_list = []

    for path in specification.paths:
        for method, operation in path.item.operations.items():
            path_list.append(f"{method.name} {path.pattern}")

    return path_list


def get_yaml_routes(data: dict) -> List[str]:
    path_list = []

    for item, config in data.items():
        for method in config['methods']:
            path_list.append(f"{method} {config['path']}")

    return path_list


def build_application_routes(files_path: str) -> List[str]:
    files = files_path.split(',')

    path_list = []

    for file in files:
        with open(file) as stream:
            data = yaml.safe_load(stream)
            path_list.extend(get_yaml_routes(data))

    return path_list
