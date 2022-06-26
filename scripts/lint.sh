#!/bin/bash

set -e

poetry run mypy xml_transformations
poetry run flake8 xml_transformations tests