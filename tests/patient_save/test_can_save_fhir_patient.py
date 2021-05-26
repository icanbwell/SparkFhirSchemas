from glob import glob
from os import path
from pathlib import Path
from shutil import rmtree
from typing import Union

from pyspark.sql import SparkSession
from pyspark.sql.types import DataType
from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.patient import PatientSchema


def test_can_save_fhir_patient(spark_session: SparkSession) -> None:
    # Arrange
    data_dir: Path = Path(__file__).parent.joinpath("./")

    temp_folder = data_dir.joinpath("./temp")
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    export_path: str = str(temp_folder.joinpath("patient_export.json"))

    patient_schema: Union[StructType, DataType] = PatientSchema.get_schema()
    assert isinstance(patient_schema, StructType)
    df = (
        spark_session.read.option("multiLine", True)
        .schema(patient_schema)
        .json(str(data_dir.joinpath("test.json")))
    )
    # df = spark_session.createDataFrame(data2)

    # Act
    df.coalesce(1).write.json(path=export_path)

    # Assert
    df.printSchema()
    df.show(truncate=False)

    assert df.select("resourceType").collect()[0][0] == "Patient"

    assert glob(str(temp_folder.joinpath("patient_export.json/*.json")))
