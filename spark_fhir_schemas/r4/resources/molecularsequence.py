from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.molecularsequence_referenceseq import MolecularSequence_ReferenceSeq
from spark_fhir_schemas.r4.complex_types.molecularsequence_variant import MolecularSequence_Variant
from spark_fhir_schemas.r4.complex_types.molecularsequence_quality import MolecularSequence_Quality
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.molecularsequence_repository import MolecularSequence_Repository
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.molecularsequence_structurevariant import MolecularSequence_StructureVariant


class MolecularSequence:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("type", StringType(), True),
                StructField("coordinateSystem", integer.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("specimen", Reference.get_schema(), True),
                StructField("device", Reference.get_schema(), True),
                StructField("performer", Reference.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("referenceSeq", MolecularSequence_ReferenceSeq.get_schema(), True),
                StructField("variant",ArrayType(MolecularSequence_Variant.get_schema()), True),
                StructField("observedSeq", StringType(), True),
                StructField("quality",ArrayType(MolecularSequence_Quality.get_schema()), True),
                StructField("readCoverage", integer.get_schema(), True),
                StructField("repository",ArrayType(MolecularSequence_Repository.get_schema()), True),
                StructField("pointer",ArrayType(Reference.get_schema()), True),
                StructField("structureVariant",ArrayType(MolecularSequence_StructureVariant.get_schema()), True),
            ]
        )

        return schema
