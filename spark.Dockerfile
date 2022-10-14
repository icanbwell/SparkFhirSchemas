FROM imranq2/helix.spark:3.3.0.8-slim
# https://github.com/icanbwell/helix.spark
USER root

ENV PYTHONPATH=/sfs
ENV CLASSPATH=/sfs/jars:$CLASSPATH

COPY Pipfile* /sfs/
WORKDIR /sfs

RUN df -h # for space monitoring
RUN pip install pipenv && pipenv sync --dev --system


# override entrypoint to remove extra logging
RUN mv /opt/minimal_entrypoint.sh /opt/entrypoint.sh

COPY . /sfs

RUN df -h # for space monitoring
RUN mkdir -p /fhir && chmod 777 /fhir
RUN mkdir -p /.local/share/virtualenvs && chmod 777 /.local/share/virtualenvs
# USER 1001
