from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.complex_types.plandefinition_target import PlanDefinition_Target


class PlanDefinition_Goal:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("description", CodeableConcept.get_schema(), True),
                StructField("priority", CodeableConcept.get_schema(), True),
                StructField("start", CodeableConcept.get_schema(), True),
                StructField("addresses",ArrayType(CodeableConcept.get_schema()), True),
                StructField("documentation",ArrayType(RelatedArtifact.get_schema()), True),
                StructField("target",ArrayType(PlanDefinition_Target.get_schema()), True),
            ]
        )

        return schema
