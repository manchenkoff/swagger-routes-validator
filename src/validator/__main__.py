import sys


def run() -> None:
    # python -m validator --swagger=some_swagger_file.yml --yaml=some_symfony_file.yml
    print(sys.argv)


if __name__ == '__main__':
    run()
