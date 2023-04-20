from typing import Any


class ResourceSchemaIndex:
    @staticmethod
    def get(resource_type: str) -> Any:
        if resource_type is None:
            raise Exception("Invalid resource type")
        elif resource_type == "Account":
            from spark_fhir_schemas.dstu2.resources.account import AccountSchema

            return AccountSchema
        elif resource_type == "AllergyIntolerance":
            from spark_fhir_schemas.dstu2.resources.allergyintolerance import (
                AllergyIntoleranceSchema,
            )

            return AllergyIntoleranceSchema
        elif resource_type == "Appointment":
            from spark_fhir_schemas.dstu2.resources.appointment import AppointmentSchema

            return AppointmentSchema
        elif resource_type == "AppointmentResponse":
            from spark_fhir_schemas.dstu2.resources.appointmentresponse import (
                AppointmentResponseSchema,
            )

            return AppointmentResponseSchema
        elif resource_type == "AuditEvent":
            from spark_fhir_schemas.dstu2.resources.auditevent import AuditEventSchema

            return AuditEventSchema
        elif resource_type == "Basic":
            from spark_fhir_schemas.dstu2.resources.basic import BasicSchema

            return BasicSchema
        elif resource_type == "Binary":
            from spark_fhir_schemas.dstu2.resources.binary import BinarySchema

            return BinarySchema
        elif resource_type == "Bundle":
            from spark_fhir_schemas.dstu2.resources.bundle import BundleSchema

            return BundleSchema
        elif resource_type == "CarePlan":
            from spark_fhir_schemas.dstu2.resources.careplan import CarePlanSchema

            return CarePlanSchema
        elif resource_type == "Claim":
            from spark_fhir_schemas.dstu2.resources.claim import ClaimSchema

            return ClaimSchema
        elif resource_type == "ClaimResponse":
            from spark_fhir_schemas.dstu2.resources.claimresponse import (
                ClaimResponseSchema,
            )

            return ClaimResponseSchema
        elif resource_type == "ClinicalImpression":
            from spark_fhir_schemas.dstu2.resources.clinicalimpression import (
                ClinicalImpressionSchema,
            )

            return ClinicalImpressionSchema
        elif resource_type == "Communication":
            from spark_fhir_schemas.dstu2.resources.communication import (
                CommunicationSchema,
            )

            return CommunicationSchema
        elif resource_type == "CommunicationRequest":
            from spark_fhir_schemas.dstu2.resources.communicationrequest import (
                CommunicationRequestSchema,
            )

            return CommunicationRequestSchema
        elif resource_type == "Composition":
            from spark_fhir_schemas.dstu2.resources.composition import CompositionSchema

            return CompositionSchema
        elif resource_type == "ConceptMap":
            from spark_fhir_schemas.dstu2.resources.conceptmap import ConceptMapSchema

            return ConceptMapSchema
        elif resource_type == "Condition":
            from spark_fhir_schemas.dstu2.resources.condition import ConditionSchema

            return ConditionSchema
        elif resource_type == "Contract":
            from spark_fhir_schemas.dstu2.resources.contract import ContractSchema

            return ContractSchema
        elif resource_type == "Coverage":
            from spark_fhir_schemas.dstu2.resources.coverage import CoverageSchema

            return CoverageSchema
        elif resource_type == "DetectedIssue":
            from spark_fhir_schemas.dstu2.resources.detectedissue import (
                DetectedIssueSchema,
            )

            return DetectedIssueSchema
        elif resource_type == "Device":
            from spark_fhir_schemas.dstu2.resources.device import DeviceSchema

            return DeviceSchema
        elif resource_type == "DeviceMetric":
            from spark_fhir_schemas.dstu2.resources.devicemetric import (
                DeviceMetricSchema,
            )

            return DeviceMetricSchema
        elif resource_type == "DeviceUseStatement":
            from spark_fhir_schemas.dstu2.resources.deviceusestatement import (
                DeviceUseStatementSchema,
            )

            return DeviceUseStatementSchema
        elif resource_type == "DiagnosticReport":
            from spark_fhir_schemas.dstu2.resources.diagnosticreport import (
                DiagnosticReportSchema,
            )

            return DiagnosticReportSchema
        elif resource_type == "DocumentManifest":
            from spark_fhir_schemas.dstu2.resources.documentmanifest import (
                DocumentManifestSchema,
            )

            return DocumentManifestSchema
        elif resource_type == "DocumentReference":
            from spark_fhir_schemas.dstu2.resources.documentreference import (
                DocumentReferenceSchema,
            )

            return DocumentReferenceSchema
        elif resource_type == "Encounter":
            from spark_fhir_schemas.dstu2.resources.encounter import EncounterSchema

            return EncounterSchema
        elif resource_type == "EnrollmentRequest":
            from spark_fhir_schemas.dstu2.resources.enrollmentrequest import (
                EnrollmentRequestSchema,
            )

            return EnrollmentRequestSchema
        elif resource_type == "EnrollmentResponse":
            from spark_fhir_schemas.dstu2.resources.enrollmentresponse import (
                EnrollmentResponseSchema,
            )

            return EnrollmentResponseSchema
        elif resource_type == "EpisodeOfCare":
            from spark_fhir_schemas.dstu2.resources.episodeofcare import (
                EpisodeOfCareSchema,
            )

            return EpisodeOfCareSchema
        elif resource_type == "ExplanationOfBenefit":
            from spark_fhir_schemas.dstu2.resources.explanationofbenefit import (
                ExplanationOfBenefitSchema,
            )

            return ExplanationOfBenefitSchema
        elif resource_type == "FamilyMemberHistory":
            from spark_fhir_schemas.dstu2.resources.familymemberhistory import (
                FamilyMemberHistorySchema,
            )

            return FamilyMemberHistorySchema
        elif resource_type == "Flag":
            from spark_fhir_schemas.dstu2.resources.flag import FlagSchema

            return FlagSchema
        elif resource_type == "Goal":
            from spark_fhir_schemas.dstu2.resources.goal import GoalSchema

            return GoalSchema
        elif resource_type == "Group":
            from spark_fhir_schemas.dstu2.resources.group import GroupSchema

            return GroupSchema
        elif resource_type == "HealthcareService":
            from spark_fhir_schemas.dstu2.resources.healthcareservice import (
                HealthcareServiceSchema,
            )

            return HealthcareServiceSchema
        elif resource_type == "ImagingStudy":
            from spark_fhir_schemas.dstu2.resources.imagingstudy import (
                ImagingStudySchema,
            )

            return ImagingStudySchema
        elif resource_type == "Immunization":
            from spark_fhir_schemas.dstu2.resources.immunization import (
                ImmunizationSchema,
            )

            return ImmunizationSchema
        elif resource_type == "ImmunizationRecommendation":
            from spark_fhir_schemas.dstu2.resources.immunizationrecommendation import (
                ImmunizationRecommendationSchema,
            )

            return ImmunizationRecommendationSchema
        elif resource_type == "ImplementationGuide":
            from spark_fhir_schemas.dstu2.resources.implementationguide import (
                ImplementationGuideSchema,
            )

            return ImplementationGuideSchema
        elif resource_type == "List":
            from spark_fhir_schemas.dstu2.resources.list import ListSchema

            return ListSchema
        elif resource_type == "Location":
            from spark_fhir_schemas.dstu2.resources.location import LocationSchema

            return LocationSchema
        elif resource_type == "Media":
            from spark_fhir_schemas.dstu2.resources.media import MediaSchema

            return MediaSchema
        elif resource_type == "Medication":
            from spark_fhir_schemas.dstu2.resources.medication import MedicationSchema

            return MedicationSchema
        elif resource_type == "MedicationAdministration":
            from spark_fhir_schemas.dstu2.resources.medicationadministration import (
                MedicationAdministrationSchema,
            )

            return MedicationAdministrationSchema
        elif resource_type == "MedicationDispense":
            from spark_fhir_schemas.dstu2.resources.medicationdispense import (
                MedicationDispenseSchema,
            )

            return MedicationDispenseSchema
        elif resource_type == "MedicationStatement":
            from spark_fhir_schemas.dstu2.resources.medicationstatement import (
                MedicationStatementSchema,
            )

            return MedicationStatementSchema
        elif resource_type == "MessageHeader":
            from spark_fhir_schemas.dstu2.resources.messageheader import (
                MessageHeaderSchema,
            )

            return MessageHeaderSchema
        elif resource_type == "NamingSystem":
            from spark_fhir_schemas.dstu2.resources.namingsystem import (
                NamingSystemSchema,
            )

            return NamingSystemSchema
        elif resource_type == "NutritionOrder":
            from spark_fhir_schemas.dstu2.resources.nutritionorder import (
                NutritionOrderSchema,
            )

            return NutritionOrderSchema
        elif resource_type == "Observation":
            from spark_fhir_schemas.dstu2.resources.observation import ObservationSchema

            return ObservationSchema
        elif resource_type == "OperationDefinition":
            from spark_fhir_schemas.dstu2.resources.operationdefinition import (
                OperationDefinitionSchema,
            )

            return OperationDefinitionSchema
        elif resource_type == "OperationOutcome":
            from spark_fhir_schemas.dstu2.resources.operationoutcome import (
                OperationOutcomeSchema,
            )

            return OperationOutcomeSchema
        elif resource_type == "Organization":
            from spark_fhir_schemas.dstu2.resources.organization import (
                OrganizationSchema,
            )

            return OrganizationSchema
        elif resource_type == "Parameters":
            from spark_fhir_schemas.dstu2.resources.parameters import ParametersSchema

            return ParametersSchema
        elif resource_type == "Patient":
            from spark_fhir_schemas.dstu2.resources.patient import PatientSchema

            return PatientSchema
        elif resource_type == "PaymentNotice":
            from spark_fhir_schemas.dstu2.resources.paymentnotice import (
                PaymentNoticeSchema,
            )

            return PaymentNoticeSchema
        elif resource_type == "PaymentReconciliation":
            from spark_fhir_schemas.dstu2.resources.paymentreconciliation import (
                PaymentReconciliationSchema,
            )

            return PaymentReconciliationSchema
        elif resource_type == "Person":
            from spark_fhir_schemas.dstu2.resources.person import PersonSchema

            return PersonSchema
        elif resource_type == "Practitioner":
            from spark_fhir_schemas.dstu2.resources.practitioner import (
                PractitionerSchema,
            )

            return PractitionerSchema
        elif resource_type == "Procedure":
            from spark_fhir_schemas.dstu2.resources.procedure import ProcedureSchema

            return ProcedureSchema
        elif resource_type == "Provenance":
            from spark_fhir_schemas.dstu2.resources.provenance import ProvenanceSchema

            return ProvenanceSchema
        elif resource_type == "Questionnaire":
            from spark_fhir_schemas.dstu2.resources.questionnaire import (
                QuestionnaireSchema,
            )

            return QuestionnaireSchema
        elif resource_type == "QuestionnaireResponse":
            from spark_fhir_schemas.dstu2.resources.questionnaireresponse import (
                QuestionnaireResponseSchema,
            )

            return QuestionnaireResponseSchema
        elif resource_type == "RelatedPerson":
            from spark_fhir_schemas.dstu2.resources.relatedperson import (
                RelatedPersonSchema,
            )

            return RelatedPersonSchema
        elif resource_type == "RiskAssessment":
            from spark_fhir_schemas.dstu2.resources.riskassessment import (
                RiskAssessmentSchema,
            )

            return RiskAssessmentSchema
        elif resource_type == "Schedule":
            from spark_fhir_schemas.dstu2.resources.schedule import ScheduleSchema

            return ScheduleSchema
        elif resource_type == "SearchParameter":
            from spark_fhir_schemas.dstu2.resources.searchparameter import (
                SearchParameterSchema,
            )

            return SearchParameterSchema
        elif resource_type == "Slot":
            from spark_fhir_schemas.dstu2.resources.slot import SlotSchema

            return SlotSchema
        elif resource_type == "Specimen":
            from spark_fhir_schemas.dstu2.resources.specimen import SpecimenSchema

            return SpecimenSchema
        elif resource_type == "StructureDefinition":
            from spark_fhir_schemas.dstu2.resources.structuredefinition import (
                StructureDefinitionSchema,
            )

            return StructureDefinitionSchema
        elif resource_type == "Subscription":
            from spark_fhir_schemas.dstu2.resources.subscription import (
                SubscriptionSchema,
            )

            return SubscriptionSchema
        elif resource_type == "Substance":
            from spark_fhir_schemas.dstu2.resources.substance import SubstanceSchema

            return SubstanceSchema
        elif resource_type == "SupplyDelivery":
            from spark_fhir_schemas.dstu2.resources.supplydelivery import (
                SupplyDeliverySchema,
            )

            return SupplyDeliverySchema
        elif resource_type == "SupplyRequest":
            from spark_fhir_schemas.dstu2.resources.supplyrequest import (
                SupplyRequestSchema,
            )

            return SupplyRequestSchema
        elif resource_type == "TestScript":
            from spark_fhir_schemas.dstu2.resources.testscript import TestScriptSchema

            return TestScriptSchema
        elif resource_type == "ValueSet":
            from spark_fhir_schemas.dstu2.resources.valueset import ValueSetSchema

            return ValueSetSchema
        elif resource_type == "VisionPrescription":
            from spark_fhir_schemas.dstu2.resources.visionprescription import (
                VisionPrescriptionSchema,
            )

            return VisionPrescriptionSchema
        else:
            raise Exception(f"Resource Type {resource_type} is unknown")
