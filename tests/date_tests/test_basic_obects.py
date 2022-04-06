import datetime
from os import path
from pathlib import Path
from shutil import rmtree
from typing import Union

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType, DataType, DateType, TimestampType
from spark_fhir_schemas.r4.resources.encounter import EncounterSchema

from tests.spark_json_helpers import create_jsonl_files

from spark_fhir_schemas.r4.complex_types.period import PeriodSchema


def test_can_set_period_start_end_to_date(spark_session: SparkSession) -> None:
    encounter_schema: Union[StructType, DataType] = EncounterSchema.get_schema(
        use_date_for=["encounter.period.start", "encounter.period.end"]
    )
    assert isinstance(
        encounter_schema["period"].dataType["start"].dataType, type(DateType())  # type: ignore
    )
    assert isinstance(
        encounter_schema["period"].dataType["end"].dataType, type(DateType())  # type: ignore
    )


def test_can_set_period_start_end_to_timestamp(spark_session: SparkSession) -> None:
    encounter_schema: Union[StructType, DataType] = EncounterSchema.get_schema()
    assert isinstance(
        encounter_schema["period"].dataType["start"].dataType, type(TimestampType())  # type: ignore
    )
    assert isinstance(
        encounter_schema["period"].dataType["end"].dataType, type(TimestampType())  # type: ignore
    )


def test_can_read_period_with_date(spark_session: SparkSession) -> None:
    data_dir: Path = Path(__file__).parent.joinpath("./")

    temp_folder = data_dir.joinpath("./temp")
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    period_test_folder: Path = data_dir.joinpath("test_files").joinpath("period.json")

    minified_json_path: Path = create_jsonl_files(
        src_file=period_test_folder,
        dst_folder=temp_folder.joinpath("minified_period"),
        dst_file_name="1.json",
    )

    schema = StructType([])

    df: DataFrame = spark_session.createDataFrame(
        spark_session.sparkContext.emptyRDD(), schema
    )

    period_schema: Union[StructType, DataType] = PeriodSchema.get_schema(
        use_date_for=["period.start", "period.end"]
    )
    print(period_schema)
    assert isinstance(period_schema, StructType)
    result_df: DataFrame = df.sql_ctx.read.schema(period_schema).json(
        str(minified_json_path)
    )
    assert result_df.collect()[0][2] == datetime.date(2022, 2, 1)
    assert result_df.collect()[0][3] == datetime.date(2022, 2, 3)


def test_can_read_period_with_datetime(spark_session: SparkSession) -> None:
    data_dir: Path = Path(__file__).parent.joinpath("./")

    temp_folder = data_dir.joinpath("./temp")
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    period_test_folder: Path = data_dir.joinpath("test_files").joinpath("period.json")

    minified_json_path: Path = create_jsonl_files(
        src_file=period_test_folder,
        dst_folder=temp_folder.joinpath("minified_period"),
        dst_file_name="1.json",
    )

    schema = StructType([])

    df: DataFrame = spark_session.createDataFrame(
        spark_session.sparkContext.emptyRDD(), schema
    )

    period_schema: Union[StructType, DataType] = PeriodSchema.get_schema()
    assert isinstance(period_schema, StructType)
    result_df: DataFrame = df.sql_ctx.read.schema(period_schema).json(
        str(minified_json_path)
    )
    assert result_df.collect()[0][2] == datetime.datetime(2022, 2, 1)
    assert result_df.collect()[0][3] == datetime.datetime(2022, 2, 3)


def test_can_read_period_with_datetime_populated(spark_session: SparkSession) -> None:
    data_dir: Path = Path(__file__).parent.joinpath("./")

    temp_folder = data_dir.joinpath("./temp")
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    period_test_folder: Path = data_dir.joinpath("test_files").joinpath(
        "period_datetime.json"
    )

    minified_json_path: Path = create_jsonl_files(
        src_file=period_test_folder,
        dst_folder=temp_folder.joinpath("minified_period"),
        dst_file_name="1.json",
    )

    schema = StructType([])

    df: DataFrame = spark_session.createDataFrame(
        spark_session.sparkContext.emptyRDD(), schema
    )

    period_schema: Union[StructType, DataType] = PeriodSchema.get_schema()
    assert isinstance(period_schema, StructType)
    result_df: DataFrame = df.sql_ctx.read.schema(period_schema).json(
        str(minified_json_path)
    )
    assert result_df.collect()[0][2] == datetime.datetime(2022, 1, 18, 14, 54, 57)
    assert result_df.collect()[0][3] == datetime.datetime(2022, 1, 18, 15, 54, 57)
