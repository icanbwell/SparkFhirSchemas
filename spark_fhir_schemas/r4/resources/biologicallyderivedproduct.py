from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.biologicallyderivedproduct_collection import BiologicallyDerivedProduct_Collection
from spark_fhir_schemas.r4.resources.biologicallyderivedproduct_processing import BiologicallyDerivedProduct_Processing
from spark_fhir_schemas.r4.resources.biologicallyderivedproduct_manipulation import BiologicallyDerivedProduct_Manipulation
from spark_fhir_schemas.r4.resources.biologicallyderivedproduct_storage import BiologicallyDerivedProduct_Storage


class BiologicallyDerivedProduct:
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
                StructField("productCategory", StringType(), True),
                StructField("productCode", CodeableConcept.get_schema(), True),
                StructField("status", StringType(), True),
                StructField("request",ArrayType(Reference.get_schema()), True),
                StructField("quantity", integer.get_schema(), True),
                StructField("parent",ArrayType(Reference.get_schema()), True),
                StructField("collection", BiologicallyDerivedProduct_Collection.get_schema(), True),
                StructField("processing",ArrayType(BiologicallyDerivedProduct_Processing.get_schema()), True),
                StructField("manipulation", BiologicallyDerivedProduct_Manipulation.get_schema(), True),
                StructField("storage",ArrayType(BiologicallyDerivedProduct_Storage.get_schema()), True),]
        )

        return schema
