from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchImagingStudy_Series(AutoMapperDataTypeComplexBase):
    """
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object Pair
    Instances (SOP Instances - images or other data) acquired or produced in a
    common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        uid: Optional[Any] = None,
        number: Optional[Any] = None,
        modality: Optional[Any] = None,
        description: Optional[Any] = None,
        numberOfInstances: Optional[Any] = None,
        endpoint: Optional[Any] = None,
        bodySite: Optional[Any] = None,
        laterality: Optional[Any] = None,
        specimen: Optional[Any] = None,
        started: Optional[Any] = None,
        performer: Optional[Any] = None,
        instance: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            uid=uid,
            number=number,
            modality=modality,
            description=description,
            numberOfInstances=numberOfInstances,
            endpoint=endpoint,
            bodySite=bodySite,
            laterality=laterality,
            specimen=specimen,
            started=started,
            performer=performer,
            instance=instance,
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
        Representation of the content produced in a DICOM imaging study. A study
        comprises a set of series, each of which includes a set of Service-Object Pair
        Instances (SOP Instances - images or other data) acquired or produced in a
        common context.  A series is of only one modality (e.g. X-ray, CT, MR,
        ultrasound), but a study may have multiple series of different modalities.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        uid: The DICOM Series Instance UID for the series.

        number: The numeric identifier of this series in the study.

        modality: The modality of this series sequence.

        description: A description of the series.

        numberOfInstances: Number of SOP Instances in the Study. The value given may be larger than the
            number of instance elements this resource contains due to resource
            availability, security, or other factors. This element should be present if
            any instance elements are present.

        endpoint: The network service providing access (e.g., query, view, or retrieval) for
            this series. See implementation notes for information about using DICOM
            endpoints. A series-level endpoint, if present, has precedence over a study-
            level endpoint with the same Endpoint.connectionType.

        bodySite: The anatomic structures examined. See DICOM Part 16 Annex L (http://dicom.nema
            .org/medical/dicom/current/output/chtml/part16/chapter_L.html) for DICOM to
            SNOMED-CT mappings. The bodySite may indicate the laterality of body part
            imaged; if so, it shall be consistent with any content of
            ImagingStudy.series.laterality.

        laterality: The laterality of the (possibly paired) anatomic structures examined. E.g.,
            the left knee, both lungs, or unpaired abdomen. If present, shall be
            consistent with any laterality information indicated in
            ImagingStudy.series.bodySite.

        specimen: The specimen imaged, e.g., for whole slide imaging of a biopsy.

        started: The date and time the series was started.

        performer: Indicates who or what performed the series and how they were involved.

        instance: A single SOP instance within the series, e.g. an image, or presentation state.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.imagingstudy_performer import (
            AutoMapperElasticSearchImagingStudy_Performer as ImagingStudy_PerformerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.imagingstudy_instance import (
            AutoMapperElasticSearchImagingStudy_Instance as ImagingStudy_InstanceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ImagingStudy_Series") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImagingStudy_Series"]
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
                # The DICOM Series Instance UID for the series.
                StructField(
                    "uid",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The numeric identifier of this series in the study.
                StructField(
                    "number",
                    unsignedIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The modality of this series sequence.
                StructField(
                    "modality",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A description of the series.
                StructField("description", StringType(), True),
                # Number of SOP Instances in the Study. The value given may be larger than the
                # number of instance elements this resource contains due to resource
                # availability, security, or other factors. This element should be present if
                # any instance elements are present.
                StructField(
                    "numberOfInstances",
                    unsignedIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The network service providing access (e.g., query, view, or retrieval) for
                # this series. See implementation notes for information about using DICOM
                # endpoints. A series-level endpoint, if present, has precedence over a study-
                # level endpoint with the same Endpoint.connectionType.
                StructField(
                    "endpoint",
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
                # The anatomic structures examined. See DICOM Part 16 Annex L (http://dicom.nema
                # .org/medical/dicom/current/output/chtml/part16/chapter_L.html) for DICOM to
                # SNOMED-CT mappings. The bodySite may indicate the laterality of body part
                # imaged; if so, it shall be consistent with any content of
                # ImagingStudy.series.laterality.
                StructField(
                    "bodySite",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The laterality of the (possibly paired) anatomic structures examined. E.g.,
                # the left knee, both lungs, or unpaired abdomen. If present, shall be
                # consistent with any laterality information indicated in
                # ImagingStudy.series.bodySite.
                StructField(
                    "laterality",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The specimen imaged, e.g., for whole slide imaging of a biopsy.
                StructField(
                    "specimen",
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
                # The date and time the series was started.
                StructField(
                    "started",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates who or what performed the series and how they were involved.
                StructField(
                    "performer",
                    ArrayType(
                        ImagingStudy_PerformerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A single SOP instance within the series, e.g. an image, or presentation state.
                StructField(
                    "instance",
                    ArrayType(
                        ImagingStudy_InstanceSchema.schema(
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
