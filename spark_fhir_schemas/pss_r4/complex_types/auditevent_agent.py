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
class AutoMapperElasticSearchAuditEvent_Agent(AutoMapperDataTypeComplexBase):
    """
    A record of an event made for purposes of maintaining a security log. Typical
    uses include detection of intrusion attempts and monitoring for inappropriate
    usage.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        role: Optional[Any] = None,
        who: Optional[Any] = None,
        altId: Optional[Any] = None,
        name: Optional[Any] = None,
        requestor: Optional[Any] = None,
        location: Optional[Any] = None,
        policy: Optional[Any] = None,
        media: Optional[Any] = None,
        network: Optional[Any] = None,
        purposeOfUse: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            role=role,
            who=who,
            altId=altId,
            name=name,
            requestor=requestor,
            location=location,
            policy=policy,
            media=media,
            network=network,
            purposeOfUse=purposeOfUse,
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
        A record of an event made for purposes of maintaining a security log. Typical
        uses include detection of intrusion attempts and monitoring for inappropriate
        usage.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: Specification of the participation type the user plays when performing the
            event.

        role: The security role that the user was acting under, that come from local codes
            defined by the access control security system (e.g. RBAC, ABAC) used in the
            local context.

        who: Reference to who this agent is that was involved in the event.

        altId: Alternative agent Identifier. For a human, this should be a user identifier
            text string from authentication system. This identifier would be one known to
            a common authentication system (e.g. single sign-on), if available.

        name: Human-meaningful name for the agent.

        requestor: Indicator that the user is or is not the requestor, or initiator, for the
            event being audited.

        location: Where the event occurred.

        policy: The policy or plan that authorized the activity being recorded. Typically, a
            single activity may have multiple applicable policies, such as patient
            consent, guarantor funding, etc. The policy would also indicate the security
            token used.

        media: Type of media involved. Used when the event is about exporting/importing onto
            media.

        network: Logical network location for application activity, if the activity has a
            network location.

        purposeOfUse: The reason (purpose of use), specific to this agent, that was used during the
            event being recorded.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.auditevent_network import (
            AutoMapperElasticSearchAuditEvent_Network as AuditEvent_NetworkSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("AuditEvent_Agent") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["AuditEvent_Agent"]
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
                # Specification of the participation type the user plays when performing the
                # event.
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
                # The security role that the user was acting under, that come from local codes
                # defined by the access control security system (e.g. RBAC, ABAC) used in the
                # local context.
                StructField(
                    "role",
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
                # Reference to who this agent is that was involved in the event.
                StructField(
                    "who",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Alternative agent Identifier. For a human, this should be a user identifier
                # text string from authentication system. This identifier would be one known to
                # a common authentication system (e.g. single sign-on), if available.
                StructField("altId", StringType(), True),
                # Human-meaningful name for the agent.
                StructField("name", StringType(), True),
                # Indicator that the user is or is not the requestor, or initiator, for the
                # event being audited.
                StructField("requestor", BooleanType(), True),
                # Where the event occurred.
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
                # The policy or plan that authorized the activity being recorded. Typically, a
                # single activity may have multiple applicable policies, such as patient
                # consent, guarantor funding, etc. The policy would also indicate the security
                # token used.
                StructField(
                    "policy",
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
                # Type of media involved. Used when the event is about exporting/importing onto
                # media.
                StructField(
                    "media",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Logical network location for application activity, if the activity has a
                # network location.
                StructField(
                    "network",
                    AuditEvent_NetworkSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The reason (purpose of use), specific to this agent, that was used during the
                # event being recorded.
                StructField(
                    "purposeOfUse",
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
