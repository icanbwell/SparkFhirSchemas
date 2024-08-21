LANG=en_US.utf-8

export LANG

Pipfile.lock: Pipfile
	docker compose run --rm --name spark_fhir_schemas dev sh -c "rm -f Pipfile.lock && pipenv lock --dev"

.PHONY:devdocker
devdocker: ## Builds the docker for dev
	docker compose build --no-cache

.PHONY:init
init: devdocker up setup-pre-commit  ## Initializes the local developer environment

.PHONY:build
build: ## Builds the docker for dev
	docker compose build --progress=plain --parallel

.PHONY: up
up: Pipfile.lock
	docker compose up --build -d

.PHONY: down
down: ## Brings down all the services in docker-compose
	export DOCKER_CLIENT_TIMEOUT=300 && export COMPOSE_HTTP_TIMEOUT=300
	docker compose down --remove-orphans && \
	docker system prune -f

.PHONY:clean-pre-commit
clean-pre-commit: ## removes pre-commit hook
	rm -f .git/hooks/pre-commit

.PHONY:setup-pre-commit
setup-pre-commit: Pipfile.lock
	cp ./pre-commit-hook ./.git/hooks/pre-commit

.PHONY:run-pre-commit
run-pre-commit: setup-pre-commit
	./.git/hooks/pre-commit

.PHONY:update
update: Pipfile.lock setup-pre-commit  ## Updates all the packages using Pipfile
	docker compose run --rm --name sfs_pipenv dev pipenv sync --dev && \
	make devdocker && \
	make pipenv-setup

.PHONY:tests
tests: up
	docker compose run --rm --name sfs_tests dev pytest tests

.PHONY: sphinx-html
sphinx-html:
	docker compose run --rm --name spark_fhir_schemas dev make -C docsrc html
	@echo "copy html to docs... why? https://github.com/sphinx-doc/sphinx/issues/3382#issuecomment-470772316"
	@rm -rf docs/*
	@touch docs/.nojekyll
	cp -a docsrc/_build/html/. docs

.PHONY:pipenv-setup
pipenv-setup:devdocker ## Run pipenv-setup to update setup.py with latest dependencies
	docker compose run --rm --name spark_data_frame_comparer dev sh -c "pipenv run pipenv install --skip-lock --categories \"pipenvsetup\" && pipenv run pipenv-setup sync --pipfile" && \
	make run-pre-commit

.PHONY:shell
shell:devdocker ## Brings up the bash shell in dev docker
	docker compose run --rm --name sfs_shell dev /bin/bash

.PHONY:schema-r4
schema-r4:
	docker compose run --rm --name sfs_shell dev python3 spark_fhir_schemas/r4/generate_schema.py && \
	make run-pre-commit
	make run-pre-commit

.PHONY:schema-r4b
schema-r4b:
	docker compose run --rm --name sfs_shell dev python3 spark_fhir_schemas/r4b/generate_schema.py && \
	make run-pre-commit
	make run-pre-commit

.PHONY:schema-stu3
schema-stu3:
	docker compose run --rm --name sfs_shell dev python3 spark_fhir_schemas/stu3/generate_schema.py && \
	make run-pre-commit
	make run-pre-commit

.PHONY:schema-dstu2
schema-dstu2:
	docker compose run --rm --name sfs_shell dev python3 spark_fhir_schemas/dstu2/generate_schema_file.py && \
	docker compose run --rm --name sfs_shell dev python3 spark_fhir_schemas/dstu2/generate_schema.py && \
	make run-pre-commit
	make run-pre-commit
