from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference


class SubstanceReferenceInformation_Target:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("target", Identifier.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("interaction", CodeableConcept.get_schema(), True),
                StructField("organism", CodeableConcept.get_schema(), True),
                StructField("organismType", CodeableConcept.get_schema(), True),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountRange", Range.get_schema(), True),
                StructField("amountString", StringType(), True),
                StructField("amountType", CodeableConcept.get_schema(), True),
                StructField("source",ArrayType(Reference.get_schema()), True),]
        )

        return schema
