from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.molecularsequence_referenceseq import MolecularSequence_ReferenceSeq
        from spark_fhir_schemas.r4.complex_types.molecularsequence_variant import MolecularSequence_Variant
        from spark_fhir_schemas.r4.complex_types.molecularsequence_quality import MolecularSequence_Quality
        from spark_fhir_schemas.r4.complex_types.molecularsequence_repository import MolecularSequence_Repository
        from spark_fhir_schemas.r4.complex_types.molecularsequence_structurevariant import MolecularSequence_StructureVariant
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("type", StringType(), True),
                StructField(
                    "coordinateSystem",
                    integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "specimen", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "device", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "referenceSeq",
                    MolecularSequence_ReferenceSeq.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "variant",
                    ArrayType(
                        MolecularSequence_Variant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("observedSeq", StringType(), True),
                StructField(
                    "quality",
                    ArrayType(
                        MolecularSequence_Quality.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "readCoverage", integer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "repository",
                    ArrayType(
                        MolecularSequence_Repository.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "pointer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "structureVariant",
                    ArrayType(
                        MolecularSequence_StructureVariant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
