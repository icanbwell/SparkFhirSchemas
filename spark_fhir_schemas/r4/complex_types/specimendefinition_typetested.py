from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SpecimenDefinition_TypeTested:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A kind of specimen with associated set of requirements.


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

        isDerived: Primary of secondary specimen.

        type: The kind of specimen conditioned for testing expected by lab.

        preference: The preference for this type of conditioned specimen.

        container: The specimen's container.

        requirement: Requirements for delivery and special handling of this kind of conditioned
            specimen.

        retentionTime: The usual time that a specimen of this kind is retained after the ordered
            tests are completed, for the purpose of additional testing.

        rejectionCriterion: Criterion for rejection of the specimen in its container by the laboratory.

        handling: Set of instructions for preservation/transport of the specimen at a defined
            temperature interval, prior the testing process.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.specimendefinition_container import SpecimenDefinition_Container
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.specimendefinition_handling import SpecimenDefinition_Handling
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
                # Primary of secondary specimen.
                StructField("isDerived", BooleanType(), True),
                # The kind of specimen conditioned for testing expected by lab.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The preference for this type of conditioned specimen.
                StructField("preference", StringType(), True),
                # The specimen's container.
                StructField(
                    "container",
                    SpecimenDefinition_Container.
                    get_schema(recursion_depth + 1), True
                ),
                # Requirements for delivery and special handling of this kind of conditioned
                # specimen.
                StructField("requirement", StringType(), True),
                # The usual time that a specimen of this kind is retained after the ordered
                # tests are completed, for the purpose of additional testing.
                StructField(
                    "retentionTime", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # Criterion for rejection of the specimen in its container by the laboratory.
                StructField(
                    "rejectionCriterion",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Set of instructions for preservation/transport of the specimen at a defined
                # temperature interval, prior the testing process.
                StructField(
                    "handling",
                    ArrayType(
                        SpecimenDefinition_Handling.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
