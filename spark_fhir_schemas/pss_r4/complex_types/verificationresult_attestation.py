from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchVerificationResult_Attestation(
    AutoMapperDataTypeComplexBase
):
    """
    Describes validation requirements, source(s), status and dates for one or more
    elements.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        who: Optional[Any] = None,
        onBehalfOf: Optional[Any] = None,
        communicationMethod: Optional[Any] = None,
        date: Optional[Any] = None,
        sourceIdentityCertificate: Optional[Any] = None,
        proxyIdentityCertificate: Optional[Any] = None,
        proxySignature: Optional[Any] = None,
        sourceSignature: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            who=who,
            onBehalfOf=onBehalfOf,
            communicationMethod=communicationMethod,
            date=date,
            sourceIdentityCertificate=sourceIdentityCertificate,
            proxyIdentityCertificate=proxyIdentityCertificate,
            proxySignature=proxySignature,
            sourceSignature=sourceSignature,
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
        Describes validation requirements, source(s), status and dates for one or more
        elements.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.signature import (
            AutoMapperElasticSearchSignature as SignatureSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("VerificationResult_Attestation")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["VerificationResult_Attestation"]
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
                # The individual or organization attesting to information.
                StructField(
                    "who",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When the who is asserting on behalf of another (organization or individual).
                StructField(
                    "onBehalfOf",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The method by which attested information was submitted/retrieved (manual; API;
                # Push).
                StructField(
                    "communicationMethod",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
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
                    SignatureSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Signed assertion by the attestation source that they have attested to the
                # information.
                StructField(
                    "sourceSignature",
                    SignatureSchema.schema(
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
