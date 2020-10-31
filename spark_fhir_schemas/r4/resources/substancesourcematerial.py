from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.substancesourcematerial_fractiondescription import SubstanceSourceMaterial_FractionDescription
from spark_fhir_schemas.r4.resources.substancesourcematerial_organism import SubstanceSourceMaterial_Organism
from spark_fhir_schemas.r4.resources.substancesourcematerial_partdescription import SubstanceSourceMaterial_PartDescription


class SubstanceSourceMaterial:
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
                StructField("sourceMaterialClass", CodeableConcept.get_schema(), True),
                StructField("sourceMaterialType", CodeableConcept.get_schema(), True),
                StructField("sourceMaterialState", CodeableConcept.get_schema(), True),
                StructField("organismId", Identifier.get_schema(), True),
                StructField("organismName", StringType(), True),
                StructField("parentSubstanceId",ArrayType(Identifier.get_schema()), True),
                StructField("parentSubstanceName",ArrayType(string.get_schema()), True),
                StructField("countryOfOrigin",ArrayType(CodeableConcept.get_schema()), True),
                StructField("geographicalLocation",ArrayType(string.get_schema()), True),
                StructField("developmentStage", CodeableConcept.get_schema(), True),
                StructField("fractionDescription",ArrayType(SubstanceSourceMaterial_FractionDescription.get_schema()), True),
                StructField("organism", SubstanceSourceMaterial_Organism.get_schema(), True),
                StructField("partDescription",ArrayType(SubstanceSourceMaterial_PartDescription.get_schema()), True),]
        )

        return schema
