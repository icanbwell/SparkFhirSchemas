from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference


class MedicinalProduct_ManufacturingBusinessOperation:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("operationType", CodeableConcept.get_schema(), True),
                StructField("authorisationReferenceNumber", Identifier.get_schema(), True),
                StructField("effectiveDate", dateTime.get_schema(), True),
                StructField("confidentialityIndicator", CodeableConcept.get_schema(), True),
                StructField("manufacturer",ArrayType(Reference.get_schema()), True),
                StructField("regulator", Reference.get_schema(), True),]
        )

        return schema
