from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.integer import integer


class MolecularSequence_ReferenceSeq:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("chromosome", CodeableConcept.get_schema(), True),
                StructField("genomeBuild", StringType(), True),
                StructField("orientation", StringType(), True),
                StructField("referenceSeqId", CodeableConcept.get_schema(), True),
                StructField("referenceSeqPointer", Reference.get_schema(), True),
                StructField("referenceSeqString", StringType(), True),
                StructField("strand", StringType(), True),
                StructField("windowStart", integer.get_schema(), True),
                StructField("windowEnd", integer.get_schema(), True),
            ]
        )

        return schema
