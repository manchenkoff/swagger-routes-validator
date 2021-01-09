.DEFAULT_GOAL := help
.PHONY: help build test

build: ## Build an application
	@pipenv run python setup.py sdist bdist_wheel

install: build ## Install application to Pip environment
	@pipenv run python setup.py install

install-dev: ## Install application to Pip development environment
	@pipenv run python setup.py develop
	@make clean

clean: ## Remove build files
	@rm -Rf build/ dist/ *.egg-info .pytest_cache/ .mypy_cache/ .pytype/ .eggs/ src/*.egg-info
	@echo "Temporary files were clear"

test: ## Run code tests
	@pipenv run python -m pytest -q

sync: ## Sync with Pipfile packages list
	@pipenv sync

lint: ## Run code linter
	@pipenv run mypy ./src

help: ## Show this message
	@echo "Application management"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'