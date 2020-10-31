from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Specimen_Container:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A sample to be used for analysis.


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

        identifier: Id for container. There may be multiple; a manufacturer's bar code, lab
            assigned identifier, etc. The container ID may differ from the specimen id in
            some circumstances.

        description: Textual description of the container.

        type: The type of container associated with the specimen (e.g. slide, aliquot,
            etc.).

        capacity: The capacity (volume or other measure) the container may contain.

        specimenQuantity: The quantity of specimen in the container; may be volume, dimensions, or other
            appropriate measurements, depending on the specimen type.

        additiveCodeableConcept: Introduced substance to preserve, maintain or enhance the specimen. Examples:
            Formalin, Citrate, EDTA.

        additiveReference: Introduced substance to preserve, maintain or enhance the specimen. Examples:
            Formalin, Citrate, EDTA.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # Id for container. There may be multiple; a manufacturer's bar code, lab
                # assigned identifier, etc. The container ID may differ from the specimen id in
                # some circumstances.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Textual description of the container.
                StructField("description", StringType(), True),
                # The type of container associated with the specimen (e.g. slide, aliquot,
                # etc.).
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The capacity (volume or other measure) the container may contain.
                StructField(
                    "capacity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # The quantity of specimen in the container; may be volume, dimensions, or other
                # appropriate measurements, depending on the specimen type.
                StructField(
                    "specimenQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                # Introduced substance to preserve, maintain or enhance the specimen. Examples:
                # Formalin, Citrate, EDTA.
                StructField(
                    "additiveCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Introduced substance to preserve, maintain or enhance the specimen. Examples:
                # Formalin, Citrate, EDTA.
                StructField(
                    "additiveReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
