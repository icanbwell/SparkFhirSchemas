from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
#checked
from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
from pyspark.sql.types import ArrayType
class ContactPointSchema:
    """
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        Details for all kinds of technology mediated contact points for a person or
        organization, including telephone, email, etc.


        system: Telecommunications form for contact point - what communications system is
            required to make use of the contact.

        value: The actual contact point details, in a form that is meaningful to the
            designated communication system (i.e. phone number or email address).

        use: Identifies the purpose for the contact point.

        rank: Specifies a preferred order in which to use a set of contacts. Contacts are
            ranked with lower values coming before higher values.

        period: Time period when the contact point was/is in use.

        """
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema

        if (
            max_recursion_limit
            and nesting_list.count("ContactPoint") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ContactPoint"]
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
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            # extension_fields=extension_fields,
                            # extension_depth=extension_depth,
                            # max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),

                # Telecommunications form for contact point - what communications system is
                # required to make use of the contact.
                StructField("system", StringType(), True),
                # The actual contact point details, in a form that is meaningful to the
                # designated communication system (i.e. phone number or email address).
                StructField("value", StringType(), True),
                # Identifies the purpose for the contact point.
                StructField("use", StringType(), True),
                # Specifies a preferred order in which to use a set of contacts. Contacts are
                # ranked with lower values coming before higher values.
                StructField("rank", IntegerType(), True),
                # Time period when the contact point was/is in use.
                StructField(
                    "period",
                    PeriodSchema.get_schema(
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