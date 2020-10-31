from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class VisionPrescription_LensSpecification:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An authorization for the provision of glasses and/or contact lenses to a
        patient.


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

        product: Identifies the type of vision correction product which is required for the
            patient.

        eye: The eye for which the lens specification applies.

        sphere: Lens power measured in dioptres (0.25 units).

        cylinder: Power adjustment for astigmatism measured in dioptres (0.25 units).

        axis: Adjustment for astigmatism measured in integer degrees.

        prism: Allows for adjustment on two axis.

        add: Power adjustment for multifocal lenses measured in dioptres (0.25 units).

        power: Contact lens power measured in dioptres (0.25 units).

        backCurve: Back curvature measured in millimetres.

        diameter: Contact lens diameter measured in millimetres.

        duration: The recommended maximum wear period for the lens.

        color: Special color or pattern.

        brand: Brand recommendations or restrictions.

        note: Notes for special requirements such as coatings and lens materials.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.visionprescription_prism import VisionPrescription_Prism
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
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
                # Identifies the type of vision correction product which is required for the
                # patient.
                StructField(
                    "product", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The eye for which the lens specification applies.
                StructField("eye", StringType(), True),
                # Lens power measured in dioptres (0.25 units).
                StructField(
                    "sphere", decimal.get_schema(recursion_depth + 1), True
                ),
                # Power adjustment for astigmatism measured in dioptres (0.25 units).
                StructField(
                    "cylinder", decimal.get_schema(recursion_depth + 1), True
                ),
                # Adjustment for astigmatism measured in integer degrees.
                StructField(
                    "axis", integer.get_schema(recursion_depth + 1), True
                ),
                # Allows for adjustment on two axis.
                StructField(
                    "prism",
                    ArrayType(
                        VisionPrescription_Prism.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Power adjustment for multifocal lenses measured in dioptres (0.25 units).
                StructField(
                    "add", decimal.get_schema(recursion_depth + 1), True
                ),
                # Contact lens power measured in dioptres (0.25 units).
                StructField(
                    "power", decimal.get_schema(recursion_depth + 1), True
                ),
                # Back curvature measured in millimetres.
                StructField(
                    "backCurve", decimal.get_schema(recursion_depth + 1), True
                ),
                # Contact lens diameter measured in millimetres.
                StructField(
                    "diameter", decimal.get_schema(recursion_depth + 1), True
                ),
                # The recommended maximum wear period for the lens.
                StructField(
                    "duration", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Special color or pattern.
                StructField("color", StringType(), True),
                # Brand recommendations or restrictions.
                StructField("brand", StringType(), True),
                # Notes for special requirements such as coatings and lens materials.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
