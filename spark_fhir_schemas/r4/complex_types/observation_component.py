from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.sampleddata import SampledData
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.observation_referencerange import Observation_ReferenceRange


class Observation_Component:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("valueQuantity", Quantity.get_schema(), True),
                StructField("valueCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("valueString", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueRange", Range.get_schema(), True),
                StructField("valueRatio", Ratio.get_schema(), True),
                StructField("valueSampledData", SampledData.get_schema(), True),
                StructField("valueTime", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valuePeriod", Period.get_schema(), True),
                StructField("dataAbsentReason", CodeableConcept.get_schema(), True),
                StructField("interpretation",ArrayType(CodeableConcept.get_schema()), True),
                StructField("referenceRange",ArrayType(Observation_ReferenceRange.get_schema()), True),
            ]
        )

        return schema
