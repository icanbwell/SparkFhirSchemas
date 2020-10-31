from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class VerificationResult_PrimarySource:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes validation requirements, source(s), status and dates for one or more
        elements.


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

        who: Reference to the primary source.

        type: Type of primary source (License Board; Primary Education; Continuing
            Education; Postal Service; Relationship owner; Registration Authority; legal
            source; issuing source; authoritative source).

        communicationMethod: Method for communicating with the primary source (manual; API; Push).

        validationStatus: Status of the validation of the target against the primary source (successful;
            failed; unknown).

        validationDate: When the target was validated against the primary source.

        canPushUpdates: Ability of the primary source to push updates/alerts (yes; no; undetermined).

        pushTypeAvailable: Type of alerts/updates the primary source can send (specific requested
            changes; any changes; as defined by source).

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
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
                # Reference to the primary source.
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                # Type of primary source (License Board; Primary Education; Continuing
                # Education; Postal Service; Relationship owner; Registration Authority; legal
                # source; issuing source; authoritative source).
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Method for communicating with the primary source (manual; API; Push).
                StructField(
                    "communicationMethod",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Status of the validation of the target against the primary source (successful;
                # failed; unknown).
                StructField(
                    "validationStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # When the target was validated against the primary source.
                StructField(
                    "validationDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Ability of the primary source to push updates/alerts (yes; no; undetermined).
                StructField(
                    "canPushUpdates",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Type of alerts/updates the primary source can send (specific requested
                # changes; any changes; as defined by source).
                StructField(
                    "pushTypeAvailable",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
