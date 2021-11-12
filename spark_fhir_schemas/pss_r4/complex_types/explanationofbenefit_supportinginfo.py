from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchExplanationOfBenefit_SupportingInfo(
    AutoMapperDataTypeComplexBase
):
    """
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        sequence: Optional[Any] = None,
        category: Optional[Any] = None,
        code: Optional[Any] = None,
        timingDate: Optional[Any] = None,
        timingPeriod: Optional[Any] = None,
        valueBoolean: Optional[Any] = None,
        valueString: Optional[Any] = None,
        valueQuantity: Optional[Any] = None,
        valueAttachment: Optional[Any] = None,
        valueReference: Optional[Any] = None,
        reason: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            category=category,
            code=code,
            timingDate=timingDate,
            timingPeriod=timingPeriod,
            valueBoolean=valueBoolean,
            valueString=valueString,
            valueQuantity=valueQuantity,
            valueAttachment=valueAttachment,
            valueReference=valueReference,
            reason=reason,
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
        This resource provides: the claim details; adjudication details from the
        processing of a Claim; and optionally account balance information, for
        informing the subscriber of the benefits provided.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        sequence: A number to uniquely identify supporting information entries.

        category: The general class of the information supplied: information; exception;
            accident, employment; onset, etc.

        code: System and code pertaining to the specific information regarding special
            conditions relating to the setting, treatment or patient  for which care is
            sought.

        timingDate: The date when or period to which this information refers.

        timingPeriod: The date when or period to which this information refers.

        valueBoolean: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueString: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueQuantity: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueAttachment: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueReference: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        reason: Provides the reason in the situation where a reason code is required in
            addition to the content.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.positiveint import (
            AutoMapperElasticSearchpositiveInt as positiveIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ExplanationOfBenefit_SupportingInfo")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ExplanationOfBenefit_SupportingInfo"
        ]
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
                # A number to uniquely identify supporting information entries.
                StructField(
                    "sequence",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The general class of the information supplied: information; exception;
                # accident, employment; onset, etc.
                StructField(
                    "category",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # System and code pertaining to the specific information regarding special
                # conditions relating to the setting, treatment or patient  for which care is
                # sought.
                StructField(
                    "code",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date when or period to which this information refers.
                StructField("timingDate", DateType(), True),
                # The date when or period to which this information refers.
                StructField(
                    "timingPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField("valueBoolean", BooleanType(), True),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField("valueString", StringType(), True),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Provides the reason in the situation where a reason code is required in
                # addition to the content.
                StructField(
                    "reason",
                    CodingSchema.schema(
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
