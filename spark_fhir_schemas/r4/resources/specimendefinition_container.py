from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.specimendefinition_additive import SpecimenDefinition_Additive
from spark_fhir_schemas.r4.resources.string import string


class SpecimenDefinition_Container:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("material", CodeableConcept.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("cap", CodeableConcept.get_schema(), True),
                StructField("description", StringType(), True),
                StructField("capacity", Quantity.get_schema(), True),
                StructField("minimumVolumeQuantity", Quantity.get_schema(), True),
                StructField("minimumVolumeString", StringType(), True),
                StructField("additive",ArrayType(SpecimenDefinition_Additive.get_schema()), True),
                StructField("preparation", StringType(), True),]
        )

        return schema
