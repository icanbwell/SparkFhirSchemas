from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CarePlan_Detail:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                # A description of the kind of resource the in-line definition of a care plan
                # activity is representing.  The CarePlan.activity.detail is an in-line
                # definition when a resource is not referenced using
                # CarePlan.activity.reference.  For example, a MedicationRequest, a
                # ServiceRequest, or a CommunicationRequest.
                StructField(
                    "kind", code.get_schema(recursion_depth + 1), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other
                # definition that is adhered to in whole or in part by this CarePlan activity.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline,
                # questionnaire or other definition that is adhered to in whole or in part by
                # this CarePlan activity.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # Detailed description of the type of planned activity; e.g. what lab test, what
                # procedure, what kind of encounter.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Provides the rationale that drove the inclusion of this particular activity as
                # part of the plan or the reason why the activity was prohibited.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource, such as the health condition(s), whose existence
                # justifies this request and drove the inclusion of this particular activity as
                # part of the plan.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Internal reference that identifies the goals that this activity is intended to
                # contribute towards meeting.
                StructField(
                    "goal",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies what progress is being made for the specific activity.
                StructField("status", StringType(), True),
                # Provides reason why the activity isn't yet started, is on hold, was cancelled,
                # etc.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # If true, indicates that the described activity is one that must NOT be engaged
                # in when following the plan.  If false, or missing, indicates that the
                # described activity is one that should be engaged in when following the plan.
                StructField("doNotPerform", BooleanType(), True),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "scheduledTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "scheduledPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField("scheduledString", StringType(), True),
                # Identifies the facility where the activity will occur; e.g. home, hospital,
                # specific clinic, etc.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies who's expected to be involved in the activity.
                StructField(
                    "performer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the food, drug or other product to be consumed or supplied in the
                # activity.
                StructField(
                    "productCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identifies the food, drug or other product to be consumed or supplied in the
                # activity.
                StructField(
                    "productReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies the quantity expected to be consumed in a given day.
                StructField(
                    "dailyAmount", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Identifies the quantity expected to be supplied, administered or consumed by
                # the subject.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # This provides a textual description of constraints on the intended activity
                # occurrence, including relation to other activities.  It may also include
                # objectives, pre-conditions and end-conditions.  Finally, it may convey
                # specifics about the activity such as body site, method, route, etc.
                StructField("description", StringType(), True),
            ]
        )
        return schema
