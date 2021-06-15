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
    FloatType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchElementDefinition(AutoMapperDataTypeComplexBase):
    """
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        path: Optional[Any] = None,
        representation: Optional[Any] = None,
        sliceName: Optional[Any] = None,
        sliceIsConstraining: Optional[Any] = None,
        label: Optional[Any] = None,
        code: Optional[Any] = None,
        slicing: Optional[Any] = None,
        short: Optional[Any] = None,
        definition: Optional[Any] = None,
        comment: Optional[Any] = None,
        requirements: Optional[Any] = None,
        alias: Optional[Any] = None,
        min_: Optional[Any] = None,
        max_: Optional[Any] = None,
        base: Optional[Any] = None,
        contentReference: Optional[Any] = None,
        type_: Optional[Any] = None,
        defaultValueBase64Binary: Optional[Any] = None,
        defaultValueBoolean: Optional[Any] = None,
        defaultValueCanonical: Optional[Any] = None,
        defaultValueCode: Optional[Any] = None,
        defaultValueDate: Optional[Any] = None,
        defaultValueDateTime: Optional[Any] = None,
        defaultValueDecimal: Optional[Any] = None,
        defaultValueId: Optional[Any] = None,
        defaultValueInstant: Optional[Any] = None,
        defaultValueInteger: Optional[Any] = None,
        defaultValueMarkdown: Optional[Any] = None,
        defaultValueOid: Optional[Any] = None,
        defaultValuePositiveInt: Optional[Any] = None,
        defaultValueString: Optional[Any] = None,
        defaultValueTime: Optional[Any] = None,
        defaultValueUnsignedInt: Optional[Any] = None,
        defaultValueUri: Optional[Any] = None,
        defaultValueUrl: Optional[Any] = None,
        defaultValueUuid: Optional[Any] = None,
        defaultValueAddress: Optional[Any] = None,
        defaultValueAge: Optional[Any] = None,
        defaultValueAnnotation: Optional[Any] = None,
        defaultValueAttachment: Optional[Any] = None,
        defaultValueCodeableConcept: Optional[Any] = None,
        defaultValueCoding: Optional[Any] = None,
        defaultValueContactPoint: Optional[Any] = None,
        defaultValueCount: Optional[Any] = None,
        defaultValueDistance: Optional[Any] = None,
        defaultValueDuration: Optional[Any] = None,
        defaultValueHumanName: Optional[Any] = None,
        defaultValueIdentifier: Optional[Any] = None,
        defaultValueMoney: Optional[Any] = None,
        defaultValuePeriod: Optional[Any] = None,
        defaultValueQuantity: Optional[Any] = None,
        defaultValueRange: Optional[Any] = None,
        defaultValueRatio: Optional[Any] = None,
        defaultValueReference: Optional[Any] = None,
        defaultValueSampledData: Optional[Any] = None,
        defaultValueSignature: Optional[Any] = None,
        defaultValueTiming: Optional[Any] = None,
        defaultValueContactDetail: Optional[Any] = None,
        defaultValueContributor: Optional[Any] = None,
        defaultValueDataRequirement: Optional[Any] = None,
        defaultValueExpression: Optional[Any] = None,
        defaultValueParameterDefinition: Optional[Any] = None,
        defaultValueRelatedArtifact: Optional[Any] = None,
        defaultValueTriggerDefinition: Optional[Any] = None,
        defaultValueUsageContext: Optional[Any] = None,
        defaultValueDosage: Optional[Any] = None,
        defaultValueMeta: Optional[Any] = None,
        meaningWhenMissing: Optional[Any] = None,
        orderMeaning: Optional[Any] = None,
        fixedBase64Binary: Optional[Any] = None,
        fixedBoolean: Optional[Any] = None,
        fixedCanonical: Optional[Any] = None,
        fixedCode: Optional[Any] = None,
        fixedDate: Optional[Any] = None,
        fixedDateTime: Optional[Any] = None,
        fixedDecimal: Optional[Any] = None,
        fixedId: Optional[Any] = None,
        fixedInstant: Optional[Any] = None,
        fixedInteger: Optional[Any] = None,
        fixedMarkdown: Optional[Any] = None,
        fixedOid: Optional[Any] = None,
        fixedPositiveInt: Optional[Any] = None,
        fixedString: Optional[Any] = None,
        fixedTime: Optional[Any] = None,
        fixedUnsignedInt: Optional[Any] = None,
        fixedUri: Optional[Any] = None,
        fixedUrl: Optional[Any] = None,
        fixedUuid: Optional[Any] = None,
        fixedAddress: Optional[Any] = None,
        fixedAge: Optional[Any] = None,
        fixedAnnotation: Optional[Any] = None,
        fixedAttachment: Optional[Any] = None,
        fixedCodeableConcept: Optional[Any] = None,
        fixedCoding: Optional[Any] = None,
        fixedContactPoint: Optional[Any] = None,
        fixedCount: Optional[Any] = None,
        fixedDistance: Optional[Any] = None,
        fixedDuration: Optional[Any] = None,
        fixedHumanName: Optional[Any] = None,
        fixedIdentifier: Optional[Any] = None,
        fixedMoney: Optional[Any] = None,
        fixedPeriod: Optional[Any] = None,
        fixedQuantity: Optional[Any] = None,
        fixedRange: Optional[Any] = None,
        fixedRatio: Optional[Any] = None,
        fixedReference: Optional[Any] = None,
        fixedSampledData: Optional[Any] = None,
        fixedSignature: Optional[Any] = None,
        fixedTiming: Optional[Any] = None,
        fixedContactDetail: Optional[Any] = None,
        fixedContributor: Optional[Any] = None,
        fixedDataRequirement: Optional[Any] = None,
        fixedExpression: Optional[Any] = None,
        fixedParameterDefinition: Optional[Any] = None,
        fixedRelatedArtifact: Optional[Any] = None,
        fixedTriggerDefinition: Optional[Any] = None,
        fixedUsageContext: Optional[Any] = None,
        fixedDosage: Optional[Any] = None,
        fixedMeta: Optional[Any] = None,
        patternBase64Binary: Optional[Any] = None,
        patternBoolean: Optional[Any] = None,
        patternCanonical: Optional[Any] = None,
        patternCode: Optional[Any] = None,
        patternDate: Optional[Any] = None,
        patternDateTime: Optional[Any] = None,
        patternDecimal: Optional[Any] = None,
        patternId: Optional[Any] = None,
        patternInstant: Optional[Any] = None,
        patternInteger: Optional[Any] = None,
        patternMarkdown: Optional[Any] = None,
        patternOid: Optional[Any] = None,
        patternPositiveInt: Optional[Any] = None,
        patternString: Optional[Any] = None,
        patternTime: Optional[Any] = None,
        patternUnsignedInt: Optional[Any] = None,
        patternUri: Optional[Any] = None,
        patternUrl: Optional[Any] = None,
        patternUuid: Optional[Any] = None,
        patternAddress: Optional[Any] = None,
        patternAge: Optional[Any] = None,
        patternAnnotation: Optional[Any] = None,
        patternAttachment: Optional[Any] = None,
        patternCodeableConcept: Optional[Any] = None,
        patternCoding: Optional[Any] = None,
        patternContactPoint: Optional[Any] = None,
        patternCount: Optional[Any] = None,
        patternDistance: Optional[Any] = None,
        patternDuration: Optional[Any] = None,
        patternHumanName: Optional[Any] = None,
        patternIdentifier: Optional[Any] = None,
        patternMoney: Optional[Any] = None,
        patternPeriod: Optional[Any] = None,
        patternQuantity: Optional[Any] = None,
        patternRange: Optional[Any] = None,
        patternRatio: Optional[Any] = None,
        patternReference: Optional[Any] = None,
        patternSampledData: Optional[Any] = None,
        patternSignature: Optional[Any] = None,
        patternTiming: Optional[Any] = None,
        patternContactDetail: Optional[Any] = None,
        patternContributor: Optional[Any] = None,
        patternDataRequirement: Optional[Any] = None,
        patternExpression: Optional[Any] = None,
        patternParameterDefinition: Optional[Any] = None,
        patternRelatedArtifact: Optional[Any] = None,
        patternTriggerDefinition: Optional[Any] = None,
        patternUsageContext: Optional[Any] = None,
        patternDosage: Optional[Any] = None,
        patternMeta: Optional[Any] = None,
        example: Optional[Any] = None,
        minValueDate: Optional[Any] = None,
        minValueDateTime: Optional[Any] = None,
        minValueInstant: Optional[Any] = None,
        minValueTime: Optional[Any] = None,
        minValueDecimal: Optional[Any] = None,
        minValueInteger: Optional[Any] = None,
        minValuePositiveInt: Optional[Any] = None,
        minValueUnsignedInt: Optional[Any] = None,
        minValueQuantity: Optional[Any] = None,
        maxValueDate: Optional[Any] = None,
        maxValueDateTime: Optional[Any] = None,
        maxValueInstant: Optional[Any] = None,
        maxValueTime: Optional[Any] = None,
        maxValueDecimal: Optional[Any] = None,
        maxValueInteger: Optional[Any] = None,
        maxValuePositiveInt: Optional[Any] = None,
        maxValueUnsignedInt: Optional[Any] = None,
        maxValueQuantity: Optional[Any] = None,
        maxLength: Optional[Any] = None,
        condition: Optional[Any] = None,
        constraint: Optional[Any] = None,
        mustSupport: Optional[Any] = None,
        isModifier: Optional[Any] = None,
        isModifierReason: Optional[Any] = None,
        isSummary: Optional[Any] = None,
        binding: Optional[Any] = None,
        mapping: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            representation=representation,
            sliceName=sliceName,
            sliceIsConstraining=sliceIsConstraining,
            label=label,
            code=code,
            slicing=slicing,
            short=short,
            definition=definition,
            comment=comment,
            requirements=requirements,
            alias=alias,
            min_=min_,
            max_=max_,
            base=base,
            contentReference=contentReference,
            type_=type_,
            defaultValueBase64Binary=defaultValueBase64Binary,
            defaultValueBoolean=defaultValueBoolean,
            defaultValueCanonical=defaultValueCanonical,
            defaultValueCode=defaultValueCode,
            defaultValueDate=defaultValueDate,
            defaultValueDateTime=defaultValueDateTime,
            defaultValueDecimal=defaultValueDecimal,
            defaultValueId=defaultValueId,
            defaultValueInstant=defaultValueInstant,
            defaultValueInteger=defaultValueInteger,
            defaultValueMarkdown=defaultValueMarkdown,
            defaultValueOid=defaultValueOid,
            defaultValuePositiveInt=defaultValuePositiveInt,
            defaultValueString=defaultValueString,
            defaultValueTime=defaultValueTime,
            defaultValueUnsignedInt=defaultValueUnsignedInt,
            defaultValueUri=defaultValueUri,
            defaultValueUrl=defaultValueUrl,
            defaultValueUuid=defaultValueUuid,
            defaultValueAddress=defaultValueAddress,
            defaultValueAge=defaultValueAge,
            defaultValueAnnotation=defaultValueAnnotation,
            defaultValueAttachment=defaultValueAttachment,
            defaultValueCodeableConcept=defaultValueCodeableConcept,
            defaultValueCoding=defaultValueCoding,
            defaultValueContactPoint=defaultValueContactPoint,
            defaultValueCount=defaultValueCount,
            defaultValueDistance=defaultValueDistance,
            defaultValueDuration=defaultValueDuration,
            defaultValueHumanName=defaultValueHumanName,
            defaultValueIdentifier=defaultValueIdentifier,
            defaultValueMoney=defaultValueMoney,
            defaultValuePeriod=defaultValuePeriod,
            defaultValueQuantity=defaultValueQuantity,
            defaultValueRange=defaultValueRange,
            defaultValueRatio=defaultValueRatio,
            defaultValueReference=defaultValueReference,
            defaultValueSampledData=defaultValueSampledData,
            defaultValueSignature=defaultValueSignature,
            defaultValueTiming=defaultValueTiming,
            defaultValueContactDetail=defaultValueContactDetail,
            defaultValueContributor=defaultValueContributor,
            defaultValueDataRequirement=defaultValueDataRequirement,
            defaultValueExpression=defaultValueExpression,
            defaultValueParameterDefinition=defaultValueParameterDefinition,
            defaultValueRelatedArtifact=defaultValueRelatedArtifact,
            defaultValueTriggerDefinition=defaultValueTriggerDefinition,
            defaultValueUsageContext=defaultValueUsageContext,
            defaultValueDosage=defaultValueDosage,
            defaultValueMeta=defaultValueMeta,
            meaningWhenMissing=meaningWhenMissing,
            orderMeaning=orderMeaning,
            fixedBase64Binary=fixedBase64Binary,
            fixedBoolean=fixedBoolean,
            fixedCanonical=fixedCanonical,
            fixedCode=fixedCode,
            fixedDate=fixedDate,
            fixedDateTime=fixedDateTime,
            fixedDecimal=fixedDecimal,
            fixedId=fixedId,
            fixedInstant=fixedInstant,
            fixedInteger=fixedInteger,
            fixedMarkdown=fixedMarkdown,
            fixedOid=fixedOid,
            fixedPositiveInt=fixedPositiveInt,
            fixedString=fixedString,
            fixedTime=fixedTime,
            fixedUnsignedInt=fixedUnsignedInt,
            fixedUri=fixedUri,
            fixedUrl=fixedUrl,
            fixedUuid=fixedUuid,
            fixedAddress=fixedAddress,
            fixedAge=fixedAge,
            fixedAnnotation=fixedAnnotation,
            fixedAttachment=fixedAttachment,
            fixedCodeableConcept=fixedCodeableConcept,
            fixedCoding=fixedCoding,
            fixedContactPoint=fixedContactPoint,
            fixedCount=fixedCount,
            fixedDistance=fixedDistance,
            fixedDuration=fixedDuration,
            fixedHumanName=fixedHumanName,
            fixedIdentifier=fixedIdentifier,
            fixedMoney=fixedMoney,
            fixedPeriod=fixedPeriod,
            fixedQuantity=fixedQuantity,
            fixedRange=fixedRange,
            fixedRatio=fixedRatio,
            fixedReference=fixedReference,
            fixedSampledData=fixedSampledData,
            fixedSignature=fixedSignature,
            fixedTiming=fixedTiming,
            fixedContactDetail=fixedContactDetail,
            fixedContributor=fixedContributor,
            fixedDataRequirement=fixedDataRequirement,
            fixedExpression=fixedExpression,
            fixedParameterDefinition=fixedParameterDefinition,
            fixedRelatedArtifact=fixedRelatedArtifact,
            fixedTriggerDefinition=fixedTriggerDefinition,
            fixedUsageContext=fixedUsageContext,
            fixedDosage=fixedDosage,
            fixedMeta=fixedMeta,
            patternBase64Binary=patternBase64Binary,
            patternBoolean=patternBoolean,
            patternCanonical=patternCanonical,
            patternCode=patternCode,
            patternDate=patternDate,
            patternDateTime=patternDateTime,
            patternDecimal=patternDecimal,
            patternId=patternId,
            patternInstant=patternInstant,
            patternInteger=patternInteger,
            patternMarkdown=patternMarkdown,
            patternOid=patternOid,
            patternPositiveInt=patternPositiveInt,
            patternString=patternString,
            patternTime=patternTime,
            patternUnsignedInt=patternUnsignedInt,
            patternUri=patternUri,
            patternUrl=patternUrl,
            patternUuid=patternUuid,
            patternAddress=patternAddress,
            patternAge=patternAge,
            patternAnnotation=patternAnnotation,
            patternAttachment=patternAttachment,
            patternCodeableConcept=patternCodeableConcept,
            patternCoding=patternCoding,
            patternContactPoint=patternContactPoint,
            patternCount=patternCount,
            patternDistance=patternDistance,
            patternDuration=patternDuration,
            patternHumanName=patternHumanName,
            patternIdentifier=patternIdentifier,
            patternMoney=patternMoney,
            patternPeriod=patternPeriod,
            patternQuantity=patternQuantity,
            patternRange=patternRange,
            patternRatio=patternRatio,
            patternReference=patternReference,
            patternSampledData=patternSampledData,
            patternSignature=patternSignature,
            patternTiming=patternTiming,
            patternContactDetail=patternContactDetail,
            patternContributor=patternContributor,
            patternDataRequirement=patternDataRequirement,
            patternExpression=patternExpression,
            patternParameterDefinition=patternParameterDefinition,
            patternRelatedArtifact=patternRelatedArtifact,
            patternTriggerDefinition=patternTriggerDefinition,
            patternUsageContext=patternUsageContext,
            patternDosage=patternDosage,
            patternMeta=patternMeta,
            example=example,
            minValueDate=minValueDate,
            minValueDateTime=minValueDateTime,
            minValueInstant=minValueInstant,
            minValueTime=minValueTime,
            minValueDecimal=minValueDecimal,
            minValueInteger=minValueInteger,
            minValuePositiveInt=minValuePositiveInt,
            minValueUnsignedInt=minValueUnsignedInt,
            minValueQuantity=minValueQuantity,
            maxValueDate=maxValueDate,
            maxValueDateTime=maxValueDateTime,
            maxValueInstant=maxValueInstant,
            maxValueTime=maxValueTime,
            maxValueDecimal=maxValueDecimal,
            maxValueInteger=maxValueInteger,
            maxValuePositiveInt=maxValuePositiveInt,
            maxValueUnsignedInt=maxValueUnsignedInt,
            maxValueQuantity=maxValueQuantity,
            maxLength=maxLength,
            condition=condition,
            constraint=constraint,
            mustSupport=mustSupport,
            isModifier=isModifier,
            isModifierReason=isModifierReason,
            isSummary=isSummary,
            binding=binding,
            mapping=mapping,
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
        Captures constraints on each element within the resource, profile, or
        extension.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        path: The path identifies the element and is expressed as a "."-separated list of
            ancestor elements, beginning with the name of the resource or extension.

        representation: Codes that define how this element is represented in instances, when the
            deviation varies from the normal case.

        sliceName: The name of this element definition slice, when slicing is working. The name
            must be a token with no dots or spaces. This is a unique name referring to a
            specific set of constraints applied to this element, used to provide a name to
            different slices of the same element.

        sliceIsConstraining: If true, indicates that this slice definition is constraining a slice
            definition with the same name in an inherited profile. If false, the slice is
            not overriding any slice in an inherited profile. If missing, the slice might
            or might not be overriding a slice in an inherited profile, depending on the
            sliceName.

        label: A single preferred label which is the text to display beside the element
            indicating its meaning or to use to prompt for the element in a user display
            or form.

        code: A code that has the same meaning as the element in a particular terminology.

        slicing: Indicates that the element is sliced into a set of alternative definitions
            (i.e. in a structure definition, there are multiple different constraints on a
            single element in the base resource). Slicing can be used in any resource that
            has cardinality ..* on the base resource, or any resource with a choice of
            types. The set of slices is any elements that come after this in the element
            sequence that have the same path, until a shorter path occurs (the shorter
            path terminates the set).

        short: A concise description of what this element means (e.g. for use in
            autogenerated summaries).

        definition: Provides a complete explanation of the meaning of the data element for human
            readability.  For the case of elements derived from existing elements (e.g.
            constraints), the definition SHALL be consistent with the base definition, but
            convey the meaning of the element in the particular context of use of the
            resource. (Note: The text you are reading is specified in
            ElementDefinition.definition).

        comment: Explanatory notes and implementation guidance about the data element,
            including notes about how to use the data properly, exceptions to proper use,
            etc. (Note: The text you are reading is specified in
            ElementDefinition.comment).

        requirements: This element is for traceability of why the element was created and why the
            constraints exist as they do. This may be used to point to source materials or
            specifications that drove the structure of this element.

        alias: Identifies additional names by which this element might also be known.

        min: The minimum number of times this element SHALL appear in the instance.

        max: The maximum number of times this element is permitted to appear in the
            instance.

        base: Information about the base definition of the element, provided to make it
            unnecessary for tools to trace the deviation of the element through the
            derived and related profiles. When the element definition is not the original
            definition of an element - i.g. either in a constraint on another type, or for
            elements from a super type in a snap shot - then the information in provided
            in the element definition may be different to the base definition. On the
            original definition of the element, it will be same.

        contentReference: Identifies an element defined elsewhere in the definition whose content rules
            should be applied to the current element. ContentReferences bring across all
            the rules that are in the ElementDefinition for the element, including
            definitions, cardinality constraints, bindings, invariants etc.

        type: The data type or resource that the value of this element is permitted to be.

        defaultValueBase64Binary: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueBoolean: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueCanonical: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueCode: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDate: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDateTime: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDecimal: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueId: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueInstant: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueInteger: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueMarkdown: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueOid: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValuePositiveInt: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueString: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueTime: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueUnsignedInt: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueUri: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueUrl: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueUuid: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueAddress: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueAge: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueAnnotation: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueAttachment: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueCodeableConcept: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueCoding: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueContactPoint: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueCount: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDistance: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDuration: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueHumanName: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueIdentifier: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueMoney: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValuePeriod: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueQuantity: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueRange: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueRatio: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueReference: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueSampledData: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueSignature: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueTiming: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueContactDetail: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueContributor: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDataRequirement: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueExpression: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueParameterDefinition: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueRelatedArtifact: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueTriggerDefinition: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueUsageContext: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueDosage: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        defaultValueMeta: The value that should be used if there is no value stated in the instance
            (e.g. 'if not otherwise specified, the abstract is false').

        meaningWhenMissing: The Implicit meaning that is to be understood when this element is missing
            (e.g. 'when this element is missing, the period is ongoing').

        orderMeaning: If present, indicates that the order of the repeating element has meaning and
            describes what that meaning is.  If absent, it means that the order of the
            element has no meaning.

        fixedBase64Binary: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedBoolean: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedCanonical: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedCode: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDate: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDateTime: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDecimal: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedId: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedInstant: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedInteger: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedMarkdown: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedOid: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedPositiveInt: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedString: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedTime: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedUnsignedInt: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedUri: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedUrl: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedUuid: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedAddress: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedAge: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedAnnotation: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedAttachment: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedCodeableConcept: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedCoding: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedContactPoint: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedCount: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDistance: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDuration: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedHumanName: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedIdentifier: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedMoney: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedPeriod: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedQuantity: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedRange: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedRatio: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedReference: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedSampledData: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedSignature: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedTiming: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedContactDetail: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedContributor: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDataRequirement: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedExpression: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedParameterDefinition: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedRelatedArtifact: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedTriggerDefinition: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedUsageContext: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedDosage: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        fixedMeta: Specifies a value that SHALL be exactly the value  for this element in the
            instance. For purposes of comparison, non-significant whitespace is ignored,
            and all values must be an exact match (case and accent sensitive). Missing
            elements/attributes must also be missing.

        patternBase64Binary: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternBoolean: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternCanonical: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternCode: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDate: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDateTime: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDecimal: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternId: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternInstant: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternInteger: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternMarkdown: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternOid: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternPositiveInt: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternString: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternTime: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternUnsignedInt: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternUri: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternUrl: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternUuid: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternAddress: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternAge: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternAnnotation: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternAttachment: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternCodeableConcept: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternCoding: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternContactPoint: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternCount: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDistance: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDuration: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternHumanName: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternIdentifier: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternMoney: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternPeriod: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternQuantity: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternRange: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternRatio: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternReference: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternSampledData: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternSignature: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternTiming: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternContactDetail: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternContributor: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDataRequirement: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternExpression: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternParameterDefinition: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternRelatedArtifact: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternTriggerDefinition: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternUsageContext: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternDosage: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        patternMeta: Specifies a value that the value in the instance SHALL follow - that is, any
            value in the pattern must be found in the instance. Other additional values
            may be found too. This is effectively constraint by example.

            When pattern[x] is used to constrain a primitive, it means that the value
            provided in the pattern[x] must match the instance value exactly.

            When pattern[x] is used to constrain an array, it means that each element
            provided in the pattern[x] array must (recursively) match at least one element
            from the instance array.

            When pattern[x] is used to constrain a complex object, it means that each
            property in the pattern must be present in the complex object, and its value
            must recursively match -- i.e.,

            1. If primitive: it must match exactly the pattern value
            2. If a complex object: it must match (recursively) the pattern value
            3. If an array: it must match (recursively) the pattern value.

        example: A sample value for this element demonstrating the type of information that
            would typically be found in the element.

        minValueDate: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueDateTime: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueInstant: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueTime: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueDecimal: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueInteger: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValuePositiveInt: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueUnsignedInt: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        minValueQuantity: The minimum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueDate: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueDateTime: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueInstant: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueTime: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueDecimal: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueInteger: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValuePositiveInt: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueUnsignedInt: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxValueQuantity: The maximum allowed value for the element. The value is inclusive. This is
            allowed for the types date, dateTime, instant, time, decimal, integer, and
            Quantity.

        maxLength: Indicates the maximum length in characters that is permitted to be present in
            conformant instances and which is expected to be supported by conformant
            consumers that support the element.

        condition: A reference to an invariant that may make additional statements about the
            cardinality or value in the instance.

        constraint: Formal constraints such as co-occurrence and other constraints that can be
            computationally evaluated within the context of the instance.

        mustSupport: If true, implementations that produce or consume resources SHALL provide
            "support" for the element in some meaningful way.  If false, the element may
            be ignored and not supported. If false, whether to populate or use the data
            element in any way is at the discretion of the implementation.

        isModifier: If true, the value of this element affects the interpretation of the element
            or resource that contains it, and the value of the element cannot be ignored.
            Typically, this is used for status, negation and qualification codes. The
            effect of this is that the element cannot be ignored by systems: they SHALL
            either recognize the element and process it, and/or a pre-determination has
            been made that it is not relevant to their particular system.

        isModifierReason: Explains how that element affects the interpretation of the resource or
            element that contains it.

        isSummary: Whether the element should be included if a client requests a search with the
            parameter _summary=true.

        binding: Binds to a value set if this element is coded (code, Coding, CodeableConcept,
            Quantity), or the data types (string, uri).

        mapping: Identifies a concept from an external specification that roughly corresponds
            to this element.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_slicing import (
            AutoMapperElasticSearchElementDefinition_Slicing as ElementDefinition_SlicingSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_base import (
            AutoMapperElasticSearchElementDefinition_Base as ElementDefinition_BaseSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_type import (
            AutoMapperElasticSearchElementDefinition_Type as ElementDefinition_TypeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.address import (
            AutoMapperElasticSearchAddress as AddressSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactpoint import (
            AutoMapperElasticSearchContactPoint as ContactPointSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.count import (
            AutoMapperElasticSearchCount as CountSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.distance import (
            AutoMapperElasticSearchDistance as DistanceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.humanname import (
            AutoMapperElasticSearchHumanName as HumanNameSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.money import (
            AutoMapperElasticSearchMoney as MoneySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.sampleddata import (
            AutoMapperElasticSearchSampledData as SampledDataSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.signature import (
            AutoMapperElasticSearchSignature as SignatureSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactdetail import (
            AutoMapperElasticSearchContactDetail as ContactDetailSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contributor import (
            AutoMapperElasticSearchContributor as ContributorSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.datarequirement import (
            AutoMapperElasticSearchDataRequirement as DataRequirementSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.expression import (
            AutoMapperElasticSearchExpression as ExpressionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.parameterdefinition import (
            AutoMapperElasticSearchParameterDefinition as ParameterDefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.relatedartifact import (
            AutoMapperElasticSearchRelatedArtifact as RelatedArtifactSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.triggerdefinition import (
            AutoMapperElasticSearchTriggerDefinition as TriggerDefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.usagecontext import (
            AutoMapperElasticSearchUsageContext as UsageContextSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.dosage import (
            AutoMapperElasticSearchDosage as DosageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_example import (
            AutoMapperElasticSearchElementDefinition_Example as ElementDefinition_ExampleSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_constraint import (
            AutoMapperElasticSearchElementDefinition_Constraint as ElementDefinition_ConstraintSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_binding import (
            AutoMapperElasticSearchElementDefinition_Binding as ElementDefinition_BindingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_mapping import (
            AutoMapperElasticSearchElementDefinition_Mapping as ElementDefinition_MappingSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ElementDefinition"]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
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
                # The path identifies the element and is expressed as a "."-separated list of
                # ancestor elements, beginning with the name of the resource or extension.
                StructField("path", StringType(), True),
                # Codes that define how this element is represented in instances, when the
                # deviation varies from the normal case.
                # The name of this element definition slice, when slicing is working. The name
                # must be a token with no dots or spaces. This is a unique name referring to a
                # specific set of constraints applied to this element, used to provide a name to
                # different slices of the same element.
                StructField("sliceName", StringType(), True),
                # If true, indicates that this slice definition is constraining a slice
                # definition with the same name in an inherited profile. If false, the slice is
                # not overriding any slice in an inherited profile. If missing, the slice might
                # or might not be overriding a slice in an inherited profile, depending on the
                # sliceName.
                StructField("sliceIsConstraining", BooleanType(), True),
                # A single preferred label which is the text to display beside the element
                # indicating its meaning or to use to prompt for the element in a user display
                # or form.
                StructField("label", StringType(), True),
                # A code that has the same meaning as the element in a particular terminology.
                StructField(
                    "code",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates that the element is sliced into a set of alternative definitions
                # (i.e. in a structure definition, there are multiple different constraints on a
                # single element in the base resource). Slicing can be used in any resource that
                # has cardinality ..* on the base resource, or any resource with a choice of
                # types. The set of slices is any elements that come after this in the element
                # sequence that have the same path, until a shorter path occurs (the shorter
                # path terminates the set).
                StructField(
                    "slicing",
                    ElementDefinition_SlicingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A concise description of what this element means (e.g. for use in
                # autogenerated summaries).
                StructField("short", StringType(), True),
                # Provides a complete explanation of the meaning of the data element for human
                # readability.  For the case of elements derived from existing elements (e.g.
                # constraints), the definition SHALL be consistent with the base definition, but
                # convey the meaning of the element in the particular context of use of the
                # resource. (Note: The text you are reading is specified in
                # ElementDefinition.definition).
                StructField(
                    "definition",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Explanatory notes and implementation guidance about the data element,
                # including notes about how to use the data properly, exceptions to proper use,
                # etc. (Note: The text you are reading is specified in
                # ElementDefinition.comment).
                StructField(
                    "comment",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # This element is for traceability of why the element was created and why the
                # constraints exist as they do. This may be used to point to source materials or
                # specifications that drove the structure of this element.
                StructField(
                    "requirements",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies additional names by which this element might also be known.
                StructField("alias", ArrayType(StringType()), True),
                # The minimum number of times this element SHALL appear in the instance.
                StructField(
                    "min",
                    unsignedIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The maximum number of times this element is permitted to appear in the
                # instance.
                StructField("max", StringType(), True),
                # Information about the base definition of the element, provided to make it
                # unnecessary for tools to trace the deviation of the element through the
                # derived and related profiles. When the element definition is not the original
                # definition of an element - i.g. either in a constraint on another type, or for
                # elements from a super type in a snap shot - then the information in provided
                # in the element definition may be different to the base definition. On the
                # original definition of the element, it will be same.
                StructField(
                    "base",
                    ElementDefinition_BaseSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies an element defined elsewhere in the definition whose content rules
                # should be applied to the current element. ContentReferences bring across all
                # the rules that are in the ElementDefinition for the element, including
                # definitions, cardinality constraints, bindings, invariants etc.
                StructField(
                    "contentReference",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The data type or resource that the value of this element is permitted to be.
                StructField(
                    "type",
                    ArrayType(
                        ElementDefinition_TypeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueBase64Binary", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueBoolean", BooleanType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueCanonical", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueCode", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueDate", DateType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueDateTime", TimestampType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueDecimal", FloatType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueId", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueInstant", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueInteger", IntegerType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueMarkdown", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueOid", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValuePositiveInt", IntegerType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueString", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueTime", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueUnsignedInt", IntegerType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueUri", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueUrl", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField("defaultValueUuid", StringType(), True),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueAddress",
                    AddressSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueAnnotation",
                    AnnotationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueContactPoint",
                    ContactPointSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueCount",
                    CountSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueDistance",
                    DistanceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueHumanName",
                    HumanNameSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueMoney",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValuePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueSampledData",
                    SampledDataSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueSignature",
                    SignatureSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueContactDetail",
                    ContactDetailSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueContributor",
                    ContributorSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueDataRequirement",
                    DataRequirementSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueExpression",
                    ExpressionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueParameterDefinition",
                    ParameterDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueRelatedArtifact",
                    RelatedArtifactSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueTriggerDefinition",
                    TriggerDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueUsageContext",
                    UsageContextSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueDosage",
                    DosageSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value that should be used if there is no value stated in the instance
                # (e.g. 'if not otherwise specified, the abstract is false').
                StructField(
                    "defaultValueMeta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The Implicit meaning that is to be understood when this element is missing
                # (e.g. 'when this element is missing, the period is ongoing').
                StructField(
                    "meaningWhenMissing",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If present, indicates that the order of the repeating element has meaning and
                # describes what that meaning is.  If absent, it means that the order of the
                # element has no meaning.
                StructField("orderMeaning", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedBase64Binary", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedBoolean", BooleanType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedCanonical", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedCode", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedDate", DateType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedDateTime", TimestampType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedDecimal", FloatType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedId", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedInstant", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedInteger", IntegerType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedMarkdown", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedOid", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedPositiveInt", IntegerType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedString", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedTime", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedUnsignedInt", IntegerType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedUri", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedUrl", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField("fixedUuid", StringType(), True),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedAddress",
                    AddressSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedAnnotation",
                    AnnotationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedContactPoint",
                    ContactPointSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedCount",
                    CountSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedDistance",
                    DistanceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedHumanName",
                    HumanNameSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedMoney",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedSampledData",
                    SampledDataSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedSignature",
                    SignatureSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedContactDetail",
                    ContactDetailSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedContributor",
                    ContributorSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedDataRequirement",
                    DataRequirementSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedExpression",
                    ExpressionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedParameterDefinition",
                    ParameterDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedRelatedArtifact",
                    RelatedArtifactSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedTriggerDefinition",
                    TriggerDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedUsageContext",
                    UsageContextSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedDosage",
                    DosageSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that SHALL be exactly the value  for this element in the
                # instance. For purposes of comparison, non-significant whitespace is ignored,
                # and all values must be an exact match (case and accent sensitive). Missing
                # elements/attributes must also be missing.
                StructField(
                    "fixedMeta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternBase64Binary", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternBoolean", BooleanType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternCanonical", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternCode", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternDate", DateType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternDateTime", TimestampType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternDecimal", FloatType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternId", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternInstant", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternInteger", IntegerType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternMarkdown", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternOid", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternPositiveInt", IntegerType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternString", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternTime", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternUnsignedInt", IntegerType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternUri", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternUrl", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField("patternUuid", StringType(), True),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternAddress",
                    AddressSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternAnnotation",
                    AnnotationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternContactPoint",
                    ContactPointSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternCount",
                    CountSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternDistance",
                    DistanceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternHumanName",
                    HumanNameSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternMoney",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternSampledData",
                    SampledDataSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternSignature",
                    SignatureSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternContactDetail",
                    ContactDetailSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternContributor",
                    ContributorSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternDataRequirement",
                    DataRequirementSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternExpression",
                    ExpressionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternParameterDefinition",
                    ParameterDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternRelatedArtifact",
                    RelatedArtifactSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternTriggerDefinition",
                    TriggerDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternUsageContext",
                    UsageContextSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternDosage",
                    DosageSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies a value that the value in the instance SHALL follow - that is, any
                # value in the pattern must be found in the instance. Other additional values
                # may be found too. This is effectively constraint by example.
                #
                # When pattern[x] is used to constrain a primitive, it means that the value
                # provided in the pattern[x] must match the instance value exactly.
                #
                # When pattern[x] is used to constrain an array, it means that each element
                # provided in the pattern[x] array must (recursively) match at least one element
                # from the instance array.
                #
                # When pattern[x] is used to constrain a complex object, it means that each
                # property in the pattern must be present in the complex object, and its value
                # must recursively match -- i.e.,
                #
                # 1. If primitive: it must match exactly the pattern value
                # 2. If a complex object: it must match (recursively) the pattern value
                # 3. If an array: it must match (recursively) the pattern value.
                StructField(
                    "patternMeta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A sample value for this element demonstrating the type of information that
                # would typically be found in the element.
                StructField(
                    "example",
                    ArrayType(
                        ElementDefinition_ExampleSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueDate", DateType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueDateTime", TimestampType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueInstant", StringType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueTime", StringType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueDecimal", FloatType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueInteger", IntegerType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValuePositiveInt", IntegerType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("minValueUnsignedInt", IntegerType(), True),
                # The minimum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField(
                    "minValueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueDate", DateType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueDateTime", TimestampType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueInstant", StringType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueTime", StringType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueDecimal", FloatType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueInteger", IntegerType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValuePositiveInt", IntegerType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField("maxValueUnsignedInt", IntegerType(), True),
                # The maximum allowed value for the element. The value is inclusive. This is
                # allowed for the types date, dateTime, instant, time, decimal, integer, and
                # Quantity.
                StructField(
                    "maxValueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the maximum length in characters that is permitted to be present in
                # conformant instances and which is expected to be supported by conformant
                # consumers that support the element.
                StructField(
                    "maxLength",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to an invariant that may make additional statements about the
                # cardinality or value in the instance.
                StructField(
                    "condition",
                    ArrayType(
                        idSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Formal constraints such as co-occurrence and other constraints that can be
                # computationally evaluated within the context of the instance.
                StructField(
                    "constraint",
                    ArrayType(
                        ElementDefinition_ConstraintSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # If true, implementations that produce or consume resources SHALL provide
                # "support" for the element in some meaningful way.  If false, the element may
                # be ignored and not supported. If false, whether to populate or use the data
                # element in any way is at the discretion of the implementation.
                StructField("mustSupport", BooleanType(), True),
                # If true, the value of this element affects the interpretation of the element
                # or resource that contains it, and the value of the element cannot be ignored.
                # Typically, this is used for status, negation and qualification codes. The
                # effect of this is that the element cannot be ignored by systems: they SHALL
                # either recognize the element and process it, and/or a pre-determination has
                # been made that it is not relevant to their particular system.
                StructField("isModifier", BooleanType(), True),
                # Explains how that element affects the interpretation of the resource or
                # element that contains it.
                StructField("isModifierReason", StringType(), True),
                # Whether the element should be included if a client requests a search with the
                # parameter _summary=true.
                StructField("isSummary", BooleanType(), True),
                # Binds to a value set if this element is coded (code, Coding, CodeableConcept,
                # Quantity), or the data types (string, uri).
                StructField(
                    "binding",
                    ElementDefinition_BindingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies a concept from an external specification that roughly corresponds
                # to this element.
                StructField(
                    "mapping",
                    ArrayType(
                        ElementDefinition_MappingSchema.schema(
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
