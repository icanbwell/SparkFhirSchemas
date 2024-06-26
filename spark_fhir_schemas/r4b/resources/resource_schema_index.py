from typing import Any


class ResourceSchemaIndex:
    @staticmethod
    def get(resource_type: str) -> Any:
        if resource_type is None:
            raise Exception("Invalid resource type")
        elif resource_type == "Account":
            from spark_fhir_schemas.r4b.resources.account import AccountSchema

            return AccountSchema
        elif resource_type == "ActivityDefinition":
            from spark_fhir_schemas.r4b.resources.activitydefinition import (
                ActivityDefinitionSchema,
            )

            return ActivityDefinitionSchema
        elif resource_type == "AdministrableProductDefinition":
            from spark_fhir_schemas.r4b.resources.administrableproductdefinition import (
                AdministrableProductDefinitionSchema,
            )

            return AdministrableProductDefinitionSchema
        elif resource_type == "AdverseEvent":
            from spark_fhir_schemas.r4b.resources.adverseevent import AdverseEventSchema

            return AdverseEventSchema
        elif resource_type == "AllergyIntolerance":
            from spark_fhir_schemas.r4b.resources.allergyintolerance import (
                AllergyIntoleranceSchema,
            )

            return AllergyIntoleranceSchema
        elif resource_type == "Appointment":
            from spark_fhir_schemas.r4b.resources.appointment import AppointmentSchema

            return AppointmentSchema
        elif resource_type == "AppointmentResponse":
            from spark_fhir_schemas.r4b.resources.appointmentresponse import (
                AppointmentResponseSchema,
            )

            return AppointmentResponseSchema
        elif resource_type == "AuditEvent":
            from spark_fhir_schemas.r4b.resources.auditevent import AuditEventSchema

            return AuditEventSchema
        elif resource_type == "Basic":
            from spark_fhir_schemas.r4b.resources.basic import BasicSchema

            return BasicSchema
        elif resource_type == "Binary":
            from spark_fhir_schemas.r4b.resources.binary import BinarySchema

            return BinarySchema
        elif resource_type == "BiologicallyDerivedProduct":
            from spark_fhir_schemas.r4b.resources.biologicallyderivedproduct import (
                BiologicallyDerivedProductSchema,
            )

            return BiologicallyDerivedProductSchema
        elif resource_type == "BodyStructure":
            from spark_fhir_schemas.r4b.resources.bodystructure import (
                BodyStructureSchema,
            )

            return BodyStructureSchema
        elif resource_type == "Bundle":
            from spark_fhir_schemas.r4b.resources.bundle import BundleSchema

            return BundleSchema
        elif resource_type == "CapabilityStatement":
            from spark_fhir_schemas.r4b.resources.capabilitystatement import (
                CapabilityStatementSchema,
            )

            return CapabilityStatementSchema
        elif resource_type == "CarePlan":
            from spark_fhir_schemas.r4b.resources.careplan import CarePlanSchema

            return CarePlanSchema
        elif resource_type == "CareTeam":
            from spark_fhir_schemas.r4b.resources.careteam import CareTeamSchema

            return CareTeamSchema
        elif resource_type == "CatalogEntry":
            from spark_fhir_schemas.r4b.resources.catalogentry import CatalogEntrySchema

            return CatalogEntrySchema
        elif resource_type == "ChargeItem":
            from spark_fhir_schemas.r4b.resources.chargeitem import ChargeItemSchema

            return ChargeItemSchema
        elif resource_type == "ChargeItemDefinition":
            from spark_fhir_schemas.r4b.resources.chargeitemdefinition import (
                ChargeItemDefinitionSchema,
            )

            return ChargeItemDefinitionSchema
        elif resource_type == "Citation":
            from spark_fhir_schemas.r4b.resources.citation import CitationSchema

            return CitationSchema
        elif resource_type == "Claim":
            from spark_fhir_schemas.r4b.resources.claim import ClaimSchema

            return ClaimSchema
        elif resource_type == "ClaimResponse":
            from spark_fhir_schemas.r4b.resources.claimresponse import (
                ClaimResponseSchema,
            )

            return ClaimResponseSchema
        elif resource_type == "ClinicalImpression":
            from spark_fhir_schemas.r4b.resources.clinicalimpression import (
                ClinicalImpressionSchema,
            )

            return ClinicalImpressionSchema
        elif resource_type == "ClinicalUseDefinition":
            from spark_fhir_schemas.r4b.resources.clinicalusedefinition import (
                ClinicalUseDefinitionSchema,
            )

            return ClinicalUseDefinitionSchema
        elif resource_type == "CodeSystem":
            from spark_fhir_schemas.r4b.resources.codesystem import CodeSystemSchema

            return CodeSystemSchema
        elif resource_type == "Communication":
            from spark_fhir_schemas.r4b.resources.communication import (
                CommunicationSchema,
            )

            return CommunicationSchema
        elif resource_type == "CommunicationRequest":
            from spark_fhir_schemas.r4b.resources.communicationrequest import (
                CommunicationRequestSchema,
            )

            return CommunicationRequestSchema
        elif resource_type == "CompartmentDefinition":
            from spark_fhir_schemas.r4b.resources.compartmentdefinition import (
                CompartmentDefinitionSchema,
            )

            return CompartmentDefinitionSchema
        elif resource_type == "Composition":
            from spark_fhir_schemas.r4b.resources.composition import CompositionSchema

            return CompositionSchema
        elif resource_type == "ConceptMap":
            from spark_fhir_schemas.r4b.resources.conceptmap import ConceptMapSchema

            return ConceptMapSchema
        elif resource_type == "Condition":
            from spark_fhir_schemas.r4b.resources.condition import ConditionSchema

            return ConditionSchema
        elif resource_type == "Consent":
            from spark_fhir_schemas.r4b.resources.consent import ConsentSchema

            return ConsentSchema
        elif resource_type == "Contract":
            from spark_fhir_schemas.r4b.resources.contract import ContractSchema

            return ContractSchema
        elif resource_type == "Coverage":
            from spark_fhir_schemas.r4b.resources.coverage import CoverageSchema

            return CoverageSchema
        elif resource_type == "CoverageEligibilityRequest":
            from spark_fhir_schemas.r4b.resources.coverageeligibilityrequest import (
                CoverageEligibilityRequestSchema,
            )

            return CoverageEligibilityRequestSchema
        elif resource_type == "CoverageEligibilityResponse":
            from spark_fhir_schemas.r4b.resources.coverageeligibilityresponse import (
                CoverageEligibilityResponseSchema,
            )

            return CoverageEligibilityResponseSchema
        elif resource_type == "DetectedIssue":
            from spark_fhir_schemas.r4b.resources.detectedissue import (
                DetectedIssueSchema,
            )

            return DetectedIssueSchema
        elif resource_type == "Device":
            from spark_fhir_schemas.r4b.resources.device import DeviceSchema

            return DeviceSchema
        elif resource_type == "DeviceDefinition":
            from spark_fhir_schemas.r4b.resources.devicedefinition import (
                DeviceDefinitionSchema,
            )

            return DeviceDefinitionSchema
        elif resource_type == "DeviceMetric":
            from spark_fhir_schemas.r4b.resources.devicemetric import DeviceMetricSchema

            return DeviceMetricSchema
        elif resource_type == "DeviceRequest":
            from spark_fhir_schemas.r4b.resources.devicerequest import (
                DeviceRequestSchema,
            )

            return DeviceRequestSchema
        elif resource_type == "DeviceUseStatement":
            from spark_fhir_schemas.r4b.resources.deviceusestatement import (
                DeviceUseStatementSchema,
            )

            return DeviceUseStatementSchema
        elif resource_type == "DiagnosticReport":
            from spark_fhir_schemas.r4b.resources.diagnosticreport import (
                DiagnosticReportSchema,
            )

            return DiagnosticReportSchema
        elif resource_type == "DocumentManifest":
            from spark_fhir_schemas.r4b.resources.documentmanifest import (
                DocumentManifestSchema,
            )

            return DocumentManifestSchema
        elif resource_type == "DocumentReference":
            from spark_fhir_schemas.r4b.resources.documentreference import (
                DocumentReferenceSchema,
            )

            return DocumentReferenceSchema
        elif resource_type == "Encounter":
            from spark_fhir_schemas.r4b.resources.encounter import EncounterSchema

            return EncounterSchema
        elif resource_type == "Endpoint":
            from spark_fhir_schemas.r4b.resources.endpoint import EndpointSchema

            return EndpointSchema
        elif resource_type == "EnrollmentRequest":
            from spark_fhir_schemas.r4b.resources.enrollmentrequest import (
                EnrollmentRequestSchema,
            )

            return EnrollmentRequestSchema
        elif resource_type == "EnrollmentResponse":
            from spark_fhir_schemas.r4b.resources.enrollmentresponse import (
                EnrollmentResponseSchema,
            )

            return EnrollmentResponseSchema
        elif resource_type == "EpisodeOfCare":
            from spark_fhir_schemas.r4b.resources.episodeofcare import (
                EpisodeOfCareSchema,
            )

            return EpisodeOfCareSchema
        elif resource_type == "EventDefinition":
            from spark_fhir_schemas.r4b.resources.eventdefinition import (
                EventDefinitionSchema,
            )

            return EventDefinitionSchema
        elif resource_type == "Evidence":
            from spark_fhir_schemas.r4b.resources.evidence import EvidenceSchema

            return EvidenceSchema
        elif resource_type == "EvidenceReport":
            from spark_fhir_schemas.r4b.resources.evidencereport import (
                EvidenceReportSchema,
            )

            return EvidenceReportSchema
        elif resource_type == "EvidenceVariable":
            from spark_fhir_schemas.r4b.resources.evidencevariable import (
                EvidenceVariableSchema,
            )

            return EvidenceVariableSchema
        elif resource_type == "ExampleScenario":
            from spark_fhir_schemas.r4b.resources.examplescenario import (
                ExampleScenarioSchema,
            )

            return ExampleScenarioSchema
        elif resource_type == "ExplanationOfBenefit":
            from spark_fhir_schemas.r4b.resources.explanationofbenefit import (
                ExplanationOfBenefitSchema,
            )

            return ExplanationOfBenefitSchema
        elif resource_type == "FamilyMemberHistory":
            from spark_fhir_schemas.r4b.resources.familymemberhistory import (
                FamilyMemberHistorySchema,
            )

            return FamilyMemberHistorySchema
        elif resource_type == "Flag":
            from spark_fhir_schemas.r4b.resources.flag import FlagSchema

            return FlagSchema
        elif resource_type == "Goal":
            from spark_fhir_schemas.r4b.resources.goal import GoalSchema

            return GoalSchema
        elif resource_type == "GraphDefinition":
            from spark_fhir_schemas.r4b.resources.graphdefinition import (
                GraphDefinitionSchema,
            )

            return GraphDefinitionSchema
        elif resource_type == "Group":
            from spark_fhir_schemas.r4b.resources.group import GroupSchema

            return GroupSchema
        elif resource_type == "GuidanceResponse":
            from spark_fhir_schemas.r4b.resources.guidanceresponse import (
                GuidanceResponseSchema,
            )

            return GuidanceResponseSchema
        elif resource_type == "HealthcareService":
            from spark_fhir_schemas.r4b.resources.healthcareservice import (
                HealthcareServiceSchema,
            )

            return HealthcareServiceSchema
        elif resource_type == "ImagingStudy":
            from spark_fhir_schemas.r4b.resources.imagingstudy import ImagingStudySchema

            return ImagingStudySchema
        elif resource_type == "Immunization":
            from spark_fhir_schemas.r4b.resources.immunization import ImmunizationSchema

            return ImmunizationSchema
        elif resource_type == "ImmunizationEvaluation":
            from spark_fhir_schemas.r4b.resources.immunizationevaluation import (
                ImmunizationEvaluationSchema,
            )

            return ImmunizationEvaluationSchema
        elif resource_type == "ImmunizationRecommendation":
            from spark_fhir_schemas.r4b.resources.immunizationrecommendation import (
                ImmunizationRecommendationSchema,
            )

            return ImmunizationRecommendationSchema
        elif resource_type == "ImplementationGuide":
            from spark_fhir_schemas.r4b.resources.implementationguide import (
                ImplementationGuideSchema,
            )

            return ImplementationGuideSchema
        elif resource_type == "Ingredient":
            from spark_fhir_schemas.r4b.resources.ingredient import IngredientSchema

            return IngredientSchema
        elif resource_type == "InsurancePlan":
            from spark_fhir_schemas.r4b.resources.insuranceplan import (
                InsurancePlanSchema,
            )

            return InsurancePlanSchema
        elif resource_type == "Invoice":
            from spark_fhir_schemas.r4b.resources.invoice import InvoiceSchema

            return InvoiceSchema
        elif resource_type == "Library":
            from spark_fhir_schemas.r4b.resources.library import LibrarySchema

            return LibrarySchema
        elif resource_type == "Linkage":
            from spark_fhir_schemas.r4b.resources.linkage import LinkageSchema

            return LinkageSchema
        elif resource_type == "List":
            from spark_fhir_schemas.r4b.resources.list import ListSchema

            return ListSchema
        elif resource_type == "Location":
            from spark_fhir_schemas.r4b.resources.location import LocationSchema

            return LocationSchema
        elif resource_type == "ManufacturedItemDefinition":
            from spark_fhir_schemas.r4b.resources.manufactureditemdefinition import (
                ManufacturedItemDefinitionSchema,
            )

            return ManufacturedItemDefinitionSchema
        elif resource_type == "Measure":
            from spark_fhir_schemas.r4b.resources.measure import MeasureSchema

            return MeasureSchema
        elif resource_type == "MeasureReport":
            from spark_fhir_schemas.r4b.resources.measurereport import (
                MeasureReportSchema,
            )

            return MeasureReportSchema
        elif resource_type == "Media":
            from spark_fhir_schemas.r4b.resources.media import MediaSchema

            return MediaSchema
        elif resource_type == "Medication":
            from spark_fhir_schemas.r4b.resources.medication import MedicationSchema

            return MedicationSchema
        elif resource_type == "MedicationAdministration":
            from spark_fhir_schemas.r4b.resources.medicationadministration import (
                MedicationAdministrationSchema,
            )

            return MedicationAdministrationSchema
        elif resource_type == "MedicationDispense":
            from spark_fhir_schemas.r4b.resources.medicationdispense import (
                MedicationDispenseSchema,
            )

            return MedicationDispenseSchema
        elif resource_type == "MedicationKnowledge":
            from spark_fhir_schemas.r4b.resources.medicationknowledge import (
                MedicationKnowledgeSchema,
            )

            return MedicationKnowledgeSchema
        elif resource_type == "MedicationRequest":
            from spark_fhir_schemas.r4b.resources.medicationrequest import (
                MedicationRequestSchema,
            )

            return MedicationRequestSchema
        elif resource_type == "MedicationStatement":
            from spark_fhir_schemas.r4b.resources.medicationstatement import (
                MedicationStatementSchema,
            )

            return MedicationStatementSchema
        elif resource_type == "MedicinalProductDefinition":
            from spark_fhir_schemas.r4b.resources.medicinalproductdefinition import (
                MedicinalProductDefinitionSchema,
            )

            return MedicinalProductDefinitionSchema
        elif resource_type == "MessageDefinition":
            from spark_fhir_schemas.r4b.resources.messagedefinition import (
                MessageDefinitionSchema,
            )

            return MessageDefinitionSchema
        elif resource_type == "MessageHeader":
            from spark_fhir_schemas.r4b.resources.messageheader import (
                MessageHeaderSchema,
            )

            return MessageHeaderSchema
        elif resource_type == "MolecularSequence":
            from spark_fhir_schemas.r4b.resources.molecularsequence import (
                MolecularSequenceSchema,
            )

            return MolecularSequenceSchema
        elif resource_type == "NamingSystem":
            from spark_fhir_schemas.r4b.resources.namingsystem import NamingSystemSchema

            return NamingSystemSchema
        elif resource_type == "NutritionOrder":
            from spark_fhir_schemas.r4b.resources.nutritionorder import (
                NutritionOrderSchema,
            )

            return NutritionOrderSchema
        elif resource_type == "NutritionProduct":
            from spark_fhir_schemas.r4b.resources.nutritionproduct import (
                NutritionProductSchema,
            )

            return NutritionProductSchema
        elif resource_type == "Observation":
            from spark_fhir_schemas.r4b.resources.observation import ObservationSchema

            return ObservationSchema
        elif resource_type == "ObservationDefinition":
            from spark_fhir_schemas.r4b.resources.observationdefinition import (
                ObservationDefinitionSchema,
            )

            return ObservationDefinitionSchema
        elif resource_type == "OperationDefinition":
            from spark_fhir_schemas.r4b.resources.operationdefinition import (
                OperationDefinitionSchema,
            )

            return OperationDefinitionSchema
        elif resource_type == "OperationOutcome":
            from spark_fhir_schemas.r4b.resources.operationoutcome import (
                OperationOutcomeSchema,
            )

            return OperationOutcomeSchema
        elif resource_type == "Organization":
            from spark_fhir_schemas.r4b.resources.organization import OrganizationSchema

            return OrganizationSchema
        elif resource_type == "OrganizationAffiliation":
            from spark_fhir_schemas.r4b.resources.organizationaffiliation import (
                OrganizationAffiliationSchema,
            )

            return OrganizationAffiliationSchema
        elif resource_type == "PackagedProductDefinition":
            from spark_fhir_schemas.r4b.resources.packagedproductdefinition import (
                PackagedProductDefinitionSchema,
            )

            return PackagedProductDefinitionSchema
        elif resource_type == "Parameters":
            from spark_fhir_schemas.r4b.resources.parameters import ParametersSchema

            return ParametersSchema
        elif resource_type == "Patient":
            from spark_fhir_schemas.r4b.resources.patient import PatientSchema

            return PatientSchema
        elif resource_type == "PaymentNotice":
            from spark_fhir_schemas.r4b.resources.paymentnotice import (
                PaymentNoticeSchema,
            )

            return PaymentNoticeSchema
        elif resource_type == "PaymentReconciliation":
            from spark_fhir_schemas.r4b.resources.paymentreconciliation import (
                PaymentReconciliationSchema,
            )

            return PaymentReconciliationSchema
        elif resource_type == "Person":
            from spark_fhir_schemas.r4b.resources.person import PersonSchema

            return PersonSchema
        elif resource_type == "PlanDefinition":
            from spark_fhir_schemas.r4b.resources.plandefinition import (
                PlanDefinitionSchema,
            )

            return PlanDefinitionSchema
        elif resource_type == "Practitioner":
            from spark_fhir_schemas.r4b.resources.practitioner import PractitionerSchema

            return PractitionerSchema
        elif resource_type == "PractitionerRole":
            from spark_fhir_schemas.r4b.resources.practitionerrole import (
                PractitionerRoleSchema,
            )

            return PractitionerRoleSchema
        elif resource_type == "Procedure":
            from spark_fhir_schemas.r4b.resources.procedure import ProcedureSchema

            return ProcedureSchema
        elif resource_type == "Provenance":
            from spark_fhir_schemas.r4b.resources.provenance import ProvenanceSchema

            return ProvenanceSchema
        elif resource_type == "Questionnaire":
            from spark_fhir_schemas.r4b.resources.questionnaire import (
                QuestionnaireSchema,
            )

            return QuestionnaireSchema
        elif resource_type == "QuestionnaireResponse":
            from spark_fhir_schemas.r4b.resources.questionnaireresponse import (
                QuestionnaireResponseSchema,
            )

            return QuestionnaireResponseSchema
        elif resource_type == "RegulatedAuthorization":
            from spark_fhir_schemas.r4b.resources.regulatedauthorization import (
                RegulatedAuthorizationSchema,
            )

            return RegulatedAuthorizationSchema
        elif resource_type == "RelatedPerson":
            from spark_fhir_schemas.r4b.resources.relatedperson import (
                RelatedPersonSchema,
            )

            return RelatedPersonSchema
        elif resource_type == "RequestGroup":
            from spark_fhir_schemas.r4b.resources.requestgroup import RequestGroupSchema

            return RequestGroupSchema
        elif resource_type == "ResearchDefinition":
            from spark_fhir_schemas.r4b.resources.researchdefinition import (
                ResearchDefinitionSchema,
            )

            return ResearchDefinitionSchema
        elif resource_type == "ResearchElementDefinition":
            from spark_fhir_schemas.r4b.resources.researchelementdefinition import (
                ResearchElementDefinitionSchema,
            )

            return ResearchElementDefinitionSchema
        elif resource_type == "ResearchStudy":
            from spark_fhir_schemas.r4b.resources.researchstudy import (
                ResearchStudySchema,
            )

            return ResearchStudySchema
        elif resource_type == "ResearchSubject":
            from spark_fhir_schemas.r4b.resources.researchsubject import (
                ResearchSubjectSchema,
            )

            return ResearchSubjectSchema
        elif resource_type == "RiskAssessment":
            from spark_fhir_schemas.r4b.resources.riskassessment import (
                RiskAssessmentSchema,
            )

            return RiskAssessmentSchema
        elif resource_type == "Schedule":
            from spark_fhir_schemas.r4b.resources.schedule import ScheduleSchema

            return ScheduleSchema
        elif resource_type == "SearchParameter":
            from spark_fhir_schemas.r4b.resources.searchparameter import (
                SearchParameterSchema,
            )

            return SearchParameterSchema
        elif resource_type == "ServiceRequest":
            from spark_fhir_schemas.r4b.resources.servicerequest import (
                ServiceRequestSchema,
            )

            return ServiceRequestSchema
        elif resource_type == "Slot":
            from spark_fhir_schemas.r4b.resources.slot import SlotSchema

            return SlotSchema
        elif resource_type == "Specimen":
            from spark_fhir_schemas.r4b.resources.specimen import SpecimenSchema

            return SpecimenSchema
        elif resource_type == "SpecimenDefinition":
            from spark_fhir_schemas.r4b.resources.specimendefinition import (
                SpecimenDefinitionSchema,
            )

            return SpecimenDefinitionSchema
        elif resource_type == "StructureDefinition":
            from spark_fhir_schemas.r4b.resources.structuredefinition import (
                StructureDefinitionSchema,
            )

            return StructureDefinitionSchema
        elif resource_type == "StructureMap":
            from spark_fhir_schemas.r4b.resources.structuremap import StructureMapSchema

            return StructureMapSchema
        elif resource_type == "Subscription":
            from spark_fhir_schemas.r4b.resources.subscription import SubscriptionSchema

            return SubscriptionSchema
        elif resource_type == "SubscriptionStatus":
            from spark_fhir_schemas.r4b.resources.subscriptionstatus import (
                SubscriptionStatusSchema,
            )

            return SubscriptionStatusSchema
        elif resource_type == "SubscriptionTopic":
            from spark_fhir_schemas.r4b.resources.subscriptiontopic import (
                SubscriptionTopicSchema,
            )

            return SubscriptionTopicSchema
        elif resource_type == "Substance":
            from spark_fhir_schemas.r4b.resources.substance import SubstanceSchema

            return SubstanceSchema
        elif resource_type == "SubstanceDefinition":
            from spark_fhir_schemas.r4b.resources.substancedefinition import (
                SubstanceDefinitionSchema,
            )

            return SubstanceDefinitionSchema
        elif resource_type == "SupplyDelivery":
            from spark_fhir_schemas.r4b.resources.supplydelivery import (
                SupplyDeliverySchema,
            )

            return SupplyDeliverySchema
        elif resource_type == "SupplyRequest":
            from spark_fhir_schemas.r4b.resources.supplyrequest import (
                SupplyRequestSchema,
            )

            return SupplyRequestSchema
        elif resource_type == "Task":
            from spark_fhir_schemas.r4b.resources.task import TaskSchema

            return TaskSchema
        elif resource_type == "TerminologyCapabilities":
            from spark_fhir_schemas.r4b.resources.terminologycapabilities import (
                TerminologyCapabilitiesSchema,
            )

            return TerminologyCapabilitiesSchema
        elif resource_type == "TestReport":
            from spark_fhir_schemas.r4b.resources.testreport import TestReportSchema

            return TestReportSchema
        elif resource_type == "TestScript":
            from spark_fhir_schemas.r4b.resources.testscript import TestScriptSchema

            return TestScriptSchema
        elif resource_type == "ValueSet":
            from spark_fhir_schemas.r4b.resources.valueset import ValueSetSchema

            return ValueSetSchema
        elif resource_type == "VerificationResult":
            from spark_fhir_schemas.r4b.resources.verificationresult import (
                VerificationResultSchema,
            )

            return VerificationResultSchema
        elif resource_type == "VisionPrescription":
            from spark_fhir_schemas.r4b.resources.visionprescription import (
                VisionPrescriptionSchema,
            )

            return VisionPrescriptionSchema
        else:
            raise Exception(f"Resource Type {resource_type} is unknown")
