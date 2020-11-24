from datetime import datetime
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
    data_dir: Path = Path(__file__).parent.joinpath('./')

    temp_folder = data_dir.joinpath('./temp')
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    export_path: str = str(temp_folder.joinpath("patient_export.json"))

    data2 = [
        {
            "active":
            True,
            "address": [
                {
                    "city": "DALLAS",
                    "country": "US",
                    "district": "DALLAS",
                    "line": ["1935 Medical District Drive"],
                    "postalCode": "75235",
                    "state": "TX",
                    "use": "home"
                }
            ],
            "name": [
                {
                    "family": "Informatics",
                    "given": ["ChildOne", "Test"],
                    "text": "ChildOne Test Informatics",
                    "use": "official"
                }, {
                    "family": "Informatics",
                    "given": ["ChildOne", "Test"],
                    "text": "ChildOne Test Informatics",
                    "use": "usual"
                }
            ],
            "birthDate":
            datetime.strptime("2008-01-01", "%Y-%m-%d"),
            "gender":
            "male",
            "id":
            "e2abVBgS5VtWv5Bckq0lQag3",
            "resourceType":
            "Patient"
        }
    ]
    patient_schema: Union[StructType, DataType] = PatientSchema.get_schema()
    df = spark_session.createDataFrame(data2, schema=patient_schema)
    # df = spark_session.createDataFrame(data2)

    # Act
    df.coalesce(1).write.json(path=export_path)

    # Assert
    df.printSchema()
    df.show(truncate=False)

    assert glob(str(temp_folder.joinpath("patient_export.json/*.json")))
