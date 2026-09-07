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