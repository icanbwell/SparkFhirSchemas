from os import path
from pathlib import Path
from shutil import rmtree
from typing import Union

from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import DataType
from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.patient import PatientSchema
from tests.spark_json_helpers import create_jsonl_files


def test_can_load_patient(spark_session: SparkSession) -> None:
    # Arrange
    data_dir: Path = Path(__file__).parent.joinpath("./")

    patient_test_folder: Path = data_dir.joinpath("test_files").joinpath("patient.json")

    temp_folder = data_dir.joinpath("./temp")
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    minified_json_path: Path = create_jsonl_files(
        src_file=patient_test_folder,
        dst_folder=temp_folder.joinpath("minified_patient"),
        dst_file_name="1.json",
    )

    schema = StructType([])

    df: DataFrame = spark_session.createDataFrame(
        spark_session.sparkContext.emptyRDD(), schema
    )

    patient_schema: Union[StructType, DataType] = PatientSchema.get_schema()
    assert isinstance(patient_schema, StructType)
    result_df: DataFrame = df.sql_ctx.read.schema(patient_schema).json(
        str(minified_json_path)
    )

    result_df.printSchema()
    result_df.show(truncate=False)
    result_df.createOrReplaceTempView("result_view")

    assert result_df.where("id == 27384972").select("gender").collect()[0][0] == "male"
    assert (
        spark_session.sql(
            "SELECT identifier[0].type.coding[0].code FROM result_view where id = '27384972'"
        ).collect()[0][0]
        == "2"
    )

    # now make sure we can persist it
