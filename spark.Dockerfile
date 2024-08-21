FROM imranq2/helix.spark:3.5.1.3-slim
# https://github.com/icanbwell/helix.spark
USER root

ENV PYTHONPATH=/sfs
ENV CLASSPATH=/sfs/jars:$CLASSPATH

COPY Pipfile* /sfs/
WORKDIR /sfs

RUN df -h # for space monitoring
RUN pipenv sync --dev --system --extra-pip-args="--prefer-binary"

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