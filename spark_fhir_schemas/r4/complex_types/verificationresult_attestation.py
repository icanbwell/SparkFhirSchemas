from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class VerificationResult_AttestationSchema:
    """
    Describes validation requirements, source(s), status and dates for one or more
    elements.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
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
        if extension_fields is None:
            extension_fields = [
                "valueBoolean",
                "valueCode",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valuePositiveInt",
                "valueString",
                "valueTime",
                "valueUnsignedInt",
                "valueUri",
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.r4.complex_types.signature import SignatureSchema

        if (
            max_recursion_limit
            and nesting_list.count("VerificationResult_Attestation")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["VerificationResult_Attestation"]
        my_parent_path = (
            parent_path + ".verificationresult_attestation"
            if parent_path
            else "verificationresult_attestation"
        )
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
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
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
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # The individual or organization attesting to information.
                StructField(
                    "who",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # When the who is asserting on behalf of another (organization or individual).
                StructField(
                    "onBehalfOf",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # The method by which attested information was submitted/retrieved (manual; API;
                # Push).
                StructField(
                    "communicationMethod",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
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
                    SignatureSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Signed assertion by the attestation source that they have attested to the
                # information.
                StructField(
                    "sourceSignature",
                    SignatureSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                (
                    c
                    if c.name != "extension"
                    else StructField("extension", StringType(), True)
                )
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                (
                    c
                    if c.name != "modifierExtension"
                    else StructField("modifierExtension", StringType(), True)
                )
                for c in schema.fields
            ]

        return schema
