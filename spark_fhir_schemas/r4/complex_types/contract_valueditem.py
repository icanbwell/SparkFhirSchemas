from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt


class Contract_ValuedItem:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("entityCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("entityReference", Reference.get_schema(), True),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("effectiveTime", dateTime.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("unitPrice", Money.get_schema(), True),
                StructField("factor", decimal.get_schema(), True),
                StructField("points", decimal.get_schema(), True),
                StructField("net", Money.get_schema(), True),
                StructField("payment", StringType(), True),
                StructField("paymentDate", dateTime.get_schema(), True),
                StructField("responsible", Reference.get_schema(), True),
                StructField("recipient", Reference.get_schema(), True),
                StructField("linkId",ArrayType(string.get_schema()), True),
                StructField("securityLabelNumber",ArrayType(unsignedInt.get_schema()), True),
            ]
        )

        return schema
