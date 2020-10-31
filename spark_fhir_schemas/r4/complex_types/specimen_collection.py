from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Specimen_Collection:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A sample to be used for analysis.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        collector: Person who collected the specimen.

        collectedDateTime: Time when specimen was collected from subject - the physiologically relevant
            time.

        collectedPeriod: Time when specimen was collected from subject - the physiologically relevant
            time.

        duration: The span of time over which the collection of a specimen occurred.

        quantity: The quantity of specimen collected; for instance the volume of a blood sample,
            or the physical measurement of an anatomic pathology sample.

        method: A coded value specifying the technique that is used to perform the procedure.

        bodySite: Anatomical location from which the specimen was collected (if subject is a
            patient). This is the target site.  This element is not used for environmental
            specimens.

        fastingStatusCodeableConcept: Abstinence or reduction from some or all food, drink, or both, for a period of
            time prior to sample collection.

        fastingStatusDuration: Abstinence or reduction from some or all food, drink, or both, for a period of
            time prior to sample collection.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Person who collected the specimen.
                StructField(
                    "collector", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Time when specimen was collected from subject - the physiologically relevant
                # time.
                StructField("collectedDateTime", StringType(), True),
                # Time when specimen was collected from subject - the physiologically relevant
                # time.
                StructField(
                    "collectedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The span of time over which the collection of a specimen occurred.
                StructField(
                    "duration", Duration.get_schema(recursion_depth + 1), True
                ),
                # The quantity of specimen collected; for instance the volume of a blood sample,
                # or the physical measurement of an anatomic pathology sample.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # A coded value specifying the technique that is used to perform the procedure.
                StructField(
                    "method", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Anatomical location from which the specimen was collected (if subject is a
                # patient). This is the target site.  This element is not used for environmental
                # specimens.
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Abstinence or reduction from some or all food, drink, or both, for a period of
                # time prior to sample collection.
                StructField(
                    "fastingStatusCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Abstinence or reduction from some or all food, drink, or both, for a period of
                # time prior to sample collection.
                StructField(
                    "fastingStatusDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
