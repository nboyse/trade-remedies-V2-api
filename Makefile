SHELL := /bin/bash
APPLICATION_NAME="Trade Remedies API"

# Colour coding for output
COLOUR_NONE=\033[0m
COLOUR_GREEN=\033[32;01m
COLOUR_YELLOW=\033[33;01m

ifeq ($(APPLICATION_VERSION),)
APPLICATION_VERSION := "no version"
endif

.PHONY: help test
help:
	@echo -e "$(COLOUR_GREEN)|--- $(APPLICATION_NAME) [$(APPLICATION_VERSION)] ---|$(COLOUR_NONE)"
	@echo -e "$(COLOUR_YELLOW)make requirements$(COLOUR_NONE) : Generate all requirements (requires local pip-compile)"

all-requirements:
	pip-compile --output-file requirements.txt requirements.in

up:
	docker-compose up

first-use:
	docker-compose build
	docker-compose up
