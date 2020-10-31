from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ProdCharacteristic:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The marketing status describes the date when a medicinal product is actually
        put on the market or the date as of which it is no longer available.


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

        height: Where applicable, the height can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        width: Where applicable, the width can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        depth: Where applicable, the depth can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        weight: Where applicable, the weight can be specified using a numerical value and its
            unit of measurement The unit of measurement shall be specified in accordance
            with ISO 11240 and the resulting terminology The symbol and the symbol
            identifier shall be used.

        nominalVolume: Where applicable, the nominal volume can be specified using a numerical value
            and its unit of measurement The unit of measurement shall be specified in
            accordance with ISO 11240 and the resulting terminology The symbol and the
            symbol identifier shall be used.

        externalDiameter: Where applicable, the external diameter can be specified using a numerical
            value and its unit of measurement The unit of measurement shall be specified
            in accordance with ISO 11240 and the resulting terminology The symbol and the
            symbol identifier shall be used.

        shape: Where applicable, the shape can be specified An appropriate controlled
            vocabulary shall be used The term and the term identifier shall be used.

        color: Where applicable, the color can be specified An appropriate controlled
            vocabulary shall be used The term and the term identifier shall be used.

        imprint: Where applicable, the imprint can be specified as text.

        image: Where applicable, the image can be provided The format of the image attachment
            shall be specified by regional implementations.

        scoring: Where applicable, the scoring can be specified An appropriate controlled
            vocabulary shall be used The term and the term identifier shall be used.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                # Where applicable, the height can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "height", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Where applicable, the width can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "width", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Where applicable, the depth can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "depth", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Where applicable, the weight can be specified using a numerical value and its
                # unit of measurement The unit of measurement shall be specified in accordance
                # with ISO 11240 and the resulting terminology The symbol and the symbol
                # identifier shall be used.
                StructField(
                    "weight", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Where applicable, the nominal volume can be specified using a numerical value
                # and its unit of measurement The unit of measurement shall be specified in
                # accordance with ISO 11240 and the resulting terminology The symbol and the
                # symbol identifier shall be used.
                StructField(
                    "nominalVolume", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Where applicable, the external diameter can be specified using a numerical
                # value and its unit of measurement The unit of measurement shall be specified
                # in accordance with ISO 11240 and the resulting terminology The symbol and the
                # symbol identifier shall be used.
                StructField(
                    "externalDiameter",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                # Where applicable, the shape can be specified An appropriate controlled
                # vocabulary shall be used The term and the term identifier shall be used.
                StructField("shape", StringType(), True),
                # Where applicable, the color can be specified An appropriate controlled
                # vocabulary shall be used The term and the term identifier shall be used.
                StructField("color", ArrayType(StringType()), True),
                # Where applicable, the imprint can be specified as text.
                StructField("imprint", ArrayType(StringType()), True),
                # Where applicable, the image can be provided The format of the image attachment
                # shall be specified by regional implementations.
                StructField(
                    "image",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
                # Where applicable, the scoring can be specified An appropriate controlled
                # vocabulary shall be used The term and the term identifier shall be used.
                StructField(
                    "scoring", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
