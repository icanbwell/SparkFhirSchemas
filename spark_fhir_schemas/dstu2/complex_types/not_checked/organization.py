from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OrganizationSchema:
    """
    A formally or informally recognized grouping of people or organizations formed
    for the purpose of achieving some form of collective action.  Includes
    companies, institutions, corporations, departments, community groups,
    healthcare practice groups, etc.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        A formally or informally recognized grouping of people or organizations formed
        for the purpose of achieving some form of collective action.  Includes
        companies, institutions, corporations, departments, community groups,
        healthcare practice groups, etc.


        resourceType: This is a Organization resource

        identifier: Identifier for the organization that is used to identify the organization
            across multiple disparate systems.

        active: Whether the organization's record is still in active use.

        type: The kind(s) of organization that this is.

        name: A name associated with the organization.

        alias: A list of alternate names that the organization is known as, or was known as
            in the past.

        telecom: A contact detail for the organization.

        address: An address for the organization.

        partOf: The organization of which this organization forms a part.

        contact: Contact for the organization for a certain purpose.

        endpoint: Technical endpoints providing access to services operated for the
            organization.

        """
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.contactpoint import (
            ContactPointSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.not_checked.address import AddressSchema
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.dstu2.complex_types.not_checked.organization_contact import (
            Organization_ContactSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Organization") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Organization"]
        schema = StructType(
            [
                # This is a Organization resource
                StructField("resourceType", StringType(), True),
                # Identifier for the organization that is used to identify the organization
                # across multiple disparate systems.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Whether the organization's record is still in active use.
                StructField("active", BooleanType(), True),
                # The kind(s) of organization that this is.
                StructField(
                    "type",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A name associated with the organization.
                StructField("name", StringType(), True),
                # A list of alternate names that the organization is known as, or was known as
                # in the past.
                # A contact detail for the organization.
                StructField(
                    "telecom",
                    ArrayType(
                        ContactPointSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An address for the organization.
                StructField(
                    "address",
                    ArrayType(
                        AddressSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The organization of which this organization forms a part.
                StructField(
                    "partOf",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Contact for the organization for a certain purpose.
                StructField(
                    "contact",
                    ArrayType(
                        Organization_ContactSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Technical endpoints providing access to services operated for the
                # organization.
                StructField(
                    "endpoint",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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