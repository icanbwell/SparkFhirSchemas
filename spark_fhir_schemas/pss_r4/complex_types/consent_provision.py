from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchConsent_Provision(AutoMapperDataTypeComplexBase):
    """
    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        period: Optional[Any] = None,
        actor: Optional[Any] = None,
        action: Optional[Any] = None,
        securityLabel: Optional[Any] = None,
        purpose: Optional[Any] = None,
        class_: Optional[Any] = None,
        code: Optional[Any] = None,
        dataPeriod: Optional[Any] = None,
        data: Optional[Any] = None,
        provision: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            period=period,
            actor=actor,
            action=action,
            securityLabel=securityLabel,
            purpose=purpose,
            class_=class_,
            code=code,
            dataPeriod=dataPeriod,
            data=data,
            provision=provision,
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
        A record of a healthcare consumer’s  choices, which permits or denies
        identified recipient(s) or recipient role(s) to perform one or more actions
        within a given policy context, for specific purposes and periods of time.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: Action  to take - permit or deny - when the rule conditions are met.  Not
            permitted in root rule, required in all nested rules.

        period: The timeframe in this rule is valid.

        actor: Who or what is controlled by this rule. Use group to identify a set of actors
            by some property they share (e.g. 'admitting officers').

        action: Actions controlled by this Rule.

        securityLabel: A security label, comprised of 0..* security label fields (Privacy tags),
            which define which resources are controlled by this exception.

        purpose: The context of the activities a user is taking - why the user is accessing the
            data - that are controlled by this rule.

        class: The class of information covered by this rule. The type can be a FHIR resource
            type, a profile on a type, or a CDA document, or some other type that
            indicates what sort of information the consent relates to.

        code: If this code is found in an instance, then the rule applies.

        dataPeriod: Clinical or Operational Relevant period of time that bounds the data
            controlled by this rule.

        data: The resources controlled by this rule if specific resources are referenced.

        provision: Rules which provide exceptions to the base rule or subrules.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.consent_actor import (
            AutoMapperElasticSearchConsent_Actor as Consent_ActorSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.consent_data import (
            AutoMapperElasticSearchConsent_Data as Consent_DataSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Consent_Provision") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Consent_Provision"]
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
                # Action  to take - permit or deny - when the rule conditions are met.  Not
                # permitted in root rule, required in all nested rules.
                StructField("type", StringType(), True),
                # The timeframe in this rule is valid.
                StructField(
                    "period",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Who or what is controlled by this rule. Use group to identify a set of actors
                # by some property they share (e.g. 'admitting officers').
                StructField(
                    "actor",
                    ArrayType(
                        Consent_ActorSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Actions controlled by this Rule.
                StructField(
                    "action",
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
                # A security label, comprised of 0..* security label fields (Privacy tags),
                # which define which resources are controlled by this exception.
                StructField(
                    "securityLabel",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The context of the activities a user is taking - why the user is accessing the
                # data - that are controlled by this rule.
                StructField(
                    "purpose",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The class of information covered by this rule. The type can be a FHIR resource
                # type, a profile on a type, or a CDA document, or some other type that
                # indicates what sort of information the consent relates to.
                StructField(
                    "class",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # If this code is found in an instance, then the rule applies.
                StructField(
                    "code",
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
                # Clinical or Operational Relevant period of time that bounds the data
                # controlled by this rule.
                StructField(
                    "dataPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The resources controlled by this rule if specific resources are referenced.
                StructField(
                    "data",
                    ArrayType(
                        Consent_DataSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Rules which provide exceptions to the base rule or subrules.
                StructField(
                    "provision",
                    ArrayType(
                        Consent_ProvisionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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
