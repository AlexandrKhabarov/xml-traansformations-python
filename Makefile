SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy xml_transformations
	poetry run flake8 xml_transformations tests

.PHONY: unit
unit:
	poetry run pytest tests

.PHONY: package
package:
	poetry run poetry check
	poetry run pip check

.PHONY: build
build:
	poetry build -f wheel

.PHONY: test
test: lint unit package