from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet_Compose:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).


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

        lockedDate: The Locked Date is  the effective date that is used to determine the version
            of all referenced Code Systems and Value Set Definitions included in the
            compose that are not already tied to a specific version.

        inactive: Whether inactive codes - codes that are not approved for current use - are in
            the value set. If inactive = true, inactive codes are to be included in the
            expansion, if inactive = false, the inactive codes will not be included in the
            expansion. If absent, the behavior is determined by the implementation, or by
            the applicable $expand parameters (but generally, inactive codes would be
            expected to be included).

        include: Include one or more codes from a code system or other value set(s).

        exclude: Exclude one or more codes from the value set based on code system filters
            and/or other value sets.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.valueset_include import ValueSet_Include
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
                # The Locked Date is  the effective date that is used to determine the version
                # of all referenced Code Systems and Value Set Definitions included in the
                # compose that are not already tied to a specific version.
                StructField("lockedDate", DateType(), True),
                # Whether inactive codes - codes that are not approved for current use - are in
                # the value set. If inactive = true, inactive codes are to be included in the
                # expansion, if inactive = false, the inactive codes will not be included in the
                # expansion. If absent, the behavior is determined by the implementation, or by
                # the applicable $expand parameters (but generally, inactive codes would be
                # expected to be included).
                StructField("inactive", BooleanType(), True),
                # Include one or more codes from a code system or other value set(s).
                StructField(
                    "include",
                    ArrayType(
                        ValueSet_Include.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Exclude one or more codes from the value set based on code system filters
                # and/or other value sets.
                StructField(
                    "exclude",
                    ArrayType(
                        ValueSet_Include.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
