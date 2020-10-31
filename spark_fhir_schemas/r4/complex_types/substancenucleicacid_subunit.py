from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substancenucleicacid_linkage import SubstanceNucleicAcid_Linkage
from spark_fhir_schemas.r4.complex_types.substancenucleicacid_sugar import SubstanceNucleicAcid_Sugar


# noinspection PyPep8Naming
class SubstanceNucleicAcid_Subunit:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("subunit", integer.get_schema(), True),
                StructField("sequence", StringType(), True),
                StructField("length", integer.get_schema(), True),
                StructField(
                    "sequenceAttachment", Attachment.get_schema(), True
                ),
                StructField("fivePrime", CodeableConcept.get_schema(), True),
                StructField("threePrime", CodeableConcept.get_schema(), True),
                StructField(
                    "linkage",
                    ArrayType(SubstanceNucleicAcid_Linkage.get_schema()), True
                ),
                StructField(
                    "sugar",
                    ArrayType(SubstanceNucleicAcid_Sugar.get_schema()), True
                ),
            ]
        )

        return schema
