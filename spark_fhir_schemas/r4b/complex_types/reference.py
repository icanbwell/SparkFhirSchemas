from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class ReferenceSchema:
    """
    A reference from one resource to another.
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
        A reference from one resource to another.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        reference: A reference to a location at which the other resource is found. The reference
            may be a relative reference, in which case it is relative to the service base
            URL, or an absolute URL that resolves to the location where the resource is
            found. The reference may be version specific or not. If the reference is not
            to a FHIR RESTful server, then it should be assumed to be version specific.
            Internal fragment references (start with '#') refer to contained resources.

        type: The expected type of the target of the reference. If both Reference.type and
            Reference.reference are populated and Reference.reference is a FHIR URL, both
            SHALL be consistent.

            The type is the Canonical URL of Resource Definition that is the type this
            reference refers to. References are URLs that are relative to
            http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference to
            http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only
            allowed for logical models (and can only be used in references in logical
            models, not resources).

        identifier: An identifier for the target resource. This is used when there is no way to
            reference the other resource directly, either because the entity it represents
            is not available through a FHIR server, or because there is no way for the
            author of the resource to convert a known identifier to an actual location.
            There is no requirement that a Reference.identifier point to something that is
            actually exposed as a FHIR instance, but it SHALL point to a business concept
            that would be expected to be exposed as a FHIR instance, and that instance
            would need to be of a FHIR resource type allowed by the reference.

        display: Plain text narrative that identifies the resource in addition to the resource
            reference.

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
        from spark_fhir_schemas.r4b.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4b.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4b.complex_types.identifier import IdentifierSchema

        if (
            max_recursion_limit
            and nesting_list.count("Reference") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Reference"]
        my_parent_path = parent_path + ".reference" if parent_path else "reference"
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
                # A reference to a location at which the other resource is found. The reference
                # may be a relative reference, in which case it is relative to the service base
                # URL, or an absolute URL that resolves to the location where the resource is
                # found. The reference may be version specific or not. If the reference is not
                # to a FHIR RESTful server, then it should be assumed to be version specific.
                # Internal fragment references (start with '#') refer to contained resources.
                StructField("reference", StringType(), True),
                # The expected type of the target of the reference. If both Reference.type and
                # Reference.reference are populated and Reference.reference is a FHIR URL, both
                # SHALL be consistent.
                #
                # The type is the Canonical URL of Resource Definition that is the type this
                # reference refers to. References are URLs that are relative to
                # http://hl7.org/fhir/StructureDefinition/ e.g. "Patient" is a reference to
                # http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only
                # allowed for logical models (and can only be used in references in logical
                # models, not resources).
                StructField(
                    "type",
                    uriSchema.get_schema(
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
                        parent_path=my_parent_path + ".type",
                    ),
                    True,
                ),
                # An identifier for the target resource. This is used when there is no way to
                # reference the other resource directly, either because the entity it represents
                # is not available through a FHIR server, or because there is no way for the
                # author of the resource to convert a known identifier to an actual location.
                # There is no requirement that a Reference.identifier point to something that is
                # actually exposed as a FHIR instance, but it SHALL point to a business concept
                # that would be expected to be exposed as a FHIR instance, and that instance
                # would need to be of a FHIR resource type allowed by the reference.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
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
                # Plain text narrative that identifies the resource in addition to the resource
                # reference.
                StructField("display", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                c
                if c.name != "modifierExtension"
                else StructField("modifierExtension", StringType(), True)
                for c in schema.fields
            ]

        return schema