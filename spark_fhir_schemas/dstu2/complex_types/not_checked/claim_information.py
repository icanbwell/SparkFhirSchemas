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
class Claim_InformationSchema:
    """
    A provider issued list of services and products provided, or to be provided,
    to a patient which is provided to an insurer for payment recovery.
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
        A provider issued list of services and products provided, or to be provided,
        to a patient which is provided to an insurer for payment recovery.


        sequence: Sequence of the information element which serves to provide a link.

        category: The general class of the information supplied: information; exception;
            accident, employment; onset, etc.

        code: System and code pertaining to the specific information regarding special
            conditions relating to the setting, treatment or patient  for which care is
            sought which may influence the adjudication.

        timingDate: The date when or period to which this information refers.

        timingPeriod: The date when or period to which this information refers.

        valueString: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueQuantity: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueAttachment: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueReference: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        reason: For example, provides the reason for: the additional stay, or missing tooth or
            any other situation where a reason code is required in addition to the
            content.

        """
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
        from spark_fhir_schemas.dstu2.complex_types.not_checked.quantity import QuantitySchema
        from spark_fhir_schemas.dstu2.complex_types.not_checked.attachment import AttachmentSchema
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema

        if (
            max_recursion_limit
            and nesting_list.count("Claim_Information") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Claim_Information"]
        schema = StructType(
            [
                # Sequence of the information element which serves to provide a link.
                StructField("sequence", IntegerType(), True),
                # The general class of the information supplied: information; exception;
                # accident, employment; onset, etc.
                StructField(
                    "category",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # System and code pertaining to the specific information regarding special
                # conditions relating to the setting, treatment or patient  for which care is
                # sought which may influence the adjudication.
                StructField(
                    "code",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date when or period to which this information refers.
                StructField("timingDate", StringType(), True),
                # The date when or period to which this information refers.
                StructField(
                    "timingPeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField("valueString", StringType(), True),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # For example, provides the reason for: the additional stay, or missing tooth or
                # any other situation where a reason code is required in addition to the
                # content.
                StructField(
                    "reason",
                    CodeableConceptSchema.get_schema(
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