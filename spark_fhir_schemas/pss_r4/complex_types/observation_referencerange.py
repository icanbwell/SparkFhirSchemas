from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchObservation_ReferenceRange(AutoMapperDataTypeComplexBase):
    """
    Measurements and simple assertions made about a patient, device or other
    subject.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        low: Optional[Any] = None,
        high: Optional[Any] = None,
        type_: Optional[Any] = None,
        appliesTo: Optional[Any] = None,
        age: Optional[Any] = None,
        text: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            low=low,
            high=high,
            type_=type_,
            appliesTo=appliesTo,
            age=age,
            text=text,
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
        Measurements and simple assertions made about a patient, device or other
        subject.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        low: The value of the low bound of the reference range.  The low bound of the
            reference range endpoint is inclusive of the value (e.g.  reference range is
            >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless
            (e.g. reference range is <=2.3).

        high: The value of the high bound of the reference range.  The high bound of the
            reference range endpoint is inclusive of the value (e.g.  reference range is
            >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless
            (e.g. reference range is >= 2.3).

        type: Codes to indicate the what part of the targeted reference population it
            applies to. For example, the normal or therapeutic range.

        appliesTo: Codes to indicate the target population this reference range applies to.  For
            example, a reference range may be based on the normal population or a
            particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of
            the target populations.  For example, to represent a target population of
            African American females, both a code of female and a code for African
            American would be used.

        age: The age at which this reference range is applicable. This is a neonatal age
            (e.g. number of weeks at term) if the meaning says so.

        text: Text based reference range in an observation which may be used when a
            quantitative range is not appropriate for an observation.  An example would be
            a reference value of "Negative" or a list or table of "normals".

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Observation_ReferenceRange") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Observation_ReferenceRange"]
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
                # The value of the low bound of the reference range.  The low bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is <=2.3).
                StructField(
                    "low",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the high bound of the reference range.  The high bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is >= 2.3).
                StructField(
                    "high",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Codes to indicate the what part of the targeted reference population it
                # applies to. For example, the normal or therapeutic range.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Codes to indicate the target population this reference range applies to.  For
                # example, a reference range may be based on the normal population or a
                # particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of
                # the target populations.  For example, to represent a target population of
                # African American females, both a code of female and a code for African
                # American would be used.
                StructField(
                    "appliesTo",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The age at which this reference range is applicable. This is a neonatal age
                # (e.g. number of weeks at term) if the meaning says so.
                StructField(
                    "age",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Text based reference range in an observation which may be used when a
                # quantitative range is not appropriate for an observation.  An example would be
                # a reference value of "Negative" or a list or table of "normals".
                StructField("text", StringType(), True),
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