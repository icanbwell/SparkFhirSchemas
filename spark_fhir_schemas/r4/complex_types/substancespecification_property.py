from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceSpecification_Property:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The detailed description of a substance, typically at a level beyond what is
        used for prescribing.


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

        category: A category for this property, e.g. Physical, Chemical, Enzymatic.

        code: Property type e.g. viscosity, pH, isoelectric point.

        parameters: Parameters that were used in the measurement of a property (e.g. for
            viscosity: measured at 20C with a pH of 7.1).

        definingSubstanceReference: A substance upon which a defining property depends (e.g. for solubility: in
            water, in alcohol).

        definingSubstanceCodeableConcept: A substance upon which a defining property depends (e.g. for solubility: in
            water, in alcohol).

        amountQuantity: Quantitative value for this property.

        amountString: Quantitative value for this property.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                # A category for this property, e.g. Physical, Chemical, Enzymatic.
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Property type e.g. viscosity, pH, isoelectric point.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Parameters that were used in the measurement of a property (e.g. for
                # viscosity: measured at 20C with a pH of 7.1).
                StructField("parameters", StringType(), True),
                # A substance upon which a defining property depends (e.g. for solubility: in
                # water, in alcohol).
                StructField(
                    "definingSubstanceReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A substance upon which a defining property depends (e.g. for solubility: in
                # water, in alcohol).
                StructField(
                    "definingSubstanceCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Quantitative value for this property.
                StructField(
                    "amountQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Quantitative value for this property.
                StructField("amountString", StringType(), True),
            ]
        )
        return schema
