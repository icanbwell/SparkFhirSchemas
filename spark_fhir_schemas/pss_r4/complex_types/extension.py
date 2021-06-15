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
    IntegerType,
    DataType,
    FloatType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchExtension(AutoMapperDataTypeComplexBase):
    """
    Optional Extension Element - found in all resources.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        url: Optional[Any] = None,
        valueBoolean: Optional[Any] = None,
        valueCode: Optional[Any] = None,
        valueDate: Optional[Any] = None,
        valueDateTime: Optional[Any] = None,
        valueDecimal: Optional[Any] = None,
        valueId: Optional[Any] = None,
        valueInteger: Optional[Any] = None,
        valuePositiveInt: Optional[Any] = None,
        valueString: Optional[Any] = None,
        valueTime: Optional[Any] = None,
        valueUnsignedInt: Optional[Any] = None,
        valueUri: Optional[Any] = None,
        valueUrl: Optional[Any] = None,
        valueCodeableConcept: Optional[Any] = None,
        valueCoding: Optional[Any] = None,
        valueCount: Optional[Any] = None,
        valueIdentifier: Optional[Any] = None,
        valueMoney: Optional[Any] = None,
        valuePeriod: Optional[Any] = None,
        valueQuantity: Optional[Any] = None,
        valueRange: Optional[Any] = None,
        valueReference: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            url=url,
            valueBoolean=valueBoolean,
            valueCode=valueCode,
            valueDate=valueDate,
            valueDateTime=valueDateTime,
            valueDecimal=valueDecimal,
            valueId=valueId,
            valueInteger=valueInteger,
            valuePositiveInt=valuePositiveInt,
            valueString=valueString,
            valueTime=valueTime,
            valueUnsignedInt=valueUnsignedInt,
            valueUri=valueUri,
            valueUrl=valueUrl,
            valueCodeableConcept=valueCodeableConcept,
            valueCoding=valueCoding,
            valueCount=valueCount,
            valueIdentifier=valueIdentifier,
            valueMoney=valueMoney,
            valuePeriod=valuePeriod,
            valueQuantity=valueQuantity,
            valueRange=valueRange,
            valueReference=valueReference,
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
        Optional Extension Element - found in all resources.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        url: Source of the definition for the extension code - a logical name or a URL.

        valueBoolean: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCode: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDate: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDateTime: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDecimal: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueId: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueInteger: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valuePositiveInt: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueString: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueTime: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUnsignedInt: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUri: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUrl: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCoding: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCount: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueIdentifier: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueMoney: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valuePeriod: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueQuantity: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueRange: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueReference: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        """
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.count import (
            AutoMapperElasticSearchCount as CountSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.money import (
            AutoMapperElasticSearchMoney as MoneySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Extension") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Extension"]
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
                # Source of the definition for the extension code - a logical name or a URL.
                StructField(
                    "url",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueBoolean", BooleanType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueCode", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDate", DateType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDateTime", TimestampType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDecimal", FloatType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueId", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueInteger", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valuePositiveInt", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueString", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueTime", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUnsignedInt", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUri", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUrl", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCount",
                    CountSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueMoney",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valuePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
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
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
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
