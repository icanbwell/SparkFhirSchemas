from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.contract_subject import Contract_Subject
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt


class Contract_Action:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("doNotPerform", BooleanType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subject",ArrayType(Contract_Subject.get_schema()), True),
                StructField("intent", CodeableConcept.get_schema(), True),
                StructField("linkId",ArrayType(string.get_schema()), True),
                StructField("status", CodeableConcept.get_schema(), True),
                StructField("context", Reference.get_schema(), True),
                StructField("contextLinkId",ArrayType(string.get_schema()), True),
                StructField("occurrenceDateTime", StringType(), True),
                StructField("occurrencePeriod", Period.get_schema(), True),
                StructField("occurrenceTiming", Timing.get_schema(), True),
                StructField("requester",ArrayType(Reference.get_schema()), True),
                StructField("requesterLinkId",ArrayType(string.get_schema()), True),
                StructField("performerType",ArrayType(CodeableConcept.get_schema()), True),
                StructField("performerRole", CodeableConcept.get_schema(), True),
                StructField("performer", Reference.get_schema(), True),
                StructField("performerLinkId",ArrayType(string.get_schema()), True),
                StructField("reasonCode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("reasonReference",ArrayType(Reference.get_schema()), True),
                StructField("reason",ArrayType(string.get_schema()), True),
                StructField("reasonLinkId",ArrayType(string.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("securityLabelNumber",ArrayType(unsignedInt.get_schema()), True),
            ]
        )

        return schema
