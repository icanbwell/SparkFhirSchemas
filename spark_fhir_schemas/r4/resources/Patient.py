from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType

from spark_fhir_schemas.r4.complex_types.human_name import FhirHumanName
from spark_fhir_schemas.r4.complex_types.reference import FhirReference
from spark_fhir_schemas.r4.resources.Id import Id
from spark_fhir_schemas.r4.resources.Meta import Meta
from spark_fhir_schemas.r4.resources.Uri import Uri
from spark_fhir_schemas.r4.resources.Code import Code
from spark_fhir_schemas.r4.resources.Narrative import Narrative
from spark_fhir_schemas.r4.resources.Resourcelist import Resourcelist
from spark_fhir_schemas.r4.resources.Extension import Extension
from spark_fhir_schemas.r4.resources.Extension import Extension
from spark_fhir_schemas.r4.resources.Identifier import Identifier
from spark_fhir_schemas.r4.resources.Boolean import Boolean
from spark_fhir_schemas.r4.resources.Humanname import Humanname
from spark_fhir_schemas.r4.resources.Contactpoint import Contactpoint
from spark_fhir_schemas.r4.resources.Date import Date
from spark_fhir_schemas.r4.resources.Address import Address
from spark_fhir_schemas.r4.resources.Codeableconcept import Codeableconcept
from spark_fhir_schemas.r4.resources.Attachment import Attachment
from spark_fhir_schemas.r4.resources.Patient_contact import Patient_contact
from spark_fhir_schemas.r4.resources.Patient_communication import Patient_communication
from spark_fhir_schemas.r4.resources.Reference import Reference
from spark_fhir_schemas.r4.resources.Reference import Reference
from spark_fhir_schemas.r4.resources.Patient_link import Patient_link


class Patient:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", Id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", Uri.get_schema(), True),
                StructField("language", Code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("active", BooleanType(), True),
                StructField("name",ArrayType(HumanName.get_schema()), True),
                StructField("telecom",ArrayType(ContactPoint.get_schema()), True),
                StructField("gender", StringType(), True),
                StructField("birthDate", DateType(), True),
                StructField("deceasedBoolean", BooleanType(), True),
                StructField("deceasedDateTime", StringType(), True),
                StructField("address",ArrayType(Address.get_schema()), True),
                StructField("maritalStatus", Codeableconcept.get_schema(), True),
                StructField("multipleBirthBoolean", BooleanType(), True),
                StructField("multipleBirthInteger", IntegerType(), True),
                StructField("photo",ArrayType(Attachment.get_schema()), True),
                StructField("contact",ArrayType(Patient_Contact.get_schema()), True),
                StructField("communication",ArrayType(Patient_Communication.get_schema()), True),
                StructField("generalPractitioner",ArrayType(Reference.get_schema()), True),
                StructField("managingOrganization", Reference.get_schema(), True),
                StructField("link",ArrayType(Patient_Link.get_schema()), True),]
        )

        return schema
