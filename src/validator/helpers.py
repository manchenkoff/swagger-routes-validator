from typing import List

import yaml
from openapi_parser.specification import Specification


def get_swagger_routes(specification: Specification) -> List[str]:
    path_list = []

    for path in specification.paths:
        for method, operation in path.item.operations.items():
            path_list.append(f"{method.name} {path.pattern}")

    return path_list


def get_yaml_routes(data: dict, prefix: str = '') -> List[str]:
    path_list = []

    for item, config in data.items():
        if not config.get('methods'):
            path_list.append(f"GET {prefix}{config['path']}")
            continue

        for method in config['methods']:
            path_list.append(f"{method} {prefix}{config['path']}")

    return path_list


def build_application_routes(routes_config: dict) -> List[str]:
    path_list = []

    for name, config in routes_config.items():
        with open(config['path']) as stream:
            data = yaml.safe_load(stream)
            path_list.extend(get_yaml_routes(data, config.get('prefix', '')))

    return path_list
