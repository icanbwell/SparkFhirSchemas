from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DataRequirement:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes a required data item for evaluation in terms of the type of data,
        and optional code or date-based filters of the data.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: The type of the required data, specified as the type name of a resource. For
            profiles, this value is set to the type of the base resource of the profile.

        profile: The profile of the required data, specified as the uri of the profile
            definition.

        subjectCodeableConcept: The intended subjects of the data requirement. If this element is not
            provided, a Patient subject is assumed.

        subjectReference: The intended subjects of the data requirement. If this element is not
            provided, a Patient subject is assumed.

        mustSupport: Indicates that specific elements of the type are referenced by the knowledge
            module and must be supported by the consumer in order to obtain an effective
            evaluation. This does not mean that a value is required for this element, only
            that the consuming system must understand the element and be able to provide
            values for it if they are available.

            The value of mustSupport SHALL be a FHIRPath resolveable on the type of the
            DataRequirement. The path SHALL consist only of identifiers, constant
            indexers, and .resolve() (see the [Simple FHIRPath
            Profile](fhirpath.html#simple) for full details).

        codeFilter: Code filters specify additional constraints on the data, specifying the value
            set of interest for a particular element of the data. Each code filter defines
            an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.

        dateFilter: Date filters specify additional constraints on the data in terms of the
            applicable date range for specific elements. Each date filter specifies an
            additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.

        limit: Specifies a maximum number of results that are required (uses the _count
            search parameter).

        sort: Specifies the order of the results to be returned.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.datarequirement_codefilter import DataRequirement_CodeFilter
        from spark_fhir_schemas.r4.complex_types.datarequirement_datefilter import DataRequirement_DateFilter
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.datarequirement_sort import DataRequirement_Sort
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
                # The type of the required data, specified as the type name of a resource. For
                # profiles, this value is set to the type of the base resource of the profile.
                StructField(
                    "type", code.get_schema(recursion_depth + 1), True
                ),
                # The profile of the required data, specified as the uri of the profile
                # definition.
                StructField(
                    "profile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The intended subjects of the data requirement. If this element is not
                # provided, a Patient subject is assumed.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The intended subjects of the data requirement. If this element is not
                # provided, a Patient subject is assumed.
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Indicates that specific elements of the type are referenced by the knowledge
                # module and must be supported by the consumer in order to obtain an effective
                # evaluation. This does not mean that a value is required for this element, only
                # that the consuming system must understand the element and be able to provide
                # values for it if they are available.
                #
                # The value of mustSupport SHALL be a FHIRPath resolveable on the type of the
                # DataRequirement. The path SHALL consist only of identifiers, constant
                # indexers, and .resolve() (see the [Simple FHIRPath
                # Profile](fhirpath.html#simple) for full details).
                StructField("mustSupport", ArrayType(StringType()), True),
                # Code filters specify additional constraints on the data, specifying the value
                # set of interest for a particular element of the data. Each code filter defines
                # an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.
                StructField(
                    "codeFilter",
                    ArrayType(
                        DataRequirement_CodeFilter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Date filters specify additional constraints on the data in terms of the
                # applicable date range for specific elements. Each date filter specifies an
                # additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
                StructField(
                    "dateFilter",
                    ArrayType(
                        DataRequirement_DateFilter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Specifies a maximum number of results that are required (uses the _count
                # search parameter).
                StructField(
                    "limit", positiveInt.get_schema(recursion_depth + 1), True
                ),
                # Specifies the order of the results to be returned.
                StructField(
                    "sort",
                    ArrayType(
                        DataRequirement_Sort.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
