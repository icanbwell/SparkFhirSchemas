from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.specimendefinition_container import SpecimenDefinition_Container
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.specimendefinition_handling import SpecimenDefinition_Handling


class SpecimenDefinition_TypeTested:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("isDerived", BooleanType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("preference", StringType(), True),
                StructField("container", SpecimenDefinition_Container.get_schema(), True),
                StructField("requirement", StringType(), True),
                StructField("retentionTime", Duration.get_schema(), True),
                StructField("rejectionCriterion",ArrayType(CodeableConcept.get_schema()), True),
                StructField("handling",ArrayType(SpecimenDefinition_Handling.get_schema()), True),]
        )

        return schema
