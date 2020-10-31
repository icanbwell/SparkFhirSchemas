from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImplementationGuide_Resource:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.


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

        reference: Where this resource is found.

        fhirVersion: Indicates the FHIR Version(s) this artifact is intended to apply to. If no
            versions are specified, the resource is assumed to apply to all the versions
            stated in ImplementationGuide.fhirVersion.

        name: A human assigned name for the resource. All resources SHOULD have a name, but
            the name may be extracted from the resource (e.g. ValueSet.name).

        description: A description of the reason that a resource has been included in the
            implementation guide.

        exampleBoolean: If true or a reference, indicates the resource is an example instance.  If a
            reference is present, indicates that the example is an example of the
            specified profile.

        exampleCanonical: If true or a reference, indicates the resource is an example instance.  If a
            reference is present, indicates that the example is an example of the
            specified profile.

        groupingId: Reference to the id of the grouping this resource appears in.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.id import id
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
                # Where this resource is found.
                StructField(
                    "reference", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the FHIR Version(s) this artifact is intended to apply to. If no
                # versions are specified, the resource is assumed to apply to all the versions
                # stated in ImplementationGuide.fhirVersion.
                # A human assigned name for the resource. All resources SHOULD have a name, but
                # the name may be extracted from the resource (e.g. ValueSet.name).
                StructField("name", StringType(), True),
                # A description of the reason that a resource has been included in the
                # implementation guide.
                StructField("description", StringType(), True),
                # If true or a reference, indicates the resource is an example instance.  If a
                # reference is present, indicates that the example is an example of the
                # specified profile.
                StructField("exampleBoolean", BooleanType(), True),
                # If true or a reference, indicates the resource is an example instance.  If a
                # reference is present, indicates that the example is an example of the
                # specified profile.
                StructField("exampleCanonical", StringType(), True),
                # Reference to the id of the grouping this resource appears in.
                StructField(
                    "groupingId", id.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
