# helix.spark is b.well's own image. Per CIE-8032 it is published to the services
# account's private ECR (it is not an upstream image, so root.io does not mirror it).
# Tag is unchanged on purpose: 3.5.5.0 == Spark 3.5.5, which must match the
# pyspark==3.5.5 pin in Pipfile. Requires `make ecr-login` locally - see README.
FROM 856965016623.dkr.ecr.us-east-1.amazonaws.com/helix.spark:3.5.5.0-slim
# https://github.com/icanbwell/helix.spark
USER root

ENV PYTHONPATH=/sfs
ENV CLASSPATH=/sfs/jars:$CLASSPATH

COPY Pipfile Pipfile.lock /sfs/
WORKDIR /sfs

RUN df -h # for space monitoring
RUN pipenv sync --system --dev --extra-pip-args="--prefer-binary"

# override entrypoint to remove extra logging
RUN mv /opt/minimal_entrypoint.sh /opt/entrypoint.sh

USER root

COPY . /sfs

RUN df -h # for space monitoring
RUN mkdir -p /fhir && chmod 777 /fhir
RUN mkdir -p /.local/share/virtualenvs && chmod 777 /.local/share/virtualenvs
# USER 1001

# Run as non-root user
# https://spark.apache.org/docs/latest/running-on-kubernetes.html#user-identity
USER 185