from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationKnowledge_Regulatory:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Information about a medication that is used to support knowledge.


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

        regulatoryAuthority: The authority that is specifying the regulations.

        substitution: Specifies if changes are allowed when dispensing a medication from a
            regulatory perspective.

        schedule: Specifies the schedule of a medication in jurisdiction.

        maxDispense: The maximum number of units of the medication that can be dispensed in a
            period.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_substitution import MedicationKnowledge_Substitution
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_schedule import MedicationKnowledge_Schedule
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_maxdispense import MedicationKnowledge_MaxDispense
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
                # The authority that is specifying the regulations.
                StructField(
                    "regulatoryAuthority",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Specifies if changes are allowed when dispensing a medication from a
                # regulatory perspective.
                StructField(
                    "substitution",
                    ArrayType(
                        MedicationKnowledge_Substitution.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Specifies the schedule of a medication in jurisdiction.
                StructField(
                    "schedule",
                    ArrayType(
                        MedicationKnowledge_Schedule.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The maximum number of units of the medication that can be dispensed in a
                # period.
                StructField(
                    "maxDispense",
                    MedicationKnowledge_MaxDispense.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
