from argparse import ArgumentParser, Namespace
from typing import List, Set

import yaml
from colorama import Fore, init as colorama_init, Style
from openapi_parser import parse

from .helpers import build_application_routes, get_swagger_routes


def parse_arguments() -> Namespace:
    arg_parser = ArgumentParser(description="Swagger validation parameters")
    arg_parser.add_argument('--config', type=str, required=True, help='path to validation config', metavar='file')

    return arg_parser.parse_args()


def load_config(config_path: str) -> dict:
    with open(config_path) as stream:
        return yaml.safe_load(stream)


def show_unused_list(unused_routes: Set[str]) -> None:
    if not unused_routes:
        return

    print(f"{Fore.YELLOW}Unused endpoints:")

    for url in unused_routes:
        print(f"{Style.BRIGHT} - {url}")


def show_uncovered_list(uncovered_routes: Set[str]) -> None:
    if not uncovered_routes:
        return

    print(f"{Fore.YELLOW}Non-existed endpoints:")

    for url in uncovered_routes:
        print(f"{Style.BRIGHT} - {url}")


def check_coverage(swagger_routes: List[str], application_routes: List[str]) -> None:
    full_set, covered_set = set(application_routes), set(swagger_routes)

    uncovered_routes = full_set.difference(covered_set)
    unused_routes = covered_set.difference(full_set)

    colorama_init(autoreset=True)

    if not uncovered_routes and not unused_routes:
        print(f"{Fore.GREEN}Swagger API routes validation SUCCEED!")
        return

    print(f"{Fore.RED}Swagger API routes validation FAILED!\n")

    show_uncovered_list(uncovered_routes)
    show_unused_list(unused_routes)

    exit(1)


def run() -> None:
    args = parse_arguments()

    config = load_config(args.config)

    specification = parse(config['swagger'])

    swagger_routes = get_swagger_routes(specification)
    application_routes = build_application_routes(config['routes'])

    check_coverage(swagger_routes, application_routes)


if __name__ == '__main__':
    run()
