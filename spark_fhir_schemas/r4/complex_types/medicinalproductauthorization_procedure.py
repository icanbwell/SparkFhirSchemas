from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class MedicinalProductAuthorization_Procedure:
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
                StructField("identifier", Identifier.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("datePeriod", Period.get_schema(), True),
                StructField("dateDateTime", StringType(), True),
                StructField(
                    "application",
                    ArrayType(
                        MedicinalProductAuthorization_Procedure.get_schema()
                    ), True
                ),
            ]
        )

        return schema
