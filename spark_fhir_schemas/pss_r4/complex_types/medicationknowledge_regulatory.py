from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicationKnowledge_Regulatory(
    AutoMapperDataTypeComplexBase
):
    """
    Information about a medication that is used to support knowledge.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        regulatoryAuthority: Optional[Any] = None,
        substitution: Optional[Any] = None,
        schedule: Optional[Any] = None,
        maxDispense: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            regulatoryAuthority=regulatoryAuthority,
            substitution=substitution,
            schedule=schedule,
            maxDispense=maxDispense,
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
        Information about a medication that is used to support knowledge.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        regulatoryAuthority: The authority that is specifying the regulations.

        substitution: Specifies if changes are allowed when dispensing a medication from a
            regulatory perspective.

        schedule: Specifies the schedule of a medication in jurisdiction.

        maxDispense: The maximum number of units of the medication that can be dispensed in a
            period.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_substitution import (
            AutoMapperElasticSearchMedicationKnowledge_Substitution as MedicationKnowledge_SubstitutionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_schedule import (
            AutoMapperElasticSearchMedicationKnowledge_Schedule as MedicationKnowledge_ScheduleSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_maxdispense import (
            AutoMapperElasticSearchMedicationKnowledge_MaxDispense as MedicationKnowledge_MaxDispenseSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MedicationKnowledge_Regulatory")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationKnowledge_Regulatory"]
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
                # The authority that is specifying the regulations.
                StructField(
                    "regulatoryAuthority",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies if changes are allowed when dispensing a medication from a
                # regulatory perspective.
                StructField(
                    "substitution",
                    ArrayType(
                        MedicationKnowledge_SubstitutionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Specifies the schedule of a medication in jurisdiction.
                StructField(
                    "schedule",
                    ArrayType(
                        MedicationKnowledge_ScheduleSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The maximum number of units of the medication that can be dispensed in a
                # period.
                StructField(
                    "maxDispense",
                    MedicationKnowledge_MaxDispenseSchema.schema(
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
