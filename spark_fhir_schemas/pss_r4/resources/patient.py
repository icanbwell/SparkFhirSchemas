from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    IntegerType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchPatient(AutoMapperDataTypeComplexBase):
    """
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        resourceType: Optional[Any] = None,
        id_: Optional[Any] = None,
        meta: Optional[Any] = None,
        implicitRules: Optional[Any] = None,
        language: Optional[Any] = None,
        text: Optional[Any] = None,
        contained: Optional[Any] = None,
        extension: Optional[Any] = None,
        identifier: Optional[Any] = None,
        active: Optional[Any] = None,
        name: Optional[Any] = None,
        telecom: Optional[Any] = None,
        gender: Optional[Any] = None,
        birthDate: Optional[Any] = None,
        deceasedBoolean: Optional[Any] = None,
        deceasedDateTime: Optional[Any] = None,
        address: Optional[Any] = None,
        maritalStatus: Optional[Any] = None,
        multipleBirthBoolean: Optional[Any] = None,
        multipleBirthInteger: Optional[Any] = None,
        photo: Optional[Any] = None,
        contact: Optional[Any] = None,
        communication: Optional[Any] = None,
        generalPractitioner: Optional[Any] = None,
        managingOrganization: Optional[Any] = None,
        link: Optional[Any] = None,
    ) -> None:
        super().__init__(
            resourceType=resourceType,
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            identifier=identifier,
            active=active,
            name=name,
            telecom=telecom,
            gender=gender,
            birthDate=birthDate,
            deceasedBoolean=deceasedBoolean,
            deceasedDateTime=deceasedDateTime,
            address=address,
            maritalStatus=maritalStatus,
            multipleBirthBoolean=multipleBirthBoolean,
            multipleBirthInteger=multipleBirthInteger,
            photo=photo,
            contact=contact,
            communication=communication,
            generalPractitioner=generalPractitioner,
            managingOrganization=managingOrganization,
            link=link,
        )
        super().include_null_properties(include_null_properties=True)

    @staticmethod
    def schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        Demographics and other administrative information about an individual or
        animal receiving care or other health-related services.


        resourceType: This is a Patient resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        identifier: An identifier for this patient.

        active: Whether this patient record is in active use.
            Many systems use this property to mark as non-current patients, such as those
            that have not been seen for a period of time based on an organization's
            business rules.

            It is often used to filter patient lists to exclude inactive patients

            Deceased patients may also be marked as inactive for the same reasons, but may
            be active for some time after death.

        name: A name associated with the individual.

        telecom: A contact detail (e.g. a telephone number or an email address) by which the
            individual may be contacted.

        gender: Administrative Gender - the gender that the patient is considered to have for
            administration and record keeping purposes.

        birthDate: The date of birth for the individual.

        deceasedBoolean: Indicates if the individual is deceased or not.

        deceasedDateTime: Indicates if the individual is deceased or not.

        address: An address for the individual.

        maritalStatus: This field contains a patient's most recent marital (civil) status.

        multipleBirthBoolean: Indicates whether the patient is part of a multiple (boolean) or indicates the
            actual birth order (integer).

        multipleBirthInteger: Indicates whether the patient is part of a multiple (boolean) or indicates the
            actual birth order (integer).

        photo: Image of the patient.

        contact: A contact party (e.g. guardian, partner, friend) for the patient.

        communication: A language which may be used to communicate with the patient about his or her
            health.

        generalPractitioner: Patient's nominated care provider.

        managingOrganization: Organization that is the custodian of the patient record.

        link: Link to another patient resource that concerns the same actual patient.

        """
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.narrative import (
            AutoMapperElasticSearchNarrative as NarrativeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.humanname import (
            AutoMapperElasticSearchHumanName as HumanNameSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactpoint import (
            AutoMapperElasticSearchContactPoint as ContactPointSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.address import (
            AutoMapperElasticSearchAddress as AddressSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.patient_contact import (
            AutoMapperElasticSearchPatient_Contact as Patient_ContactSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.patient_communication import (
            AutoMapperElasticSearchPatient_Communication as Patient_CommunicationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.patient_link import (
            AutoMapperElasticSearchPatient_Link as Patient_LinkSchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Patient") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Patient"]
        schema = StructType(
            [
                # This is a Patient resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An identifier for this patient.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Whether this patient record is in active use.
                # Many systems use this property to mark as non-current patients, such as those
                # that have not been seen for a period of time based on an organization's
                # business rules.
                #
                # It is often used to filter patient lists to exclude inactive patients
                #
                # Deceased patients may also be marked as inactive for the same reasons, but may
                # be active for some time after death.
                StructField("active", BooleanType(), True),
                # A name associated with the individual.
                StructField(
                    "name",
                    ArrayType(
                        HumanNameSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A contact detail (e.g. a telephone number or an email address) by which the
                # individual may be contacted.
                StructField(
                    "telecom",
                    ArrayType(
                        ContactPointSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Administrative Gender - the gender that the patient is considered to have for
                # administration and record keeping purposes.
                StructField("gender", StringType(), True),
                # The date of birth for the individual.
                StructField("birthDate", DateType(), True),
                # Indicates if the individual is deceased or not.
                StructField("deceasedBoolean", BooleanType(), True),
                # Indicates if the individual is deceased or not.
                StructField("deceasedDateTime", TimestampType(), True),
                # An address for the individual.
                StructField(
                    "address",
                    ArrayType(
                        AddressSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # This field contains a patient's most recent marital (civil) status.
                StructField(
                    "maritalStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates whether the patient is part of a multiple (boolean) or indicates the
                # actual birth order (integer).
                StructField("multipleBirthBoolean", BooleanType(), True),
                # Indicates whether the patient is part of a multiple (boolean) or indicates the
                # actual birth order (integer).
                StructField("multipleBirthInteger", IntegerType(), True),
                # Image of the patient.
                StructField(
                    "photo",
                    ArrayType(
                        AttachmentSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A contact party (e.g. guardian, partner, friend) for the patient.
                StructField(
                    "contact",
                    ArrayType(
                        Patient_ContactSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A language which may be used to communicate with the patient about his or her
                # health.
                StructField(
                    "communication",
                    ArrayType(
                        Patient_CommunicationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Patient's nominated care provider.
                StructField(
                    "generalPractitioner",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Organization that is the custodian of the patient record.
                StructField(
                    "managingOrganization",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Link to another patient resource that concerns the same actual patient.
                StructField(
                    "link",
                    ArrayType(
                        Patient_LinkSchema.schema(
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
