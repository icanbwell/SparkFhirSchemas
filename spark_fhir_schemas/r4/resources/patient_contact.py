from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.humanname import HumanName
from spark_fhir_schemas.r4.resources.contactpoint import ContactPoint
from spark_fhir_schemas.r4.resources.address import Address
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period


class Patient_Contact:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("relationship",ArrayType(CodeableConcept.get_schema()), True),
                StructField("name", HumanName.get_schema(), True),
                StructField("telecom",ArrayType(ContactPoint.get_schema()), True),
                StructField("address", Address.get_schema(), True),
                StructField("gender", StringType(), True),
                StructField("organization", Reference.get_schema(), True),
                StructField("period", Period.get_schema(), True),]
        )

        return schema
