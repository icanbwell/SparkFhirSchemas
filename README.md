# SparkFhirSchemas


This project is a collection of [FHIR](https://www.hl7.org/fhir/) schemas for [Apache Spark](https://spark.apache.org/).

## Prerequisites for local development

`spark.Dockerfile` is now built from a base image in b.well's **services** AWS
account (`856965016623`) rather than Docker Hub:

| File | Base image | Why |
| --- | --- | --- |
| `spark.Dockerfile` | `856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark:3.5.5.0-slim` | [CIE-8032](https://icanbwell.atlassian.net/browse/CIE-8032) moved `helix.spark` off the `imranq2` Docker Hub namespace into the private services ECR. `helix.spark` is b.well's own image, so the root.io mirror does not carry it. |
| `pre-commit.Dockerfile` | `python:3.12-slim` (unchanged, public Docker Hub) | Needs no private registry. See the comment at the top of that file for the root.io-mirror option and why it was not taken. |

Because that is a private registry you must authenticate before building. This
applies to `make run-pre-commit` too: it depends on the `Pipfile.lock` target,
which always builds the `dev` service from `spark.Dockerfile`.

```bash
aws sso login --profile services   # once per session
make ecr-login                     # also run automatically by make build/up/run-pre-commit
```

`make ecr-login` uses the `services` profile by default; override with
`AWS_SERVICES_PROFILE=<profile> make ecr-login`, or set it to empty to use
ambient credentials (which is what CI does).

Do **not** change the `helix.spark` tag on its own: `3.5.5.0` means Spark 3.5.5
and must stay in step with the `pyspark==3.5.5` pin in `Pipfile`.

## Usage
1. First update the `fhir.schema.json` file with the FHIR schema you want to use.
   2. You can find the FHIR schema in the [FHIR specification](https://hl7.org/fhir/R4B/fhir.schema.json).
3. Run `make schema-RXX` to generate the Spark schema for RXX. Replace "XX" with the verison you desire. For instance if you want to update R4B you would run `make schema-R4B`.
4. Run `make schema-stu3` to generate the Spark schema for STU3.
5. Run `make schema-dstu2` to generate the Spark schema for DSTU2.

This will generate the Spark schema in the spark_fhir_schemas directory.
### Prerequisite: these base-image tags must exist in the services ECR

`helix.spark`'s publish workflows push **only to Docker Hub** — there is no ECR push step —
so the tags below do not reach `856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark`
unless someone copies them. Until they do, `docker build` here fails on a missing image.

| tag to copy | expected digest |
|---|---|
| `3.5.5.0-slim` | `sha256:e2c4762e38e3f57bfa99afdd68621c0be46eb373475c5578113c0e683b193126` |

Copy with a manifest-preserving tool. These are multi-arch (`linux/amd64` + `linux/arm64`);
a `docker pull`/`tag`/`push` cycle from an Apple-silicon Mac would push arm64 only and
silently break amd64 CI runners.

```bash
aws sso login --profile services
aws ecr get-login-password --region us-east-1 --profile services \
  | crane auth login 856965016623.dkr.ecr.us-east-1.amazonaws.com --username AWS --password-stdin
DEST=856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark
crane copy icanbwell/helix.spark:3.5.5.0-slim "$DEST:3.5.5.0-slim"
# verify:
crane digest "$DEST:3.5.5.0-slim"
```

Source is `icanbwell/helix.spark` (the icanbwell-owned namespace mandated by CIE-8032); it is
digest-identical to the old `imranq2/helix.spark`, so the copy is the same image bytes.

The tag itself is **derived, not chosen**: `A.B.C` in the tag is the Apache Spark version in
the image and must match this repo's `pyspark` pin. Do not change the tag as part of a
registry migration.

See `CIE-8032` for the full decision trail. Copying these tags does NOT by itself make CI
pass — this is a public repo on `ubuntu-latest` with no AWS identity, so a GitHub OIDC
trusted role scoped to `repo:icanbwell/SparkFhirSchemas:*` is still required.
