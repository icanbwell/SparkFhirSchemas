from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchDevice(AutoMapperDataTypeComplexBase):
    """
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may be a
    medical or non-medical device.
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
        definition: Optional[Any] = None,
        udiCarrier: Optional[Any] = None,
        status: Optional[Any] = None,
        statusReason: Optional[Any] = None,
        distinctIdentifier: Optional[Any] = None,
        manufacturer: Optional[Any] = None,
        manufactureDate: Optional[Any] = None,
        expirationDate: Optional[Any] = None,
        lotNumber: Optional[Any] = None,
        serialNumber: Optional[Any] = None,
        deviceName: Optional[Any] = None,
        modelNumber: Optional[Any] = None,
        partNumber: Optional[Any] = None,
        type_: Optional[Any] = None,
        specialization: Optional[Any] = None,
        version: Optional[Any] = None,
        property_: Optional[Any] = None,
        patient: Optional[Any] = None,
        owner: Optional[Any] = None,
        contact: Optional[Any] = None,
        location: Optional[Any] = None,
        url: Optional[Any] = None,
        note: Optional[Any] = None,
        safety: Optional[Any] = None,
        parent: Optional[Any] = None,
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
            definition=definition,
            udiCarrier=udiCarrier,
            status=status,
            statusReason=statusReason,
            distinctIdentifier=distinctIdentifier,
            manufacturer=manufacturer,
            manufactureDate=manufactureDate,
            expirationDate=expirationDate,
            lotNumber=lotNumber,
            serialNumber=serialNumber,
            deviceName=deviceName,
            modelNumber=modelNumber,
            partNumber=partNumber,
            type_=type_,
            specialization=specialization,
            version=version,
            property_=property_,
            patient=patient,
            owner=owner,
            contact=contact,
            location=location,
            url=url,
            note=note,
            safety=safety,
            parent=parent,
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
        A type of a manufactured item that is used in the provision of healthcare
        without being substantially changed through that activity. The device may be a
        medical or non-medical device.


        resourceType: This is a Device resource

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

        identifier: Unique instance identifiers assigned to a device by manufacturers other
            organizations or owners.

        definition: The reference to the definition for the device.

        udiCarrier: Unique device identifier (UDI) assigned to device label or package.  Note that
            the Device may include multiple udiCarriers as it either may include just the
            udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
            could have been sold.

        status: Status of the Device availability.

        statusReason: Reason for the dtatus of the Device availability.

        distinctIdentifier: The distinct identification string as required by regulation for a human cell,
            tissue, or cellular and tissue-based product.

        manufacturer: A name of the manufacturer.

        manufactureDate: The date and time when the device was manufactured.

        expirationDate: The date and time beyond which this device is no longer valid or should not be
            used (if applicable).

        lotNumber: Lot number assigned by the manufacturer.

        serialNumber: The serial number assigned by the organization when the device was
            manufactured.

        deviceName: This represents the manufacturer's name of the device as provided by the
            device, from a UDI label, or by a person describing the Device.  This
            typically would be used when a person provides the name(s) or when the device
            represents one of the names available from DeviceDefinition.

        modelNumber: The model number for the device.

        partNumber: The part number of the device.

        type: The kind or type of device.

        specialization: The capabilities supported on a  device, the standards to which the device
            conforms for a particular purpose, and used for the communication.

        version: The actual design of the device or software version running on the device.

        property: The actual configuration settings of a device as it actually operates, e.g.,
            regulation status, time properties.

        patient: Patient information, If the device is affixed to a person.

        owner: An organization that is responsible for the provision and ongoing maintenance
            of the device.

        contact: Contact details for an organization or a particular human that is responsible
            for the device.

        location: The place where the device can be found.

        url: A network address on which the device may be contacted directly.

        note: Descriptive information, usage information or implantation information that is
            not captured in an existing element.

        safety: Provides additional safety characteristics about a medical device.  For
            example devices containing latex.

        parent: The parent device.

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
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.device_udicarrier import (
            AutoMapperElasticSearchDevice_UdiCarrier as Device_UdiCarrierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.device_devicename import (
            AutoMapperElasticSearchDevice_DeviceName as Device_DeviceNameSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.device_specialization import (
            AutoMapperElasticSearchDevice_Specialization as Device_SpecializationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.device_version import (
            AutoMapperElasticSearchDevice_Version as Device_VersionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.device_property import (
            AutoMapperElasticSearchDevice_Property as Device_PropertySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactpoint import (
            AutoMapperElasticSearchContactPoint as ContactPointSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Device") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Device"]
        schema = StructType(
            [
                # This is a Device resource
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
                # Unique instance identifiers assigned to a device by manufacturers other
                # organizations or owners.
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
                # The reference to the definition for the device.
                StructField(
                    "definition",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Unique device identifier (UDI) assigned to device label or package.  Note that
                # the Device may include multiple udiCarriers as it either may include just the
                # udiCarrier for the jurisdiction it is sold, or for multiple jurisdictions it
                # could have been sold.
                StructField(
                    "udiCarrier",
                    ArrayType(
                        Device_UdiCarrierSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Status of the Device availability.
                StructField("status", StringType(), True),
                # Reason for the dtatus of the Device availability.
                StructField(
                    "statusReason",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The distinct identification string as required by regulation for a human cell,
                # tissue, or cellular and tissue-based product.
                StructField("distinctIdentifier", StringType(), True),
                # A name of the manufacturer.
                StructField("manufacturer", StringType(), True),
                # The date and time when the device was manufactured.
                StructField(
                    "manufactureDate",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date and time beyond which this device is no longer valid or should not be
                # used (if applicable).
                StructField(
                    "expirationDate",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Lot number assigned by the manufacturer.
                StructField("lotNumber", StringType(), True),
                # The serial number assigned by the organization when the device was
                # manufactured.
                StructField("serialNumber", StringType(), True),
                # This represents the manufacturer's name of the device as provided by the
                # device, from a UDI label, or by a person describing the Device.  This
                # typically would be used when a person provides the name(s) or when the device
                # represents one of the names available from DeviceDefinition.
                StructField(
                    "deviceName",
                    ArrayType(
                        Device_DeviceNameSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The model number for the device.
                StructField("modelNumber", StringType(), True),
                # The part number of the device.
                StructField("partNumber", StringType(), True),
                # The kind or type of device.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The capabilities supported on a  device, the standards to which the device
                # conforms for a particular purpose, and used for the communication.
                StructField(
                    "specialization",
                    ArrayType(
                        Device_SpecializationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The actual design of the device or software version running on the device.
                StructField(
                    "version",
                    ArrayType(
                        Device_VersionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The actual configuration settings of a device as it actually operates, e.g.,
                # regulation status, time properties.
                StructField(
                    "property",
                    ArrayType(
                        Device_PropertySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Patient information, If the device is affixed to a person.
                StructField(
                    "patient",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An organization that is responsible for the provision and ongoing maintenance
                # of the device.
                StructField(
                    "owner",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Contact details for an organization or a particular human that is responsible
                # for the device.
                StructField(
                    "contact",
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
                # The place where the device can be found.
                StructField(
                    "location",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A network address on which the device may be contacted directly.
                StructField(
                    "url",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Descriptive information, usage information or implantation information that is
                # not captured in an existing element.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Provides additional safety characteristics about a medical device.  For
                # example devices containing latex.
                StructField(
                    "safety",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The parent device.
                StructField(
                    "parent",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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
