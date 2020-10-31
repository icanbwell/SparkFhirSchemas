from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Measure_SupplementalData:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The Measure resource provides the definition of a quality measure.


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

        code: Indicates a meaning for the supplemental data. This can be as simple as a
            unique identifier, or it can establish meaning in a broader context by drawing
            from a terminology, allowing supplemental data to be correlated across
            measures.

        usage: An indicator of the intended usage for the supplemental data element.
            Supplemental data indicates the data is additional information requested to
            augment the measure information. Risk adjustment factor indicates the data is
            additional information used to calculate risk adjustment factors when applying
            a risk model to the measure calculation.

        description: The human readable description of this supplemental data.

        criteria: The criteria for the supplemental data. This is typically the name of a valid
            expression defined within a referenced library, but it may also be a path to a
            specific data element. The criteria defines the data to be returned for this
            element.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.expression import Expression
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
                # Indicates a meaning for the supplemental data. This can be as simple as a
                # unique identifier, or it can establish meaning in a broader context by drawing
                # from a terminology, allowing supplemental data to be correlated across
                # measures.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # An indicator of the intended usage for the supplemental data element.
                # Supplemental data indicates the data is additional information requested to
                # augment the measure information. Risk adjustment factor indicates the data is
                # additional information used to calculate risk adjustment factors when applying
                # a risk model to the measure calculation.
                StructField(
                    "usage",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The human readable description of this supplemental data.
                StructField("description", StringType(), True),
                # The criteria for the supplemental data. This is typically the name of a valid
                # expression defined within a referenced library, but it may also be a path to a
                # specific data element. The criteria defines the data to be returned for this
                # element.
                StructField(
                    "criteria", Expression.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
