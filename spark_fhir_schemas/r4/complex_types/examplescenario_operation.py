from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ExampleScenario_Operation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Example of workflow instance.


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

        number: The sequential number of the interaction, e.g. 1.2.5.

        type: The type of operation - CRUD.

        name: The human-friendly name of the interaction.

        initiator: Who starts the transaction.

        receiver: Who receives the transaction.

        description: A comment to be inserted in the diagram.

        initiatorActive: Whether the initiator is deactivated right after the transaction.

        receiverActive: Whether the receiver is deactivated right after the transaction.

        request: Each resource instance used by the initiator.

        response: Each resource instance used by the responder.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.examplescenario_containedinstance import ExampleScenario_ContainedInstance
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
                # The sequential number of the interaction, e.g. 1.2.5.
                StructField("number", StringType(), True),
                # The type of operation - CRUD.
                StructField("type", StringType(), True),
                # The human-friendly name of the interaction.
                StructField("name", StringType(), True),
                # Who starts the transaction.
                StructField("initiator", StringType(), True),
                # Who receives the transaction.
                StructField("receiver", StringType(), True),
                # A comment to be inserted in the diagram.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # Whether the initiator is deactivated right after the transaction.
                StructField("initiatorActive", BooleanType(), True),
                # Whether the receiver is deactivated right after the transaction.
                StructField("receiverActive", BooleanType(), True),
                # Each resource instance used by the initiator.
                StructField(
                    "request",
                    ExampleScenario_ContainedInstance.
                    get_schema(recursion_depth + 1), True
                ),
                # Each resource instance used by the responder.
                StructField(
                    "response",
                    ExampleScenario_ContainedInstance.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
