from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.substancespecification_moiety import SubstanceSpecification_Moiety
from spark_fhir_schemas.r4.complex_types.substancespecification_property import SubstanceSpecification_Property
from spark_fhir_schemas.r4.complex_types.substancespecification_structure import SubstanceSpecification_Structure
from spark_fhir_schemas.r4.complex_types.substancespecification_code import SubstanceSpecification_Code
from spark_fhir_schemas.r4.complex_types.substancespecification_name import SubstanceSpecification_Name
from spark_fhir_schemas.r4.complex_types.substancespecification_molecularweight import SubstanceSpecification_MolecularWeight
from spark_fhir_schemas.r4.complex_types.substancespecification_relationship import SubstanceSpecification_Relationship


# noinspection PyPep8Naming
class SubstanceSpecification:
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
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("status", CodeableConcept.get_schema(), True),
                StructField("domain", CodeableConcept.get_schema(), True),
                StructField("description", StringType(), True),
                StructField("source", ArrayType(Reference.get_schema()), True),
                StructField("comment", StringType(), True),
                StructField(
                    "moiety",
                    ArrayType(SubstanceSpecification_Moiety.get_schema()), True
                ),
                StructField(
                    "property",
                    ArrayType(SubstanceSpecification_Property.get_schema()),
                    True
                ),
                StructField(
                    "referenceInformation", Reference.get_schema(), True
                ),
                StructField(
                    "structure", SubstanceSpecification_Structure.get_schema(),
                    True
                ),
                StructField(
                    "code",
                    ArrayType(SubstanceSpecification_Code.get_schema()), True
                ),
                StructField(
                    "name",
                    ArrayType(SubstanceSpecification_Name.get_schema()), True
                ),
                StructField(
                    "molecularWeight",
                    ArrayType(
                        SubstanceSpecification_MolecularWeight.get_schema()
                    ), True
                ),
                StructField(
                    "relationship",
                    ArrayType(
                        SubstanceSpecification_Relationship.get_schema()
                    ), True
                ),
                StructField("nucleicAcid", Reference.get_schema(), True),
                StructField("polymer", Reference.get_schema(), True),
                StructField("protein", Reference.get_schema(), True),
                StructField("sourceMaterial", Reference.get_schema(), True),
            ]
        )

        return schema
