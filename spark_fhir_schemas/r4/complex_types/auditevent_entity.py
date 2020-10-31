from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AuditEvent_Entity:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        what: Identifies a specific instance of the entity. The reference should be version
            specific.

        type: The type of the object that was involved in this audit event.

        role: Code representing the role the entity played in the event being audited.

        lifecycle: Identifier for the data life-cycle stage for the entity.

        securityLabel: Security labels for the identified entity.

        name: A name of the entity in the audit event.

        description: Text that describes the entity in more detail.

        query: The query parameters for a query-type entities.

        detail: Tagged value pairs for conveying additional information about the entity.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.simple_types.base64binary import base64Binary
        from spark_fhir_schemas.r4.complex_types.auditevent_detail import AuditEvent_Detail
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
                # Identifies a specific instance of the entity. The reference should be version
                # specific.
                StructField(
                    "what", Reference.get_schema(recursion_depth + 1), True
                ),
                # The type of the object that was involved in this audit event.
                StructField(
                    "type", Coding.get_schema(recursion_depth + 1), True
                ),
                # Code representing the role the entity played in the event being audited.
                StructField(
                    "role", Coding.get_schema(recursion_depth + 1), True
                ),
                # Identifier for the data life-cycle stage for the entity.
                StructField(
                    "lifecycle", Coding.get_schema(recursion_depth + 1), True
                ),
                # Security labels for the identified entity.
                StructField(
                    "securityLabel",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                # A name of the entity in the audit event.
                StructField("name", StringType(), True),
                # Text that describes the entity in more detail.
                StructField("description", StringType(), True),
                # The query parameters for a query-type entities.
                StructField(
                    "query", base64Binary.get_schema(recursion_depth + 1), True
                ),
                # Tagged value pairs for conveying additional information about the entity.
                StructField(
                    "detail",
                    ArrayType(
                        AuditEvent_Detail.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
