from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class VerificationResult_Attestation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Describes validation requirements, source(s), status and dates for one or more
        elements.


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

        who: The individual or organization attesting to information.

        onBehalfOf: When the who is asserting on behalf of another (organization or individual).

        communicationMethod: The method by which attested information was submitted/retrieved (manual; API;
            Push).

        date: The date the information was attested to.

        sourceIdentityCertificate: A digital identity certificate associated with the attestation source.

        proxyIdentityCertificate: A digital identity certificate associated with the proxy entity submitting
            attested information on behalf of the attestation source.

        proxySignature: Signed assertion by the proxy entity indicating that they have the right to
            submit attested information on behalf of the attestation source.

        sourceSignature: Signed assertion by the attestation source that they have attested to the
            information.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.signature import Signature
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
                # The individual or organization attesting to information.
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                # When the who is asserting on behalf of another (organization or individual).
                StructField(
                    "onBehalfOf", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The method by which attested information was submitted/retrieved (manual; API;
                # Push).
                StructField(
                    "communicationMethod",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The date the information was attested to.
                StructField("date", DateType(), True),
                # A digital identity certificate associated with the attestation source.
                StructField("sourceIdentityCertificate", StringType(), True),
                # A digital identity certificate associated with the proxy entity submitting
                # attested information on behalf of the attestation source.
                StructField("proxyIdentityCertificate", StringType(), True),
                # Signed assertion by the proxy entity indicating that they have the right to
                # submit attested information on behalf of the attestation source.
                StructField(
                    "proxySignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                # Signed assertion by the attestation source that they have attested to the
                # information.
                StructField(
                    "sourceSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
