from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicationKnowledge(AutoMapperDataTypeComplexBase):
    """
    Information about a medication that is used to support knowledge.
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
        code: Optional[Any] = None,
        status: Optional[Any] = None,
        manufacturer: Optional[Any] = None,
        doseForm: Optional[Any] = None,
        amount: Optional[Any] = None,
        synonym: Optional[Any] = None,
        relatedMedicationKnowledge: Optional[Any] = None,
        associatedMedication: Optional[Any] = None,
        productType: Optional[Any] = None,
        monograph: Optional[Any] = None,
        ingredient: Optional[Any] = None,
        preparationInstruction: Optional[Any] = None,
        intendedRoute: Optional[Any] = None,
        cost: Optional[Any] = None,
        monitoringProgram: Optional[Any] = None,
        administrationGuidelines: Optional[Any] = None,
        medicineClassification: Optional[Any] = None,
        packaging: Optional[Any] = None,
        drugCharacteristic: Optional[Any] = None,
        contraindication: Optional[Any] = None,
        regulatory: Optional[Any] = None,
        kinetics: Optional[Any] = None,
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
            code=code,
            status=status,
            manufacturer=manufacturer,
            doseForm=doseForm,
            amount=amount,
            synonym=synonym,
            relatedMedicationKnowledge=relatedMedicationKnowledge,
            associatedMedication=associatedMedication,
            productType=productType,
            monograph=monograph,
            ingredient=ingredient,
            preparationInstruction=preparationInstruction,
            intendedRoute=intendedRoute,
            cost=cost,
            monitoringProgram=monitoringProgram,
            administrationGuidelines=administrationGuidelines,
            medicineClassification=medicineClassification,
            packaging=packaging,
            drugCharacteristic=drugCharacteristic,
            contraindication=contraindication,
            regulatory=regulatory,
            kinetics=kinetics,
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
        Information about a medication that is used to support knowledge.


        resourceType: This is a MedicationKnowledge resource

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

        code: A code that specifies this medication, or a textual description if no code is
            available. Usage note: This could be a standard medication code such as a code
            from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local
            formulary code, optionally with translations to other code systems.

        status: A code to indicate if the medication is in active use.  The status refers to
            the validity about the information of the medication and not to its medicinal
            properties.

        manufacturer: Describes the details of the manufacturer of the medication product.  This is
            not intended to represent the distributor of a medication product.

        doseForm: Describes the form of the item.  Powder; tablets; capsule.

        amount: Specific amount of the drug in the packaged product.  For example, when
            specifying a product that has the same strength (For example, Insulin glargine
            100 unit per mL solution for injection), this attribute provides additional
            clarification of the package amount (For example, 3 mL, 10mL, etc.).

        synonym: Additional names for a medication, for example, the name(s) given to a
            medication in different countries.  For example, acetaminophen and paracetamol
            or salbutamol and albuterol.

        relatedMedicationKnowledge: Associated or related knowledge about a medication.

        associatedMedication: Associated or related medications.  For example, if the medication is a
            branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g.
            Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this
            would link to a branded product (e.g. Crestor).

        productType: Category of the medication or product (e.g. branded product, therapeutic
            moeity, generic product, innovator product, etc.).

        monograph: Associated documentation about the medication.

        ingredient: Identifies a particular constituent of interest in the product.

        preparationInstruction: The instructions for preparing the medication.

        intendedRoute: The intended or approved route of administration.

        cost: The price of the medication.

        monitoringProgram: The program under which the medication is reviewed.

        administrationGuidelines: Guidelines for the administration of the medication.

        medicineClassification: Categorization of the medication within a formulary or classification system.

        packaging: Information that only applies to packages (not products).

        drugCharacteristic: Specifies descriptive properties of the medicine, such as color, shape,
            imprints, etc.

        contraindication: Potential clinical issue with or between medication(s) (for example, drug-drug
            interaction, drug-disease contraindication, drug-allergy interaction, etc.).

        regulatory: Regulatory information about a medication.

        kinetics: The time course of drug absorption, distribution, metabolism and excretion of
            a medication from the body.

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
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_relatedmedicationknowledge import (
            AutoMapperElasticSearchMedicationKnowledge_RelatedMedicationKnowledge as MedicationKnowledge_RelatedMedicationKnowledgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_monograph import (
            AutoMapperElasticSearchMedicationKnowledge_Monograph as MedicationKnowledge_MonographSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_ingredient import (
            AutoMapperElasticSearchMedicationKnowledge_Ingredient as MedicationKnowledge_IngredientSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_cost import (
            AutoMapperElasticSearchMedicationKnowledge_Cost as MedicationKnowledge_CostSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_monitoringprogram import (
            AutoMapperElasticSearchMedicationKnowledge_MonitoringProgram as MedicationKnowledge_MonitoringProgramSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_administrationguidelines import (
            AutoMapperElasticSearchMedicationKnowledge_AdministrationGuidelines as MedicationKnowledge_AdministrationGuidelinesSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_medicineclassification import (
            AutoMapperElasticSearchMedicationKnowledge_MedicineClassification as MedicationKnowledge_MedicineClassificationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_packaging import (
            AutoMapperElasticSearchMedicationKnowledge_Packaging as MedicationKnowledge_PackagingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_drugcharacteristic import (
            AutoMapperElasticSearchMedicationKnowledge_DrugCharacteristic as MedicationKnowledge_DrugCharacteristicSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_regulatory import (
            AutoMapperElasticSearchMedicationKnowledge_Regulatory as MedicationKnowledge_RegulatorySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationknowledge_kinetics import (
            AutoMapperElasticSearchMedicationKnowledge_Kinetics as MedicationKnowledge_KineticsSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MedicationKnowledge") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationKnowledge"]
        schema = StructType(
            [
                # This is a MedicationKnowledge resource
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
                # A code that specifies this medication, or a textual description if no code is
                # available. Usage note: This could be a standard medication code such as a code
                # from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local
                # formulary code, optionally with translations to other code systems.
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
                # A code to indicate if the medication is in active use.  The status refers to
                # the validity about the information of the medication and not to its medicinal
                # properties.
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
                # Describes the details of the manufacturer of the medication product.  This is
                # not intended to represent the distributor of a medication product.
                StructField(
                    "manufacturer",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Describes the form of the item.  Powder; tablets; capsule.
                StructField(
                    "doseForm",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specific amount of the drug in the packaged product.  For example, when
                # specifying a product that has the same strength (For example, Insulin glargine
                # 100 unit per mL solution for injection), this attribute provides additional
                # clarification of the package amount (For example, 3 mL, 10mL, etc.).
                StructField(
                    "amount",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional names for a medication, for example, the name(s) given to a
                # medication in different countries.  For example, acetaminophen and paracetamol
                # or salbutamol and albuterol.
                StructField("synonym", ArrayType(StringType()), True),
                # Associated or related knowledge about a medication.
                StructField(
                    "relatedMedicationKnowledge",
                    ArrayType(
                        MedicationKnowledge_RelatedMedicationKnowledgeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Associated or related medications.  For example, if the medication is a
                # branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g.
                # Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this
                # would link to a branded product (e.g. Crestor).
                StructField(
                    "associatedMedication",
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
                # Category of the medication or product (e.g. branded product, therapeutic
                # moeity, generic product, innovator product, etc.).
                StructField(
                    "productType",
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
                # Associated documentation about the medication.
                StructField(
                    "monograph",
                    ArrayType(
                        MedicationKnowledge_MonographSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Identifies a particular constituent of interest in the product.
                StructField(
                    "ingredient",
                    ArrayType(
                        MedicationKnowledge_IngredientSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The instructions for preparing the medication.
                StructField(
                    "preparationInstruction",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The intended or approved route of administration.
                StructField(
                    "intendedRoute",
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
                # The price of the medication.
                StructField(
                    "cost",
                    ArrayType(
                        MedicationKnowledge_CostSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The program under which the medication is reviewed.
                StructField(
                    "monitoringProgram",
                    ArrayType(
                        MedicationKnowledge_MonitoringProgramSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Guidelines for the administration of the medication.
                StructField(
                    "administrationGuidelines",
                    ArrayType(
                        MedicationKnowledge_AdministrationGuidelinesSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Categorization of the medication within a formulary or classification system.
                StructField(
                    "medicineClassification",
                    ArrayType(
                        MedicationKnowledge_MedicineClassificationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Information that only applies to packages (not products).
                StructField(
                    "packaging",
                    MedicationKnowledge_PackagingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies descriptive properties of the medicine, such as color, shape,
                # imprints, etc.
                StructField(
                    "drugCharacteristic",
                    ArrayType(
                        MedicationKnowledge_DrugCharacteristicSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Potential clinical issue with or between medication(s) (for example, drug-drug
                # interaction, drug-disease contraindication, drug-allergy interaction, etc.).
                StructField(
                    "contraindication",
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
                # Regulatory information about a medication.
                StructField(
                    "regulatory",
                    ArrayType(
                        MedicationKnowledge_RegulatorySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The time course of drug absorption, distribution, metabolism and excretion of
                # a medication from the body.
                StructField(
                    "kinetics",
                    ArrayType(
                        MedicationKnowledge_KineticsSchema.schema(
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