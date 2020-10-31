from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.substancespecification_name import SubstanceSpecification_Name
from spark_fhir_schemas.r4.resources.substancespecification_name import SubstanceSpecification_Name
from spark_fhir_schemas.r4.resources.substancespecification_official import SubstanceSpecification_Official
from spark_fhir_schemas.r4.resources.reference import Reference


class SubstanceSpecification_Name:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("name", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("status", CodeableConcept.get_schema(), True),
                StructField("preferred", BooleanType(), True),
                StructField("language",ArrayType(CodeableConcept.get_schema()), True),
                StructField("domain",ArrayType(CodeableConcept.get_schema()), True),
                StructField("jurisdiction",ArrayType(CodeableConcept.get_schema()), True),
                StructField("synonym",ArrayType(SubstanceSpecification_Name.get_schema()), True),
                StructField("translation",ArrayType(SubstanceSpecification_Name.get_schema()), True),
                StructField("official",ArrayType(SubstanceSpecification_Official.get_schema()), True),
                StructField("source",ArrayType(Reference.get_schema()), True),]
        )

        return schema
