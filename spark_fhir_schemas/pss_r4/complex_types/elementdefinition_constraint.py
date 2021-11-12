from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchElementDefinition_Constraint(
    AutoMapperDataTypeComplexBase
):
    """
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        key: Optional[Any] = None,
        requirements: Optional[Any] = None,
        severity: Optional[Any] = None,
        human: Optional[Any] = None,
        expression: Optional[Any] = None,
        xpath: Optional[Any] = None,
        source: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            key=key,
            requirements=requirements,
            severity=severity,
            human=human,
            expression=expression,
            xpath=xpath,
            source=source,
        )
        super().include_null_properties(include_null_properties=True)

    @staticmethod
    def schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition_Constraint")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ElementDefinition_Constraint"]
        schema = StructType(
            [
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
                    ArrayType(
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Allows identification of which elements have their cardinalities impacted by
                # the constraint.  Will not be referenced for constraints that do not affect
                # cardinality.
                StructField(
                    "key",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
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
                    "source",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
