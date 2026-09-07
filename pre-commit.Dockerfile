# Aikido CUSTOM-RULE-2300 flags this line (issue 506324628) because it is not the
# root.io ECR mirror. Deliberately left on Docker Hub for now - see below.
#
# This image carries no Spark, and `python` IS in root_repo_list in
# rootio-terraform/terraform/environment/svc/us-east-1/common.vars, so unlike
# spark.Dockerfile this file *could* be flipped in one line:
#
#   FROM 856965016623.dkr.ecr.us-east-1.amazonaws.com/root-mirror/python:3.12-slim
#
# Verified with Aikido's own engine (aikido_full_scan, 2026-09-08): that line
# clears CUSTOM-RULE-2300, the only rule at stake here (CUSTOM-RULE-559 keys on
# the imranq2 namespace and never fired on this file). CUSTOM-RULE-2576 ("use
# Alpine") still fires either way - it fires on real Alpine images too, so it is
# a rule bug, not something this file can fix.
#
# Why it is NOT flipped:
#  1. No `root-mirror/*:*-slim` tag is in use anywhere in the icanbwell org except
#     bwell_Platform's python:3.7-slim-bookworm. Every other consumer
#     (fhir_to_llm, patient-intake-service, helix.providersearch,
#     helix-event-listener-service) uses -alpine. So root-mirror/python:3.12-slim
#     is unlikely to exist, and there were no AWS credentials to confirm it.
#  2. Pulling from a private ECR breaks this PUBLIC repo for forks and external
#     contributors, whose CI cannot obtain services-account credentials.
#
# If root-mirror is adopted here later, use the proven-working shape rather than
# -slim: `root-mirror/python:3.12-alpine3.22` plus
# `apk add --no-cache git build-base` in place of the apt-get layer below
# (copy icanbwell/fhir_to_llm's pre-commit.Dockerfile).
#
# To get a tag mirrored, there is a self-service API - no CIE ticket needed:
#   https://github.com/icanbwell/aikido-image-sync
#   POST https://aikido-image-sync.services.bwell.zone/request  {"image":"python:3.12-alpine3.22"}
#   POST https://aikido-image-sync.services.bwell.zone/mirror   {"image":"python:3.12-alpine3.22"}
FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y git && \
    pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --system --dev --verbose

WORKDIR /sourcecode
RUN git config --global --add safe.directory /sourcecode

CMD ["pre-commit", "run", "--all-files"]

# don't default to root.  pre-commit-hook overrides this at runtime with
# --user "$(id -u):$(id -g)" so the bind-mounted /sourcecode stays writable
# whatever UID the host uses.
USER 1001
