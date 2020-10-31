from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.attachment import Attachment
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.substancenucleicacid_linkage import SubstanceNucleicAcid_Linkage
from spark_fhir_schemas.r4.resources.substancenucleicacid_sugar import SubstanceNucleicAcid_Sugar


class SubstanceNucleicAcid_Subunit:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("subunit", integer.get_schema(), True),
                StructField("sequence", StringType(), True),
                StructField("length", integer.get_schema(), True),
                StructField("sequenceAttachment", Attachment.get_schema(), True),
                StructField("fivePrime", CodeableConcept.get_schema(), True),
                StructField("threePrime", CodeableConcept.get_schema(), True),
                StructField("linkage",ArrayType(SubstanceNucleicAcid_Linkage.get_schema()), True),
                StructField("sugar",ArrayType(SubstanceNucleicAcid_Sugar.get_schema()), True),]
        )

        return schema
