from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DataRequirement:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.datarequirement_codefilter import DataRequirement_CodeFilter
        from spark_fhir_schemas.r4.complex_types.datarequirement_datefilter import DataRequirement_DateFilter
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.datarequirement_sort import DataRequirement_Sort
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "type", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "profile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("mustSupport", ArrayType(StringType()), True),
                StructField(
                    "codeFilter",
                    ArrayType(
                        DataRequirement_CodeFilter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "dateFilter",
                    ArrayType(
                        DataRequirement_DateFilter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "limit", positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sort",
                    ArrayType(
                        DataRequirement_Sort.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
