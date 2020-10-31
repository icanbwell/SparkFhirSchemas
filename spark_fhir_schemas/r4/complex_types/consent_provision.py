from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Consent_Provision:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.consent_actor import Consent_Actor
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.consent_data import Consent_Data
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
                # Action  to take - permit or deny - when the rule conditions are met.  Not
                # permitted in root rule, required in all nested rules.
                StructField("type", StringType(), True),
                # The timeframe in this rule is valid.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # Who or what is controlled by this rule. Use group to identify a set of actors
                # by some property they share (e.g. 'admitting officers').
                StructField(
                    "actor",
                    ArrayType(Consent_Actor.get_schema(recursion_depth + 1)),
                    True
                ),
                # Actions controlled by this Rule.
                StructField(
                    "action",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A security label, comprised of 0..* security label fields (Privacy tags),
                # which define which resources are controlled by this exception.
                StructField(
                    "securityLabel",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                # The context of the activities a user is taking - why the user is accessing the
                # data - that are controlled by this rule.
                StructField(
                    "purpose",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                # The class of information covered by this rule. The type can be a FHIR resource
                # type, a profile on a type, or a CDA document, or some other type that
                # indicates what sort of information the consent relates to.
                StructField(
                    "class", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                # If this code is found in an instance, then the rule applies.
                StructField(
                    "code",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Clinical or Operational Relevant period of time that bounds the data
                # controlled by this rule.
                StructField(
                    "dataPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # The resources controlled by this rule if specific resources are referenced.
                StructField(
                    "data",
                    ArrayType(Consent_Data.get_schema(recursion_depth + 1)),
                    True
                ),
                # Rules which provide exceptions to the base rule or subrules.
                StructField(
                    "provision",
                    ArrayType(
                        Consent_Provision.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
