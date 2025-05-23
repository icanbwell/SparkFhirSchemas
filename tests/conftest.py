import logging
import os
from os import path
import shutil
from typing import Any

from pyspark.sql import SparkSession
import pytest

# make sure env variables are set correctly
if "SPARK_HOME" not in os.environ:
    os.environ["SPARK_HOME"] = "/usr/local/opt/spark"


def quiet_py4j() -> None:
    """turn down spark logging for the test context"""
    logger = logging.getLogger("py4j")
    logger.setLevel(logging.ERROR)


def clean_spark_dir() -> None:
    """

    :return:
    """
    try:
        os.remove("./derby.log")
        shutil.rmtree("./metastore_db")
        shutil.rmtree("./spark-warehouse")
    except OSError:
        pass


def clean_spark_session(session: SparkSession) -> None:
    """

    :param session:
    :return:
    """
    tables = session.catalog.listTables("default")

    for table in tables:
        print(f"clear_tables() is dropping table/view: {table.name}")
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        session.sql(f"DROP TABLE IF EXISTS default.{table.name}")
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        session.sql(f"DROP VIEW IF EXISTS default.{table.name}")
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        session.sql(f"DROP VIEW IF EXISTS {table.name}")

    session.catalog.clearCache()


def clean_close(session: SparkSession) -> None:
    """

    :param session:
    :return:
    """
    clean_spark_session(session)
    clean_spark_dir()
    session.stop()


@pytest.fixture(scope="session")
def spark_session(request: Any) -> SparkSession:
    # make sure env variables are set correctly
    if "SPARK_HOME" not in os.environ:
        os.environ["SPARK_HOME"] = "/usr/local/opt/spark"

    clean_spark_dir()

    master: str = "spark://spark:7077"
    master = "local[2]"
    if not path.exists("/Applications/Docker.app"):
        master = "local[2]"
        print(f"++++++ Running on local spark: {master} ++++")
    else:
        print(f"++++++ Running on docker spark: {master} ++++")

    session = (
        SparkSession.builder.appName("pytest-pyspark-local-testing")
        .master(master)
        .config("spark.ui.showConsoleProgress", "false")
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.default.parallelism", "4")
        .config("spark.sql.broadcastTimeout", "2400")
        .enableHiveSupport()
        .getOrCreate()
    )

    request.addfinalizer(lambda: clean_close(session))
    quiet_py4j()
    return session


@pytest.fixture(scope="function")
def spark_session_per_function(request: Any) -> SparkSession:
    # make sure env variables are set correctly
    if "SPARK_HOME" not in os.environ:
        os.environ["SPARK_HOME"] = "/usr/local/opt/spark"

    clean_spark_dir()

    master: str = "spark://spark:7077"
    master = "local[2]"
    if not path.exists("/Applications/Docker.app"):
        master = "local[2]"
        print(f"++++++ Running on local spark: {master} ++++")
    else:
        print(f"++++++ Running on docker spark: {master} ++++")

    session = (
        SparkSession.builder.appName("pytest-pyspark-local-testing")
        .master(master)
        .config("spark.ui.showConsoleProgress", "false")
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.default.parallelism", "4")
        .config("spark.sql.broadcastTimeout", "2400")
        .enableHiveSupport()
        .getOrCreate()
    )

    request.addfinalizer(lambda: clean_close(session))
    quiet_py4j()
    return session
