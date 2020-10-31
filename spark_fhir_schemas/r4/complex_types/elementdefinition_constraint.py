from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ElementDefinition_Constraint:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Captures constraints on each element within the resource, profile, or
        extension.


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

        key: Allows identification of which elements have their cardinalities impacted by
            the constraint.  Will not be referenced for constraints that do not affect
            cardinality.

        requirements: Description of why this constraint is necessary or appropriate.

        severity: Identifies the impact constraint violation has on the conformance of the
            instance.

        human: Text that can be used to describe the constraint in messages identifying that
            the constraint has been violated.

        expression: A [FHIRPath](fhirpath.html) expression of constraint that can be executed to
            see if this constraint is met.

        xpath: An XPath expression of constraint that can be executed to see if this
            constraint is met.

        source: A reference to the original source of the constraint, for traceability
            purposes.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
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
                # Allows identification of which elements have their cardinalities impacted by
                # the constraint.  Will not be referenced for constraints that do not affect
                # cardinality.
                StructField("key", id.get_schema(recursion_depth + 1), True),
                # Description of why this constraint is necessary or appropriate.
                StructField("requirements", StringType(), True),
                # Identifies the impact constraint violation has on the conformance of the
                # instance.
                StructField("severity", StringType(), True),
                # Text that can be used to describe the constraint in messages identifying that
                # the constraint has been violated.
                StructField("human", StringType(), True),
                # A [FHIRPath](fhirpath.html) expression of constraint that can be executed to
                # see if this constraint is met.
                StructField("expression", StringType(), True),
                # An XPath expression of constraint that can be executed to see if this
                # constraint is met.
                StructField("xpath", StringType(), True),
                # A reference to the original source of the constraint, for traceability
                # purposes.
                StructField(
                    "source", canonical.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
