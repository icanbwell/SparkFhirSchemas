from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchProcedure(AutoMapperDataTypeComplexBase):
    """
    An action that is or was performed on or for a patient. This can be a physical
    intervention like an operation, or less invasive like long term services,
    counseling, or hypnotherapy.
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
        instantiatesCanonical: Optional[Any] = None,
        instantiatesUri: Optional[Any] = None,
        basedOn: Optional[Any] = None,
        partOf: Optional[Any] = None,
        status: Optional[Any] = None,
        statusReason: Optional[Any] = None,
        category: Optional[Any] = None,
        code: Optional[Any] = None,
        subject: Optional[Any] = None,
        encounter: Optional[Any] = None,
        performedDateTime: Optional[Any] = None,
        performedPeriod: Optional[Any] = None,
        performedString: Optional[Any] = None,
        performedAge: Optional[Any] = None,
        performedRange: Optional[Any] = None,
        recorder: Optional[Any] = None,
        asserter: Optional[Any] = None,
        performer: Optional[Any] = None,
        location: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        bodySite: Optional[Any] = None,
        outcome: Optional[Any] = None,
        report: Optional[Any] = None,
        complication: Optional[Any] = None,
        complicationDetail: Optional[Any] = None,
        followUp: Optional[Any] = None,
        note: Optional[Any] = None,
        focalDevice: Optional[Any] = None,
        usedReference: Optional[Any] = None,
        usedCode: Optional[Any] = None,
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
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            category=category,
            code=code,
            subject=subject,
            encounter=encounter,
            performedDateTime=performedDateTime,
            performedPeriod=performedPeriod,
            performedString=performedString,
            performedAge=performedAge,
            performedRange=performedRange,
            recorder=recorder,
            asserter=asserter,
            performer=performer,
            location=location,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            bodySite=bodySite,
            outcome=outcome,
            report=report,
            complication=complication,
            complicationDetail=complicationDetail,
            followUp=followUp,
            note=note,
            focalDevice=focalDevice,
            usedReference=usedReference,
            usedCode=usedCode,
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
        An action that is or was performed on or for a patient. This can be a physical
        intervention like an operation, or less invasive like long term services,
        counseling, or hypnotherapy.


        resourceType: This is a Procedure resource

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

        identifier: Business identifiers assigned to this procedure by the performer or other
            systems which remain constant as the resource is updated and is propagated
            from server to server.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, order set or other
            definition that is adhered to in whole or in part by this Procedure.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, order set or
            other definition that is adhered to in whole or in part by this Procedure.

        basedOn: A reference to a resource that contains details of the request for this
            procedure.

        partOf: A larger event of which this particular procedure is a component or step.

        status: A code specifying the state of the procedure. Generally, this will be the in-
            progress or completed state.

        statusReason: Captures the reason for the current state of the procedure.

        category: A code that classifies the procedure for searching, sorting and display
            purposes (e.g. "Surgical Procedure").

        code: The specific procedure that is performed. Use text if the exact nature of the
            procedure cannot be coded (e.g. "Laparoscopic Appendectomy").

        subject: The person, animal or group on which the procedure was performed.

        encounter: The Encounter during which this Procedure was created or performed or to which
            the creation of this record is tightly associated.

        performedDateTime: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedPeriod: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedString: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedAge: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        performedRange: Estimated or actual date, date-time, period, or age when the procedure was
            performed.  Allows a period to support complex procedures that span more than
            one date, and also allows for the length of the procedure to be captured.

        recorder: Individual who recorded the record and takes responsibility for its content.

        asserter: Individual who is making the procedure statement.

        performer: Limited to "real" people rather than equipment.

        location: The location where the procedure actually happened.  E.g. a newborn at home, a
            tracheostomy at a restaurant.

        reasonCode: The coded reason why the procedure was performed. This may be a coded entity
            of some type, or may simply be present as text.

        reasonReference: The justification of why the procedure was performed.

        bodySite: Detailed and structured anatomical location information. Multiple locations
            are allowed - e.g. multiple punch biopsies of a lesion.

        outcome: The outcome of the procedure - did it resolve the reasons for the procedure
            being performed?

        report: This could be a histology result, pathology report, surgical report, etc.

        complication: Any complications that occurred during the procedure, or in the immediate
            post-performance period. These are generally tracked separately from the
            notes, which will typically describe the procedure itself rather than any
            'post procedure' issues.

        complicationDetail: Any complications that occurred during the procedure, or in the immediate
            post-performance period.

        followUp: If the procedure required specific follow up - e.g. removal of sutures. The
            follow up may be represented as a simple note or could potentially be more
            complex, in which case the CarePlan resource can be used.

        note: Any other notes and comments about the procedure.

        focalDevice: A device that is implanted, removed or otherwise manipulated (calibration,
            battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a
            focal portion of the Procedure.

        usedReference: Identifies medications, devices and any other substance used as part of the
            procedure.

        usedCode: Identifies coded items that were used as part of the procedure.

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
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.procedure_performer import (
            AutoMapperElasticSearchProcedure_Performer as Procedure_PerformerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.procedure_focaldevice import (
            AutoMapperElasticSearchProcedure_FocalDevice as Procedure_FocalDeviceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Procedure") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Procedure"]
        schema = StructType(
            [
                # This is a Procedure resource
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
                # Business identifiers assigned to this procedure by the performer or other
                # systems which remain constant as the resource is updated and is propagated
                # from server to server.
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
                # The URL pointing to a FHIR-defined protocol, guideline, order set or other
                # definition that is adhered to in whole or in part by this Procedure.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(
                        canonicalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The URL pointing to an externally maintained protocol, guideline, order set or
                # other definition that is adhered to in whole or in part by this Procedure.
                StructField(
                    "instantiatesUri",
                    ArrayType(
                        uriSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A reference to a resource that contains details of the request for this
                # procedure.
                StructField(
                    "basedOn",
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
                # A larger event of which this particular procedure is a component or step.
                StructField(
                    "partOf",
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
                # A code specifying the state of the procedure. Generally, this will be the in-
                # progress or completed state.
                StructField(
                    "status",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Captures the reason for the current state of the procedure.
                StructField(
                    "statusReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code that classifies the procedure for searching, sorting and display
                # purposes (e.g. "Surgical Procedure").
                StructField(
                    "category",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The specific procedure that is performed. Use text if the exact nature of the
                # procedure cannot be coded (e.g. "Laparoscopic Appendectomy").
                StructField(
                    "code",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The person, animal or group on which the procedure was performed.
                StructField(
                    "subject",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The Encounter during which this Procedure was created or performed or to which
                # the creation of this record is tightly associated.
                StructField(
                    "encounter",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField("performedDateTime", TimestampType(), True),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField(
                    "performedPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField("performedString", StringType(), True),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField(
                    "performedAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date, date-time, period, or age when the procedure was
                # performed.  Allows a period to support complex procedures that span more than
                # one date, and also allows for the length of the procedure to be captured.
                StructField(
                    "performedRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Individual who recorded the record and takes responsibility for its content.
                StructField(
                    "recorder",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Individual who is making the procedure statement.
                StructField(
                    "asserter",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Limited to "real" people rather than equipment.
                StructField(
                    "performer",
                    ArrayType(
                        Procedure_PerformerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The location where the procedure actually happened.  E.g. a newborn at home, a
                # tracheostomy at a restaurant.
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
                # The coded reason why the procedure was performed. This may be a coded entity
                # of some type, or may simply be present as text.
                StructField(
                    "reasonCode",
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
                # The justification of why the procedure was performed.
                StructField(
                    "reasonReference",
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
                # Detailed and structured anatomical location information. Multiple locations
                # are allowed - e.g. multiple punch biopsies of a lesion.
                StructField(
                    "bodySite",
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
                # The outcome of the procedure - did it resolve the reasons for the procedure
                # being performed?
                StructField(
                    "outcome",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # This could be a histology result, pathology report, surgical report, etc.
                StructField(
                    "report",
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
                # Any complications that occurred during the procedure, or in the immediate
                # post-performance period. These are generally tracked separately from the
                # notes, which will typically describe the procedure itself rather than any
                # 'post procedure' issues.
                StructField(
                    "complication",
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
                # Any complications that occurred during the procedure, or in the immediate
                # post-performance period.
                StructField(
                    "complicationDetail",
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
                # If the procedure required specific follow up - e.g. removal of sutures. The
                # follow up may be represented as a simple note or could potentially be more
                # complex, in which case the CarePlan resource can be used.
                StructField(
                    "followUp",
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
                # Any other notes and comments about the procedure.
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
                # A device that is implanted, removed or otherwise manipulated (calibration,
                # battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a
                # focal portion of the Procedure.
                StructField(
                    "focalDevice",
                    ArrayType(
                        Procedure_FocalDeviceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Identifies medications, devices and any other substance used as part of the
                # procedure.
                StructField(
                    "usedReference",
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
                # Identifies coded items that were used as part of the procedure.
                StructField(
                    "usedCode",
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