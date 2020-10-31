from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Coding:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A reference to a code defined by a terminology system.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        system: The identification of the code system that defines the meaning of the symbol
            in the code.

        version: The version of the code system which was used when choosing this code. Note
            that a well-maintained code system does not need the version reported, because
            the meaning of codes is consistent across versions. However this cannot
            consistently be assured, and when the meaning is not guaranteed to be
            consistent, the version SHOULD be exchanged.

        code: A symbol in syntax defined by the system. The symbol may be a predefined code
            or an expression in a syntax defined by the coding system (e.g. post-
            coordination).

        display: A representation of the meaning of the code in the system, following the rules
            of the system.

        userSelected: Indicates that this coding was chosen by a user directly - e.g. off a pick
            list of available items (codes or displays).

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
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
                # The identification of the code system that defines the meaning of the symbol
                # in the code.
                StructField(
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                # The version of the code system which was used when choosing this code. Note
                # that a well-maintained code system does not need the version reported, because
                # the meaning of codes is consistent across versions. However this cannot
                # consistently be assured, and when the meaning is not guaranteed to be
                # consistent, the version SHOULD be exchanged.
                StructField("version", StringType(), True),
                # A symbol in syntax defined by the system. The symbol may be a predefined code
                # or an expression in a syntax defined by the coding system (e.g. post-
                # coordination).
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                # A representation of the meaning of the code in the system, following the rules
                # of the system.
                StructField("display", StringType(), True),
                # Indicates that this coding was chosen by a user directly - e.g. off a pick
                # list of available items (codes or displays).
                StructField("userSelected", BooleanType(), True),
            ]
        )
        return schema
