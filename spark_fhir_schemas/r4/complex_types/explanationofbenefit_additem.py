from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ExplanationOfBenefit_AddItem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_adjudication import ExplanationOfBenefit_Adjudication
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_detail1 import ExplanationOfBenefit_Detail1
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
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "itemSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "detailSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "subDetailSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "provider",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "productOrService",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "modifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "programCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("servicedDate", StringType(), True),
                StructField(
                    "servicedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "locationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "locationAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "locationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "unitPrice", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "net", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subSite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "noteNumber",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "adjudication",
                    ArrayType(
                        ExplanationOfBenefit_Adjudication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "detail",
                    ArrayType(
                        ExplanationOfBenefit_Detail1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
