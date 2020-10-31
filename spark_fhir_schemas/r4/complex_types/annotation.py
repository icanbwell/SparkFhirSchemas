from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Annotation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A  text note which also  contains information about who made the statement and
        when.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        authorReference: The individual responsible for making the annotation.

        authorString: The individual responsible for making the annotation.

        time: Indicates when this particular annotation was made.

        text: The text of the annotation in markdown format.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
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
                # The individual responsible for making the annotation.
                StructField(
                    "authorReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The individual responsible for making the annotation.
                StructField("authorString", StringType(), True),
                # Indicates when this particular annotation was made.
                StructField(
                    "time", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The text of the annotation in markdown format.
                StructField(
                    "text", markdown.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
