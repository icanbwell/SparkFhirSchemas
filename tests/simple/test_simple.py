import os
from os import path
from pathlib import Path
from shutil import rmtree
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.complex_types.address import AddressSchema
from spark_fhir_schemas.r4.resources.explanationofbenefit import ExplanationOfBenefitSchema
from spark_fhir_schemas.r4.resources.patient import PatientSchema


def test_simple() -> None:
    data_dir: Path = Path(__file__).parent.joinpath('./')
    temp_folder = data_dir.joinpath('./temp')
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    os.mkdir(temp_folder)

    schema: Union[StructType, DataType] = PatientSchema.get_schema()
    assert isinstance(schema, StructType)

    # print(schema)
    print("------- Patient --------")
    print(schema.json())

    with open(temp_folder.joinpath("patient_schema.json"), "w+") as file:
        file.write(schema.json())

    print("------- Address --------")
    schema = AddressSchema.get_schema()
    print(schema.json())
    with open(temp_folder.joinpath("address_schema.json"), "w+") as file:
        file.write(schema.json())

    print("------- ExplanationOfBenefitSchema --------")
    schema = ExplanationOfBenefitSchema.get_schema()
    print(schema.json())
    # noinspection SpellCheckingInspection
    with open(
        temp_folder.joinpath("explanationofbenefit_schema.json"), "w"
    ) as file:
        file.write(schema.json())

    assert 1 == 1
