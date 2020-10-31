from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Media:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A photo, video, or audio recording acquired or used in healthcare. The actual
        content may be inline or provided by direct reference.


        resourceType: This is a Media resource

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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: Identifiers associated with the image - these may include identifiers for the
            image itself, identifiers for the context of its collection (e.g. series ids)
            and context ids such as accession numbers or other workflow identifiers.

        basedOn: A procedure that is fulfilled in whole or in part by the creation of this
            media.

        partOf: A larger event of which this particular event is a component or step.

        status: The current state of the {{title}}.

        type: A code that classifies whether the media is an image, video or audio recording
            or some other media category.

        modality: Details of the type of the media - usually, how it was acquired (what type of
            device). If images sourced from a DICOM system, are wrapped in a Media
            resource, then this is the modality.

        view: The name of the imaging view e.g. Lateral or Antero-posterior (AP).

        subject: Who/What this Media is a record of.

        encounter: The encounter that establishes the context for this media.

        createdDateTime: The date and time(s) at which the media was collected.

        createdPeriod: The date and time(s) at which the media was collected.

        issued: The date and time this version of the media was made available to providers,
            typically after having been reviewed.

        operator: The person who administered the collection of the image.

        reasonCode: Describes why the event occurred in coded or textual form.

        bodySite: Indicates the site on the subject's body where the observation was made (i.e.
            the target site).

        deviceName: The name of the device / manufacturer of the device  that was used to make the
            recording.

        device: The device used to collect the media.

        height: Height of the image in pixels (photo/video).

        width: Width of the image in pixels (photo/video).

        frames: The number of frames in a photo. This is used with a multi-page fax, or an
            imaging acquisition context that takes multiple slices in a single image, or
            an animated gif. If there is more than one frame, this SHALL have a value in
            order to alert interface software that a multi-frame capable rendering widget
            is required.

        duration: The duration of the recording in seconds - for audio and video.

        content: The actual content of the media - inline or by direct reference to the media
            source file.

        note: Comments made about the media by the performer, subject or other participants.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Media resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Identifiers associated with the image - these may include identifiers for the
                # image itself, identifiers for the context of its collection (e.g. series ids)
                # and context ids such as accession numbers or other workflow identifiers.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # A procedure that is fulfilled in whole or in part by the creation of this
                # media.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A larger event of which this particular event is a component or step.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The current state of the {{title}}.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # A code that classifies whether the media is an image, video or audio recording
                # or some other media category.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Details of the type of the media - usually, how it was acquired (what type of
                # device). If images sourced from a DICOM system, are wrapped in a Media
                # resource, then this is the modality.
                StructField(
                    "modality",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The name of the imaging view e.g. Lateral or Antero-posterior (AP).
                StructField(
                    "view", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Who/What this Media is a record of.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The encounter that establishes the context for this media.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The date and time(s) at which the media was collected.
                StructField("createdDateTime", StringType(), True),
                # The date and time(s) at which the media was collected.
                StructField(
                    "createdPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date and time this version of the media was made available to providers,
                # typically after having been reviewed.
                StructField(
                    "issued", instant.get_schema(recursion_depth + 1), True
                ),
                # The person who administered the collection of the image.
                StructField(
                    "operator", Reference.get_schema(recursion_depth + 1), True
                ),
                # Describes why the event occurred in coded or textual form.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates the site on the subject's body where the observation was made (i.e.
                # the target site).
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The name of the device / manufacturer of the device  that was used to make the
                # recording.
                StructField("deviceName", StringType(), True),
                # The device used to collect the media.
                StructField(
                    "device", Reference.get_schema(recursion_depth + 1), True
                ),
                # Height of the image in pixels (photo/video).
                StructField(
                    "height", positiveInt.get_schema(recursion_depth + 1), True
                ),
                # Width of the image in pixels (photo/video).
                StructField(
                    "width", positiveInt.get_schema(recursion_depth + 1), True
                ),
                # The number of frames in a photo. This is used with a multi-page fax, or an
                # imaging acquisition context that takes multiple slices in a single image, or
                # an animated gif. If there is more than one frame, this SHALL have a value in
                # order to alert interface software that a multi-frame capable rendering widget
                # is required.
                StructField(
                    "frames", positiveInt.get_schema(recursion_depth + 1), True
                ),
                # The duration of the recording in seconds - for audio and video.
                StructField(
                    "duration", decimal.get_schema(recursion_depth + 1), True
                ),
                # The actual content of the media - inline or by direct reference to the media
                # source file.
                StructField(
                    "content", Attachment.get_schema(recursion_depth + 1), True
                ),
                # Comments made about the media by the performer, subject or other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
