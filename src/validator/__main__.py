from argparse import ArgumentParser, Namespace
from typing import List

from colorama import Fore, init as colorama_init, Style
from openapi_parser import parse

from .helpers import build_application_routes, get_swagger_routes


def parse_arguments() -> Namespace:
    arg_parser = ArgumentParser(description="Swagger validation parameters")

    arg_parser.add_argument('--swagger', type=str, required=True, help='path to OpenAPI file', metavar='file')
    arg_parser.add_argument('--routes', type=str, required=True, help='path to YAML routes files (separated by comma)',
                            metavar='file1,file2')

    return arg_parser.parse_args()


def check_coverage(swagger_routes: List[str], application_routes: List[str]) -> None:
    full_set, covered_set = set(application_routes), set(swagger_routes)

    diff = covered_set.difference(full_set)

    colorama_init(autoreset=True)

    if not diff:
        print(f"{Fore.GREEN}Swagger API routes validation SUCCEED!")
        return

    print(f"{Fore.RED}Swagger API routes validation FAILED!\n")
    print(f"{Fore.YELLOW}Non-existed endpoints:")

    for url in diff:
        print(f"{Style.BRIGHT} - {url}")

    exit(1)


def run() -> None:
    args = parse_arguments()

    specification = parse(args.swagger)

    swagger_routes = get_swagger_routes(specification)
    application_routes = build_application_routes(args.routes)

    check_coverage(swagger_routes, application_routes)


if __name__ == '__main__':
    run()
