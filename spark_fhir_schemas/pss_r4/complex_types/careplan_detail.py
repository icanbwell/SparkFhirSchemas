from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchCarePlan_Detail(AutoMapperDataTypeComplexBase):
    """
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        kind: Optional[Any] = None,
        instantiatesCanonical: Optional[Any] = None,
        instantiatesUri: Optional[Any] = None,
        code: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        goal: Optional[Any] = None,
        status: Optional[Any] = None,
        statusReason: Optional[Any] = None,
        doNotPerform: Optional[Any] = None,
        scheduledTiming: Optional[Any] = None,
        scheduledPeriod: Optional[Any] = None,
        scheduledString: Optional[Any] = None,
        location: Optional[Any] = None,
        performer: Optional[Any] = None,
        productCodeableConcept: Optional[Any] = None,
        productReference: Optional[Any] = None,
        dailyAmount: Optional[Any] = None,
        quantity: Optional[Any] = None,
        description: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            kind=kind,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            code=code,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            goal=goal,
            status=status,
            statusReason=statusReason,
            doNotPerform=doNotPerform,
            scheduledTiming=scheduledTiming,
            scheduledPeriod=scheduledPeriod,
            scheduledString=scheduledString,
            location=location,
            performer=performer,
            productCodeableConcept=productCodeableConcept,
            productReference=productReference,
            dailyAmount=dailyAmount,
            quantity=quantity,
            description=description,
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
        Describes the intention of how one or more practitioners intend to deliver
        care for a particular patient, group or community for a period of time,
        possibly limited to care for a specific condition or set of conditions.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        kind: A description of the kind of resource the in-line definition of a care plan
            activity is representing.  The CarePlan.activity.detail is an in-line
            definition when a resource is not referenced using
            CarePlan.activity.reference.  For example, a MedicationRequest, a
            ServiceRequest, or a CommunicationRequest.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other
            definition that is adhered to in whole or in part by this CarePlan activity.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline,
            questionnaire or other definition that is adhered to in whole or in part by
            this CarePlan activity.

        code: Detailed description of the type of planned activity; e.g. what lab test, what
            procedure, what kind of encounter.

        reasonCode: Provides the rationale that drove the inclusion of this particular activity as
            part of the plan or the reason why the activity was prohibited.

        reasonReference: Indicates another resource, such as the health condition(s), whose existence
            justifies this request and drove the inclusion of this particular activity as
            part of the plan.

        goal: Internal reference that identifies the goals that this activity is intended to
            contribute towards meeting.

        status: Identifies what progress is being made for the specific activity.

        statusReason: Provides reason why the activity isn't yet started, is on hold, was cancelled,
            etc.

        doNotPerform: If true, indicates that the described activity is one that must NOT be engaged
            in when following the plan.  If false, or missing, indicates that the
            described activity is one that should be engaged in when following the plan.

        scheduledTiming: The period, timing or frequency upon which the described activity is to occur.

        scheduledPeriod: The period, timing or frequency upon which the described activity is to occur.

        scheduledString: The period, timing or frequency upon which the described activity is to occur.

        location: Identifies the facility where the activity will occur; e.g. home, hospital,
            specific clinic, etc.

        performer: Identifies who's expected to be involved in the activity.

        productCodeableConcept: Identifies the food, drug or other product to be consumed or supplied in the
            activity.

        productReference: Identifies the food, drug or other product to be consumed or supplied in the
            activity.

        dailyAmount: Identifies the quantity expected to be consumed in a given day.

        quantity: Identifies the quantity expected to be supplied, administered or consumed by
            the subject.

        description: This provides a textual description of constraints on the intended activity
            occurrence, including relation to other activities.  It may also include
            objectives, pre-conditions and end-conditions.  Finally, it may convey
            specifics about the activity such as body site, method, route, etc.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("CarePlan_Detail") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CarePlan_Detail"]
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
                # A description of the kind of resource the in-line definition of a care plan
                # activity is representing.  The CarePlan.activity.detail is an in-line
                # definition when a resource is not referenced using
                # CarePlan.activity.reference.  For example, a MedicationRequest, a
                # ServiceRequest, or a CommunicationRequest.
                StructField(
                    "kind",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other
                # definition that is adhered to in whole or in part by this CarePlan activity.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(
                        canonicalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The URL pointing to an externally maintained protocol, guideline,
                # questionnaire or other definition that is adhered to in whole or in part by
                # this CarePlan activity.
                StructField(
                    "instantiatesUri",
                    ArrayType(
                        uriSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Detailed description of the type of planned activity; e.g. what lab test, what
                # procedure, what kind of encounter.
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
                # Provides the rationale that drove the inclusion of this particular activity as
                # part of the plan or the reason why the activity was prohibited.
                StructField(
                    "reasonCode",
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
                # Indicates another resource, such as the health condition(s), whose existence
                # justifies this request and drove the inclusion of this particular activity as
                # part of the plan.
                StructField(
                    "reasonReference",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Internal reference that identifies the goals that this activity is intended to
                # contribute towards meeting.
                StructField(
                    "goal",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Identifies what progress is being made for the specific activity.
                StructField("status", StringType(), True),
                # Provides reason why the activity isn't yet started, is on hold, was cancelled,
                # etc.
                StructField(
                    "statusReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If true, indicates that the described activity is one that must NOT be engaged
                # in when following the plan.  If false, or missing, indicates that the
                # described activity is one that should be engaged in when following the plan.
                StructField("doNotPerform", BooleanType(), True),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "scheduledTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "scheduledPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField("scheduledString", StringType(), True),
                # Identifies the facility where the activity will occur; e.g. home, hospital,
                # specific clinic, etc.
                StructField(
                    "location",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies who's expected to be involved in the activity.
                StructField(
                    "performer",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Identifies the food, drug or other product to be consumed or supplied in the
                # activity.
                StructField(
                    "productCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the food, drug or other product to be consumed or supplied in the
                # activity.
                StructField(
                    "productReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the quantity expected to be consumed in a given day.
                StructField(
                    "dailyAmount",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the quantity expected to be supplied, administered or consumed by
                # the subject.
                StructField(
                    "quantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # This provides a textual description of constraints on the intended activity
                # occurrence, including relation to other activities.  It may also include
                # objectives, pre-conditions and end-conditions.  Finally, it may convey
                # specifics about the activity such as body site, method, route, etc.
                StructField("description", StringType(), True),
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