from typing import Any


class ResourceSchemaIndex:
    @staticmethod
    def get(resource_type: str) -> Any:
        if resource_type is None:
            raise Exception("Invalid resource type")
        elif resource_type == "Element":
            from spark_fhir_schemas.stu3.complex_types.element import ElementSchema

            return ElementSchema
        elif resource_type == "Extension":
            from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema

            return ExtensionSchema
        elif resource_type == "BackboneElement":
            from spark_fhir_schemas.stu3.complex_types.backboneelement import (
                BackboneElementSchema,
            )

            return BackboneElementSchema
        elif resource_type == "Narrative":
            from spark_fhir_schemas.stu3.complex_types.narrative import NarrativeSchema

            return NarrativeSchema
        elif resource_type == "Annotation":
            from spark_fhir_schemas.stu3.complex_types.annotation import (
                AnnotationSchema,
            )

            return AnnotationSchema
        elif resource_type == "Attachment":
            from spark_fhir_schemas.stu3.complex_types.attachment import (
                AttachmentSchema,
            )

            return AttachmentSchema
        elif resource_type == "Identifier":
            from spark_fhir_schemas.stu3.complex_types.identifier import (
                IdentifierSchema,
            )

            return IdentifierSchema
        elif resource_type == "CodeableConcept":
            from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
                CodeableConceptSchema,
            )

            return CodeableConceptSchema
        elif resource_type == "Coding":
            from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema

            return CodingSchema
        elif resource_type == "Quantity":
            from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema

            return QuantitySchema
        elif resource_type == "Duration":
            from spark_fhir_schemas.stu3.complex_types.duration import DurationSchema

            return DurationSchema
        elif resource_type == "Distance":
            from spark_fhir_schemas.stu3.complex_types.distance import DistanceSchema

            return DistanceSchema
        elif resource_type == "Count":
            from spark_fhir_schemas.stu3.complex_types.count import CountSchema

            return CountSchema
        elif resource_type == "Money":
            from spark_fhir_schemas.stu3.complex_types.money import MoneySchema

            return MoneySchema
        elif resource_type == "Age":
            from spark_fhir_schemas.stu3.complex_types.age import AgeSchema

            return AgeSchema
        elif resource_type == "Range":
            from spark_fhir_schemas.stu3.complex_types.range import RangeSchema

            return RangeSchema
        elif resource_type == "Period":
            from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema

            return PeriodSchema
        elif resource_type == "Ratio":
            from spark_fhir_schemas.stu3.complex_types.ratio import RatioSchema

            return RatioSchema
        elif resource_type == "Reference":
            from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema

            return ReferenceSchema
        elif resource_type == "SampledData":
            from spark_fhir_schemas.stu3.complex_types.sampleddata import (
                SampledDataSchema,
            )

            return SampledDataSchema
        elif resource_type == "Signature":
            from spark_fhir_schemas.stu3.complex_types.signature import SignatureSchema

            return SignatureSchema
        elif resource_type == "HumanName":
            from spark_fhir_schemas.stu3.complex_types.humanname import HumanNameSchema

            return HumanNameSchema
        elif resource_type == "Address":
            from spark_fhir_schemas.stu3.complex_types.address import AddressSchema

            return AddressSchema
        elif resource_type == "ContactPoint":
            from spark_fhir_schemas.stu3.complex_types.contactpoint import (
                ContactPointSchema,
            )

            return ContactPointSchema
        elif resource_type == "Timing":
            from spark_fhir_schemas.stu3.complex_types.timing import TimingSchema

            return TimingSchema
        elif resource_type == "Timing_Repeat":
            from spark_fhir_schemas.stu3.complex_types.timing_repeat import (
                Timing_RepeatSchema,
            )

            return Timing_RepeatSchema
        elif resource_type == "Meta":
            from spark_fhir_schemas.stu3.complex_types.meta import MetaSchema

            return MetaSchema
        elif resource_type == "ElementDefinition":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition import (
                ElementDefinitionSchema,
            )

            return ElementDefinitionSchema
        elif resource_type == "ElementDefinition_Slicing":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_slicing import (
                ElementDefinition_SlicingSchema,
            )

            return ElementDefinition_SlicingSchema
        elif resource_type == "ElementDefinition_Discriminator":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_discriminator import (
                ElementDefinition_DiscriminatorSchema,
            )

            return ElementDefinition_DiscriminatorSchema
        elif resource_type == "ElementDefinition_Base":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_base import (
                ElementDefinition_BaseSchema,
            )

            return ElementDefinition_BaseSchema
        elif resource_type == "ElementDefinition_Type":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_type import (
                ElementDefinition_TypeSchema,
            )

            return ElementDefinition_TypeSchema
        elif resource_type == "ElementDefinition_Example":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_example import (
                ElementDefinition_ExampleSchema,
            )

            return ElementDefinition_ExampleSchema
        elif resource_type == "ElementDefinition_Constraint":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_constraint import (
                ElementDefinition_ConstraintSchema,
            )

            return ElementDefinition_ConstraintSchema
        elif resource_type == "ElementDefinition_Binding":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_binding import (
                ElementDefinition_BindingSchema,
            )

            return ElementDefinition_BindingSchema
        elif resource_type == "ElementDefinition_Mapping":
            from spark_fhir_schemas.stu3.complex_types.elementdefinition_mapping import (
                ElementDefinition_MappingSchema,
            )

            return ElementDefinition_MappingSchema
        elif resource_type == "ContactDetail":
            from spark_fhir_schemas.stu3.complex_types.contactdetail import (
                ContactDetailSchema,
            )

            return ContactDetailSchema
        elif resource_type == "Contributor":
            from spark_fhir_schemas.stu3.complex_types.contributor import (
                ContributorSchema,
            )

            return ContributorSchema
        elif resource_type == "Dosage":
            from spark_fhir_schemas.stu3.complex_types.dosage import DosageSchema

            return DosageSchema
        elif resource_type == "RelatedArtifact":
            from spark_fhir_schemas.stu3.complex_types.relatedartifact import (
                RelatedArtifactSchema,
            )

            return RelatedArtifactSchema
        elif resource_type == "UsageContext":
            from spark_fhir_schemas.stu3.complex_types.usagecontext import (
                UsageContextSchema,
            )

            return UsageContextSchema
        elif resource_type == "DataRequirement":
            from spark_fhir_schemas.stu3.complex_types.datarequirement import (
                DataRequirementSchema,
            )

            return DataRequirementSchema
        elif resource_type == "DataRequirement_CodeFilter":
            from spark_fhir_schemas.stu3.complex_types.datarequirement_codefilter import (
                DataRequirement_CodeFilterSchema,
            )

            return DataRequirement_CodeFilterSchema
        elif resource_type == "DataRequirement_DateFilter":
            from spark_fhir_schemas.stu3.complex_types.datarequirement_datefilter import (
                DataRequirement_DateFilterSchema,
            )

            return DataRequirement_DateFilterSchema
        elif resource_type == "ParameterDefinition":
            from spark_fhir_schemas.stu3.complex_types.parameterdefinition import (
                ParameterDefinitionSchema,
            )

            return ParameterDefinitionSchema
        elif resource_type == "TriggerDefinition":
            from spark_fhir_schemas.stu3.complex_types.triggerdefinition import (
                TriggerDefinitionSchema,
            )

            return TriggerDefinitionSchema
        elif resource_type == "Account":
            from spark_fhir_schemas.stu3.complex_types.account import AccountSchema

            return AccountSchema
        elif resource_type == "Account_Coverage":
            from spark_fhir_schemas.stu3.complex_types.account_coverage import (
                Account_CoverageSchema,
            )

            return Account_CoverageSchema
        elif resource_type == "Account_Guarantor":
            from spark_fhir_schemas.stu3.complex_types.account_guarantor import (
                Account_GuarantorSchema,
            )

            return Account_GuarantorSchema
        elif resource_type == "ActivityDefinition":
            from spark_fhir_schemas.stu3.complex_types.activitydefinition import (
                ActivityDefinitionSchema,
            )

            return ActivityDefinitionSchema
        elif resource_type == "ActivityDefinition_Participant":
            from spark_fhir_schemas.stu3.complex_types.activitydefinition_participant import (
                ActivityDefinition_ParticipantSchema,
            )

            return ActivityDefinition_ParticipantSchema
        elif resource_type == "ActivityDefinition_DynamicValue":
            from spark_fhir_schemas.stu3.complex_types.activitydefinition_dynamicvalue import (
                ActivityDefinition_DynamicValueSchema,
            )

            return ActivityDefinition_DynamicValueSchema
        elif resource_type == "AdverseEvent":
            from spark_fhir_schemas.stu3.complex_types.adverseevent import (
                AdverseEventSchema,
            )

            return AdverseEventSchema
        elif resource_type == "AdverseEvent_SuspectEntity":
            from spark_fhir_schemas.stu3.complex_types.adverseevent_suspectentity import (
                AdverseEvent_SuspectEntitySchema,
            )

            return AdverseEvent_SuspectEntitySchema
        elif resource_type == "AllergyIntolerance":
            from spark_fhir_schemas.stu3.complex_types.allergyintolerance import (
                AllergyIntoleranceSchema,
            )

            return AllergyIntoleranceSchema
        elif resource_type == "AllergyIntolerance_Reaction":
            from spark_fhir_schemas.stu3.complex_types.allergyintolerance_reaction import (
                AllergyIntolerance_ReactionSchema,
            )

            return AllergyIntolerance_ReactionSchema
        elif resource_type == "Appointment":
            from spark_fhir_schemas.stu3.complex_types.appointment import (
                AppointmentSchema,
            )

            return AppointmentSchema
        elif resource_type == "Appointment_Participant":
            from spark_fhir_schemas.stu3.complex_types.appointment_participant import (
                Appointment_ParticipantSchema,
            )

            return Appointment_ParticipantSchema
        elif resource_type == "AppointmentResponse":
            from spark_fhir_schemas.stu3.complex_types.appointmentresponse import (
                AppointmentResponseSchema,
            )

            return AppointmentResponseSchema
        elif resource_type == "AuditEvent":
            from spark_fhir_schemas.stu3.complex_types.auditevent import (
                AuditEventSchema,
            )

            return AuditEventSchema
        elif resource_type == "AuditEvent_Agent":
            from spark_fhir_schemas.stu3.complex_types.auditevent_agent import (
                AuditEvent_AgentSchema,
            )

            return AuditEvent_AgentSchema
        elif resource_type == "AuditEvent_Network":
            from spark_fhir_schemas.stu3.complex_types.auditevent_network import (
                AuditEvent_NetworkSchema,
            )

            return AuditEvent_NetworkSchema
        elif resource_type == "AuditEvent_Source":
            from spark_fhir_schemas.stu3.complex_types.auditevent_source import (
                AuditEvent_SourceSchema,
            )

            return AuditEvent_SourceSchema
        elif resource_type == "AuditEvent_Entity":
            from spark_fhir_schemas.stu3.complex_types.auditevent_entity import (
                AuditEvent_EntitySchema,
            )

            return AuditEvent_EntitySchema
        elif resource_type == "AuditEvent_Detail":
            from spark_fhir_schemas.stu3.complex_types.auditevent_detail import (
                AuditEvent_DetailSchema,
            )

            return AuditEvent_DetailSchema
        elif resource_type == "Basic":
            from spark_fhir_schemas.stu3.complex_types.basic import BasicSchema

            return BasicSchema
        elif resource_type == "Binary":
            from spark_fhir_schemas.stu3.complex_types.binary import BinarySchema

            return BinarySchema
        elif resource_type == "BodySite":
            from spark_fhir_schemas.stu3.complex_types.bodysite import BodySiteSchema

            return BodySiteSchema
        elif resource_type == "Bundle":
            from spark_fhir_schemas.stu3.complex_types.bundle import BundleSchema

            return BundleSchema
        elif resource_type == "Bundle_Link":
            from spark_fhir_schemas.stu3.complex_types.bundle_link import (
                Bundle_LinkSchema,
            )

            return Bundle_LinkSchema
        elif resource_type == "Bundle_Entry":
            from spark_fhir_schemas.stu3.complex_types.bundle_entry import (
                Bundle_EntrySchema,
            )

            return Bundle_EntrySchema
        elif resource_type == "Bundle_Search":
            from spark_fhir_schemas.stu3.complex_types.bundle_search import (
                Bundle_SearchSchema,
            )

            return Bundle_SearchSchema
        elif resource_type == "Bundle_Request":
            from spark_fhir_schemas.stu3.complex_types.bundle_request import (
                Bundle_RequestSchema,
            )

            return Bundle_RequestSchema
        elif resource_type == "Bundle_Response":
            from spark_fhir_schemas.stu3.complex_types.bundle_response import (
                Bundle_ResponseSchema,
            )

            return Bundle_ResponseSchema
        elif resource_type == "CapabilityStatement":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement import (
                CapabilityStatementSchema,
            )

            return CapabilityStatementSchema
        elif resource_type == "CapabilityStatement_Software":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_software import (
                CapabilityStatement_SoftwareSchema,
            )

            return CapabilityStatement_SoftwareSchema
        elif resource_type == "CapabilityStatement_Implementation":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_implementation import (
                CapabilityStatement_ImplementationSchema,
            )

            return CapabilityStatement_ImplementationSchema
        elif resource_type == "CapabilityStatement_Rest":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_rest import (
                CapabilityStatement_RestSchema,
            )

            return CapabilityStatement_RestSchema
        elif resource_type == "CapabilityStatement_Security":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_security import (
                CapabilityStatement_SecuritySchema,
            )

            return CapabilityStatement_SecuritySchema
        elif resource_type == "CapabilityStatement_Certificate":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_certificate import (
                CapabilityStatement_CertificateSchema,
            )

            return CapabilityStatement_CertificateSchema
        elif resource_type == "CapabilityStatement_Resource":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_resource import (
                CapabilityStatement_ResourceSchema,
            )

            return CapabilityStatement_ResourceSchema
        elif resource_type == "CapabilityStatement_Interaction":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_interaction import (
                CapabilityStatement_InteractionSchema,
            )

            return CapabilityStatement_InteractionSchema
        elif resource_type == "CapabilityStatement_SearchParam":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_searchparam import (
                CapabilityStatement_SearchParamSchema,
            )

            return CapabilityStatement_SearchParamSchema
        elif resource_type == "CapabilityStatement_Interaction1":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_interaction1 import (
                CapabilityStatement_Interaction1Schema,
            )

            return CapabilityStatement_Interaction1Schema
        elif resource_type == "CapabilityStatement_Operation":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_operation import (
                CapabilityStatement_OperationSchema,
            )

            return CapabilityStatement_OperationSchema
        elif resource_type == "CapabilityStatement_Messaging":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_messaging import (
                CapabilityStatement_MessagingSchema,
            )

            return CapabilityStatement_MessagingSchema
        elif resource_type == "CapabilityStatement_Endpoint":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_endpoint import (
                CapabilityStatement_EndpointSchema,
            )

            return CapabilityStatement_EndpointSchema
        elif resource_type == "CapabilityStatement_SupportedMessage":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_supportedmessage import (
                CapabilityStatement_SupportedMessageSchema,
            )

            return CapabilityStatement_SupportedMessageSchema
        elif resource_type == "CapabilityStatement_Event":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_event import (
                CapabilityStatement_EventSchema,
            )

            return CapabilityStatement_EventSchema
        elif resource_type == "CapabilityStatement_Document":
            from spark_fhir_schemas.stu3.complex_types.capabilitystatement_document import (
                CapabilityStatement_DocumentSchema,
            )

            return CapabilityStatement_DocumentSchema
        elif resource_type == "CarePlan":
            from spark_fhir_schemas.stu3.complex_types.careplan import CarePlanSchema

            return CarePlanSchema
        elif resource_type == "CarePlan_Activity":
            from spark_fhir_schemas.stu3.complex_types.careplan_activity import (
                CarePlan_ActivitySchema,
            )

            return CarePlan_ActivitySchema
        elif resource_type == "CarePlan_Detail":
            from spark_fhir_schemas.stu3.complex_types.careplan_detail import (
                CarePlan_DetailSchema,
            )

            return CarePlan_DetailSchema
        elif resource_type == "CareTeam":
            from spark_fhir_schemas.stu3.complex_types.careteam import CareTeamSchema

            return CareTeamSchema
        elif resource_type == "CareTeam_Participant":
            from spark_fhir_schemas.stu3.complex_types.careteam_participant import (
                CareTeam_ParticipantSchema,
            )

            return CareTeam_ParticipantSchema
        elif resource_type == "ChargeItem":
            from spark_fhir_schemas.stu3.complex_types.chargeitem import (
                ChargeItemSchema,
            )

            return ChargeItemSchema
        elif resource_type == "ChargeItem_Participant":
            from spark_fhir_schemas.stu3.complex_types.chargeitem_participant import (
                ChargeItem_ParticipantSchema,
            )

            return ChargeItem_ParticipantSchema
        elif resource_type == "Claim":
            from spark_fhir_schemas.stu3.complex_types.claim import ClaimSchema

            return ClaimSchema
        elif resource_type == "Claim_Related":
            from spark_fhir_schemas.stu3.complex_types.claim_related import (
                Claim_RelatedSchema,
            )

            return Claim_RelatedSchema
        elif resource_type == "Claim_Payee":
            from spark_fhir_schemas.stu3.complex_types.claim_payee import (
                Claim_PayeeSchema,
            )

            return Claim_PayeeSchema
        elif resource_type == "Claim_CareTeam":
            from spark_fhir_schemas.stu3.complex_types.claim_careteam import (
                Claim_CareTeamSchema,
            )

            return Claim_CareTeamSchema
        elif resource_type == "Claim_Information":
            from spark_fhir_schemas.stu3.complex_types.claim_information import (
                Claim_InformationSchema,
            )

            return Claim_InformationSchema
        elif resource_type == "Claim_Diagnosis":
            from spark_fhir_schemas.stu3.complex_types.claim_diagnosis import (
                Claim_DiagnosisSchema,
            )

            return Claim_DiagnosisSchema
        elif resource_type == "Claim_Procedure":
            from spark_fhir_schemas.stu3.complex_types.claim_procedure import (
                Claim_ProcedureSchema,
            )

            return Claim_ProcedureSchema
        elif resource_type == "Claim_Insurance":
            from spark_fhir_schemas.stu3.complex_types.claim_insurance import (
                Claim_InsuranceSchema,
            )

            return Claim_InsuranceSchema
        elif resource_type == "Claim_Accident":
            from spark_fhir_schemas.stu3.complex_types.claim_accident import (
                Claim_AccidentSchema,
            )

            return Claim_AccidentSchema
        elif resource_type == "Claim_Item":
            from spark_fhir_schemas.stu3.complex_types.claim_item import (
                Claim_ItemSchema,
            )

            return Claim_ItemSchema
        elif resource_type == "Claim_Detail":
            from spark_fhir_schemas.stu3.complex_types.claim_detail import (
                Claim_DetailSchema,
            )

            return Claim_DetailSchema
        elif resource_type == "Claim_SubDetail":
            from spark_fhir_schemas.stu3.complex_types.claim_subdetail import (
                Claim_SubDetailSchema,
            )

            return Claim_SubDetailSchema
        elif resource_type == "ClaimResponse":
            from spark_fhir_schemas.stu3.complex_types.claimresponse import (
                ClaimResponseSchema,
            )

            return ClaimResponseSchema
        elif resource_type == "ClaimResponse_Item":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_item import (
                ClaimResponse_ItemSchema,
            )

            return ClaimResponse_ItemSchema
        elif resource_type == "ClaimResponse_Adjudication":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_adjudication import (
                ClaimResponse_AdjudicationSchema,
            )

            return ClaimResponse_AdjudicationSchema
        elif resource_type == "ClaimResponse_Detail":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_detail import (
                ClaimResponse_DetailSchema,
            )

            return ClaimResponse_DetailSchema
        elif resource_type == "ClaimResponse_SubDetail":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_subdetail import (
                ClaimResponse_SubDetailSchema,
            )

            return ClaimResponse_SubDetailSchema
        elif resource_type == "ClaimResponse_AddItem":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_additem import (
                ClaimResponse_AddItemSchema,
            )

            return ClaimResponse_AddItemSchema
        elif resource_type == "ClaimResponse_Detail1":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_detail1 import (
                ClaimResponse_Detail1Schema,
            )

            return ClaimResponse_Detail1Schema
        elif resource_type == "ClaimResponse_Error":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_error import (
                ClaimResponse_ErrorSchema,
            )

            return ClaimResponse_ErrorSchema
        elif resource_type == "ClaimResponse_Payment":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_payment import (
                ClaimResponse_PaymentSchema,
            )

            return ClaimResponse_PaymentSchema
        elif resource_type == "ClaimResponse_ProcessNote":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_processnote import (
                ClaimResponse_ProcessNoteSchema,
            )

            return ClaimResponse_ProcessNoteSchema
        elif resource_type == "ClaimResponse_Insurance":
            from spark_fhir_schemas.stu3.complex_types.claimresponse_insurance import (
                ClaimResponse_InsuranceSchema,
            )

            return ClaimResponse_InsuranceSchema
        elif resource_type == "ClinicalImpression":
            from spark_fhir_schemas.stu3.complex_types.clinicalimpression import (
                ClinicalImpressionSchema,
            )

            return ClinicalImpressionSchema
        elif resource_type == "ClinicalImpression_Investigation":
            from spark_fhir_schemas.stu3.complex_types.clinicalimpression_investigation import (
                ClinicalImpression_InvestigationSchema,
            )

            return ClinicalImpression_InvestigationSchema
        elif resource_type == "ClinicalImpression_Finding":
            from spark_fhir_schemas.stu3.complex_types.clinicalimpression_finding import (
                ClinicalImpression_FindingSchema,
            )

            return ClinicalImpression_FindingSchema
        elif resource_type == "CodeSystem":
            from spark_fhir_schemas.stu3.complex_types.codesystem import (
                CodeSystemSchema,
            )

            return CodeSystemSchema
        elif resource_type == "CodeSystem_Filter":
            from spark_fhir_schemas.stu3.complex_types.codesystem_filter import (
                CodeSystem_FilterSchema,
            )

            return CodeSystem_FilterSchema
        elif resource_type == "CodeSystem_Property":
            from spark_fhir_schemas.stu3.complex_types.codesystem_property import (
                CodeSystem_PropertySchema,
            )

            return CodeSystem_PropertySchema
        elif resource_type == "CodeSystem_Concept":
            from spark_fhir_schemas.stu3.complex_types.codesystem_concept import (
                CodeSystem_ConceptSchema,
            )

            return CodeSystem_ConceptSchema
        elif resource_type == "CodeSystem_Designation":
            from spark_fhir_schemas.stu3.complex_types.codesystem_designation import (
                CodeSystem_DesignationSchema,
            )

            return CodeSystem_DesignationSchema
        elif resource_type == "CodeSystem_Property1":
            from spark_fhir_schemas.stu3.complex_types.codesystem_property1 import (
                CodeSystem_Property1Schema,
            )

            return CodeSystem_Property1Schema
        elif resource_type == "Communication":
            from spark_fhir_schemas.stu3.complex_types.communication import (
                CommunicationSchema,
            )

            return CommunicationSchema
        elif resource_type == "Communication_Payload":
            from spark_fhir_schemas.stu3.complex_types.communication_payload import (
                Communication_PayloadSchema,
            )

            return Communication_PayloadSchema
        elif resource_type == "CommunicationRequest":
            from spark_fhir_schemas.stu3.complex_types.communicationrequest import (
                CommunicationRequestSchema,
            )

            return CommunicationRequestSchema
        elif resource_type == "CommunicationRequest_Payload":
            from spark_fhir_schemas.stu3.complex_types.communicationrequest_payload import (
                CommunicationRequest_PayloadSchema,
            )

            return CommunicationRequest_PayloadSchema
        elif resource_type == "CommunicationRequest_Requester":
            from spark_fhir_schemas.stu3.complex_types.communicationrequest_requester import (
                CommunicationRequest_RequesterSchema,
            )

            return CommunicationRequest_RequesterSchema
        elif resource_type == "CompartmentDefinition":
            from spark_fhir_schemas.stu3.complex_types.compartmentdefinition import (
                CompartmentDefinitionSchema,
            )

            return CompartmentDefinitionSchema
        elif resource_type == "CompartmentDefinition_Resource":
            from spark_fhir_schemas.stu3.complex_types.compartmentdefinition_resource import (
                CompartmentDefinition_ResourceSchema,
            )

            return CompartmentDefinition_ResourceSchema
        elif resource_type == "Composition":
            from spark_fhir_schemas.stu3.complex_types.composition import (
                CompositionSchema,
            )

            return CompositionSchema
        elif resource_type == "Composition_Attester":
            from spark_fhir_schemas.stu3.complex_types.composition_attester import (
                Composition_AttesterSchema,
            )

            return Composition_AttesterSchema
        elif resource_type == "Composition_RelatesTo":
            from spark_fhir_schemas.stu3.complex_types.composition_relatesto import (
                Composition_RelatesToSchema,
            )

            return Composition_RelatesToSchema
        elif resource_type == "Composition_Event":
            from spark_fhir_schemas.stu3.complex_types.composition_event import (
                Composition_EventSchema,
            )

            return Composition_EventSchema
        elif resource_type == "Composition_Section":
            from spark_fhir_schemas.stu3.complex_types.composition_section import (
                Composition_SectionSchema,
            )

            return Composition_SectionSchema
        elif resource_type == "ConceptMap":
            from spark_fhir_schemas.stu3.complex_types.conceptmap import (
                ConceptMapSchema,
            )

            return ConceptMapSchema
        elif resource_type == "ConceptMap_Group":
            from spark_fhir_schemas.stu3.complex_types.conceptmap_group import (
                ConceptMap_GroupSchema,
            )

            return ConceptMap_GroupSchema
        elif resource_type == "ConceptMap_Element":
            from spark_fhir_schemas.stu3.complex_types.conceptmap_element import (
                ConceptMap_ElementSchema,
            )

            return ConceptMap_ElementSchema
        elif resource_type == "ConceptMap_Target":
            from spark_fhir_schemas.stu3.complex_types.conceptmap_target import (
                ConceptMap_TargetSchema,
            )

            return ConceptMap_TargetSchema
        elif resource_type == "ConceptMap_DependsOn":
            from spark_fhir_schemas.stu3.complex_types.conceptmap_dependson import (
                ConceptMap_DependsOnSchema,
            )

            return ConceptMap_DependsOnSchema
        elif resource_type == "ConceptMap_Unmapped":
            from spark_fhir_schemas.stu3.complex_types.conceptmap_unmapped import (
                ConceptMap_UnmappedSchema,
            )

            return ConceptMap_UnmappedSchema
        elif resource_type == "Condition":
            from spark_fhir_schemas.stu3.complex_types.condition import ConditionSchema

            return ConditionSchema
        elif resource_type == "Condition_Stage":
            from spark_fhir_schemas.stu3.complex_types.condition_stage import (
                Condition_StageSchema,
            )

            return Condition_StageSchema
        elif resource_type == "Condition_Evidence":
            from spark_fhir_schemas.stu3.complex_types.condition_evidence import (
                Condition_EvidenceSchema,
            )

            return Condition_EvidenceSchema
        elif resource_type == "Consent":
            from spark_fhir_schemas.stu3.complex_types.consent import ConsentSchema

            return ConsentSchema
        elif resource_type == "Consent_Actor":
            from spark_fhir_schemas.stu3.complex_types.consent_actor import (
                Consent_ActorSchema,
            )

            return Consent_ActorSchema
        elif resource_type == "Consent_Policy":
            from spark_fhir_schemas.stu3.complex_types.consent_policy import (
                Consent_PolicySchema,
            )

            return Consent_PolicySchema
        elif resource_type == "Consent_Data":
            from spark_fhir_schemas.stu3.complex_types.consent_data import (
                Consent_DataSchema,
            )

            return Consent_DataSchema
        elif resource_type == "Consent_Except":
            from spark_fhir_schemas.stu3.complex_types.consent_except import (
                Consent_ExceptSchema,
            )

            return Consent_ExceptSchema
        elif resource_type == "Consent_Actor1":
            from spark_fhir_schemas.stu3.complex_types.consent_actor1 import (
                Consent_Actor1Schema,
            )

            return Consent_Actor1Schema
        elif resource_type == "Consent_Data1":
            from spark_fhir_schemas.stu3.complex_types.consent_data1 import (
                Consent_Data1Schema,
            )

            return Consent_Data1Schema
        elif resource_type == "Contract":
            from spark_fhir_schemas.stu3.complex_types.contract import ContractSchema

            return ContractSchema
        elif resource_type == "Contract_Agent":
            from spark_fhir_schemas.stu3.complex_types.contract_agent import (
                Contract_AgentSchema,
            )

            return Contract_AgentSchema
        elif resource_type == "Contract_Signer":
            from spark_fhir_schemas.stu3.complex_types.contract_signer import (
                Contract_SignerSchema,
            )

            return Contract_SignerSchema
        elif resource_type == "Contract_ValuedItem":
            from spark_fhir_schemas.stu3.complex_types.contract_valueditem import (
                Contract_ValuedItemSchema,
            )

            return Contract_ValuedItemSchema
        elif resource_type == "Contract_Term":
            from spark_fhir_schemas.stu3.complex_types.contract_term import (
                Contract_TermSchema,
            )

            return Contract_TermSchema
        elif resource_type == "Contract_Agent1":
            from spark_fhir_schemas.stu3.complex_types.contract_agent1 import (
                Contract_Agent1Schema,
            )

            return Contract_Agent1Schema
        elif resource_type == "Contract_ValuedItem1":
            from spark_fhir_schemas.stu3.complex_types.contract_valueditem1 import (
                Contract_ValuedItem1Schema,
            )

            return Contract_ValuedItem1Schema
        elif resource_type == "Contract_Friendly":
            from spark_fhir_schemas.stu3.complex_types.contract_friendly import (
                Contract_FriendlySchema,
            )

            return Contract_FriendlySchema
        elif resource_type == "Contract_Legal":
            from spark_fhir_schemas.stu3.complex_types.contract_legal import (
                Contract_LegalSchema,
            )

            return Contract_LegalSchema
        elif resource_type == "Contract_Rule":
            from spark_fhir_schemas.stu3.complex_types.contract_rule import (
                Contract_RuleSchema,
            )

            return Contract_RuleSchema
        elif resource_type == "Coverage":
            from spark_fhir_schemas.stu3.complex_types.coverage import CoverageSchema

            return CoverageSchema
        elif resource_type == "Coverage_Grouping":
            from spark_fhir_schemas.stu3.complex_types.coverage_grouping import (
                Coverage_GroupingSchema,
            )

            return Coverage_GroupingSchema
        elif resource_type == "DataElement":
            from spark_fhir_schemas.stu3.complex_types.dataelement import (
                DataElementSchema,
            )

            return DataElementSchema
        elif resource_type == "DataElement_Mapping":
            from spark_fhir_schemas.stu3.complex_types.dataelement_mapping import (
                DataElement_MappingSchema,
            )

            return DataElement_MappingSchema
        elif resource_type == "DetectedIssue":
            from spark_fhir_schemas.stu3.complex_types.detectedissue import (
                DetectedIssueSchema,
            )

            return DetectedIssueSchema
        elif resource_type == "DetectedIssue_Mitigation":
            from spark_fhir_schemas.stu3.complex_types.detectedissue_mitigation import (
                DetectedIssue_MitigationSchema,
            )

            return DetectedIssue_MitigationSchema
        elif resource_type == "Device":
            from spark_fhir_schemas.stu3.complex_types.device import DeviceSchema

            return DeviceSchema
        elif resource_type == "Device_Udi":
            from spark_fhir_schemas.stu3.complex_types.device_udi import (
                Device_UdiSchema,
            )

            return Device_UdiSchema
        elif resource_type == "DeviceComponent":
            from spark_fhir_schemas.stu3.complex_types.devicecomponent import (
                DeviceComponentSchema,
            )

            return DeviceComponentSchema
        elif resource_type == "DeviceComponent_ProductionSpecification":
            from spark_fhir_schemas.stu3.complex_types.devicecomponent_productionspecification import (
                DeviceComponent_ProductionSpecificationSchema,
            )

            return DeviceComponent_ProductionSpecificationSchema
        elif resource_type == "DeviceMetric":
            from spark_fhir_schemas.stu3.complex_types.devicemetric import (
                DeviceMetricSchema,
            )

            return DeviceMetricSchema
        elif resource_type == "DeviceMetric_Calibration":
            from spark_fhir_schemas.stu3.complex_types.devicemetric_calibration import (
                DeviceMetric_CalibrationSchema,
            )

            return DeviceMetric_CalibrationSchema
        elif resource_type == "DeviceRequest":
            from spark_fhir_schemas.stu3.complex_types.devicerequest import (
                DeviceRequestSchema,
            )

            return DeviceRequestSchema
        elif resource_type == "DeviceRequest_Requester":
            from spark_fhir_schemas.stu3.complex_types.devicerequest_requester import (
                DeviceRequest_RequesterSchema,
            )

            return DeviceRequest_RequesterSchema
        elif resource_type == "DeviceUseStatement":
            from spark_fhir_schemas.stu3.complex_types.deviceusestatement import (
                DeviceUseStatementSchema,
            )

            return DeviceUseStatementSchema
        elif resource_type == "DiagnosticReport":
            from spark_fhir_schemas.stu3.complex_types.diagnosticreport import (
                DiagnosticReportSchema,
            )

            return DiagnosticReportSchema
        elif resource_type == "DiagnosticReport_Performer":
            from spark_fhir_schemas.stu3.complex_types.diagnosticreport_performer import (
                DiagnosticReport_PerformerSchema,
            )

            return DiagnosticReport_PerformerSchema
        elif resource_type == "DiagnosticReport_Image":
            from spark_fhir_schemas.stu3.complex_types.diagnosticreport_image import (
                DiagnosticReport_ImageSchema,
            )

            return DiagnosticReport_ImageSchema
        elif resource_type == "DocumentManifest":
            from spark_fhir_schemas.stu3.complex_types.documentmanifest import (
                DocumentManifestSchema,
            )

            return DocumentManifestSchema
        elif resource_type == "DocumentManifest_Content":
            from spark_fhir_schemas.stu3.complex_types.documentmanifest_content import (
                DocumentManifest_ContentSchema,
            )

            return DocumentManifest_ContentSchema
        elif resource_type == "DocumentManifest_Related":
            from spark_fhir_schemas.stu3.complex_types.documentmanifest_related import (
                DocumentManifest_RelatedSchema,
            )

            return DocumentManifest_RelatedSchema
        elif resource_type == "DocumentReference":
            from spark_fhir_schemas.stu3.complex_types.documentreference import (
                DocumentReferenceSchema,
            )

            return DocumentReferenceSchema
        elif resource_type == "DocumentReference_RelatesTo":
            from spark_fhir_schemas.stu3.complex_types.documentreference_relatesto import (
                DocumentReference_RelatesToSchema,
            )

            return DocumentReference_RelatesToSchema
        elif resource_type == "DocumentReference_Content":
            from spark_fhir_schemas.stu3.complex_types.documentreference_content import (
                DocumentReference_ContentSchema,
            )

            return DocumentReference_ContentSchema
        elif resource_type == "DocumentReference_Context":
            from spark_fhir_schemas.stu3.complex_types.documentreference_context import (
                DocumentReference_ContextSchema,
            )

            return DocumentReference_ContextSchema
        elif resource_type == "DocumentReference_Related":
            from spark_fhir_schemas.stu3.complex_types.documentreference_related import (
                DocumentReference_RelatedSchema,
            )

            return DocumentReference_RelatedSchema
        elif resource_type == "DomainResource":
            from spark_fhir_schemas.stu3.complex_types.domainresource import (
                DomainResourceSchema,
            )

            return DomainResourceSchema
        elif resource_type == "EligibilityRequest":
            from spark_fhir_schemas.stu3.complex_types.eligibilityrequest import (
                EligibilityRequestSchema,
            )

            return EligibilityRequestSchema
        elif resource_type == "EligibilityResponse":
            from spark_fhir_schemas.stu3.complex_types.eligibilityresponse import (
                EligibilityResponseSchema,
            )

            return EligibilityResponseSchema
        elif resource_type == "EligibilityResponse_Insurance":
            from spark_fhir_schemas.stu3.complex_types.eligibilityresponse_insurance import (
                EligibilityResponse_InsuranceSchema,
            )

            return EligibilityResponse_InsuranceSchema
        elif resource_type == "EligibilityResponse_BenefitBalance":
            from spark_fhir_schemas.stu3.complex_types.eligibilityresponse_benefitbalance import (
                EligibilityResponse_BenefitBalanceSchema,
            )

            return EligibilityResponse_BenefitBalanceSchema
        elif resource_type == "EligibilityResponse_Financial":
            from spark_fhir_schemas.stu3.complex_types.eligibilityresponse_financial import (
                EligibilityResponse_FinancialSchema,
            )

            return EligibilityResponse_FinancialSchema
        elif resource_type == "EligibilityResponse_Error":
            from spark_fhir_schemas.stu3.complex_types.eligibilityresponse_error import (
                EligibilityResponse_ErrorSchema,
            )

            return EligibilityResponse_ErrorSchema
        elif resource_type == "Encounter":
            from spark_fhir_schemas.stu3.complex_types.encounter import EncounterSchema

            return EncounterSchema
        elif resource_type == "Encounter_StatusHistory":
            from spark_fhir_schemas.stu3.complex_types.encounter_statushistory import (
                Encounter_StatusHistorySchema,
            )

            return Encounter_StatusHistorySchema
        elif resource_type == "Encounter_ClassHistory":
            from spark_fhir_schemas.stu3.complex_types.encounter_classhistory import (
                Encounter_ClassHistorySchema,
            )

            return Encounter_ClassHistorySchema
        elif resource_type == "Encounter_Participant":
            from spark_fhir_schemas.stu3.complex_types.encounter_participant import (
                Encounter_ParticipantSchema,
            )

            return Encounter_ParticipantSchema
        elif resource_type == "Encounter_Diagnosis":
            from spark_fhir_schemas.stu3.complex_types.encounter_diagnosis import (
                Encounter_DiagnosisSchema,
            )

            return Encounter_DiagnosisSchema
        elif resource_type == "Encounter_Hospitalization":
            from spark_fhir_schemas.stu3.complex_types.encounter_hospitalization import (
                Encounter_HospitalizationSchema,
            )

            return Encounter_HospitalizationSchema
        elif resource_type == "Encounter_Location":
            from spark_fhir_schemas.stu3.complex_types.encounter_location import (
                Encounter_LocationSchema,
            )

            return Encounter_LocationSchema
        elif resource_type == "Endpoint":
            from spark_fhir_schemas.stu3.complex_types.endpoint import EndpointSchema

            return EndpointSchema
        elif resource_type == "EnrollmentRequest":
            from spark_fhir_schemas.stu3.complex_types.enrollmentrequest import (
                EnrollmentRequestSchema,
            )

            return EnrollmentRequestSchema
        elif resource_type == "EnrollmentResponse":
            from spark_fhir_schemas.stu3.complex_types.enrollmentresponse import (
                EnrollmentResponseSchema,
            )

            return EnrollmentResponseSchema
        elif resource_type == "EpisodeOfCare":
            from spark_fhir_schemas.stu3.complex_types.episodeofcare import (
                EpisodeOfCareSchema,
            )

            return EpisodeOfCareSchema
        elif resource_type == "EpisodeOfCare_StatusHistory":
            from spark_fhir_schemas.stu3.complex_types.episodeofcare_statushistory import (
                EpisodeOfCare_StatusHistorySchema,
            )

            return EpisodeOfCare_StatusHistorySchema
        elif resource_type == "EpisodeOfCare_Diagnosis":
            from spark_fhir_schemas.stu3.complex_types.episodeofcare_diagnosis import (
                EpisodeOfCare_DiagnosisSchema,
            )

            return EpisodeOfCare_DiagnosisSchema
        elif resource_type == "ExpansionProfile":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile import (
                ExpansionProfileSchema,
            )

            return ExpansionProfileSchema
        elif resource_type == "ExpansionProfile_FixedVersion":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_fixedversion import (
                ExpansionProfile_FixedVersionSchema,
            )

            return ExpansionProfile_FixedVersionSchema
        elif resource_type == "ExpansionProfile_ExcludedSystem":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_excludedsystem import (
                ExpansionProfile_ExcludedSystemSchema,
            )

            return ExpansionProfile_ExcludedSystemSchema
        elif resource_type == "ExpansionProfile_Designation":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_designation import (
                ExpansionProfile_DesignationSchema,
            )

            return ExpansionProfile_DesignationSchema
        elif resource_type == "ExpansionProfile_Include":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_include import (
                ExpansionProfile_IncludeSchema,
            )

            return ExpansionProfile_IncludeSchema
        elif resource_type == "ExpansionProfile_Designation1":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_designation1 import (
                ExpansionProfile_Designation1Schema,
            )

            return ExpansionProfile_Designation1Schema
        elif resource_type == "ExpansionProfile_Exclude":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_exclude import (
                ExpansionProfile_ExcludeSchema,
            )

            return ExpansionProfile_ExcludeSchema
        elif resource_type == "ExpansionProfile_Designation2":
            from spark_fhir_schemas.stu3.complex_types.expansionprofile_designation2 import (
                ExpansionProfile_Designation2Schema,
            )

            return ExpansionProfile_Designation2Schema
        elif resource_type == "ExplanationOfBenefit":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit import (
                ExplanationOfBenefitSchema,
            )

            return ExplanationOfBenefitSchema
        elif resource_type == "ExplanationOfBenefit_Related":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_related import (
                ExplanationOfBenefit_RelatedSchema,
            )

            return ExplanationOfBenefit_RelatedSchema
        elif resource_type == "ExplanationOfBenefit_Payee":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_payee import (
                ExplanationOfBenefit_PayeeSchema,
            )

            return ExplanationOfBenefit_PayeeSchema
        elif resource_type == "ExplanationOfBenefit_Information":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_information import (
                ExplanationOfBenefit_InformationSchema,
            )

            return ExplanationOfBenefit_InformationSchema
        elif resource_type == "ExplanationOfBenefit_CareTeam":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_careteam import (
                ExplanationOfBenefit_CareTeamSchema,
            )

            return ExplanationOfBenefit_CareTeamSchema
        elif resource_type == "ExplanationOfBenefit_Diagnosis":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_diagnosis import (
                ExplanationOfBenefit_DiagnosisSchema,
            )

            return ExplanationOfBenefit_DiagnosisSchema
        elif resource_type == "ExplanationOfBenefit_Procedure":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_procedure import (
                ExplanationOfBenefit_ProcedureSchema,
            )

            return ExplanationOfBenefit_ProcedureSchema
        elif resource_type == "ExplanationOfBenefit_Insurance":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_insurance import (
                ExplanationOfBenefit_InsuranceSchema,
            )

            return ExplanationOfBenefit_InsuranceSchema
        elif resource_type == "ExplanationOfBenefit_Accident":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_accident import (
                ExplanationOfBenefit_AccidentSchema,
            )

            return ExplanationOfBenefit_AccidentSchema
        elif resource_type == "ExplanationOfBenefit_Item":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_item import (
                ExplanationOfBenefit_ItemSchema,
            )

            return ExplanationOfBenefit_ItemSchema
        elif resource_type == "ExplanationOfBenefit_Adjudication":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_adjudication import (
                ExplanationOfBenefit_AdjudicationSchema,
            )

            return ExplanationOfBenefit_AdjudicationSchema
        elif resource_type == "ExplanationOfBenefit_Detail":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_detail import (
                ExplanationOfBenefit_DetailSchema,
            )

            return ExplanationOfBenefit_DetailSchema
        elif resource_type == "ExplanationOfBenefit_SubDetail":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_subdetail import (
                ExplanationOfBenefit_SubDetailSchema,
            )

            return ExplanationOfBenefit_SubDetailSchema
        elif resource_type == "ExplanationOfBenefit_AddItem":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_additem import (
                ExplanationOfBenefit_AddItemSchema,
            )

            return ExplanationOfBenefit_AddItemSchema
        elif resource_type == "ExplanationOfBenefit_Detail1":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_detail1 import (
                ExplanationOfBenefit_Detail1Schema,
            )

            return ExplanationOfBenefit_Detail1Schema
        elif resource_type == "ExplanationOfBenefit_Payment":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_payment import (
                ExplanationOfBenefit_PaymentSchema,
            )

            return ExplanationOfBenefit_PaymentSchema
        elif resource_type == "ExplanationOfBenefit_ProcessNote":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_processnote import (
                ExplanationOfBenefit_ProcessNoteSchema,
            )

            return ExplanationOfBenefit_ProcessNoteSchema
        elif resource_type == "ExplanationOfBenefit_BenefitBalance":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_benefitbalance import (
                ExplanationOfBenefit_BenefitBalanceSchema,
            )

            return ExplanationOfBenefit_BenefitBalanceSchema
        elif resource_type == "ExplanationOfBenefit_Financial":
            from spark_fhir_schemas.stu3.complex_types.explanationofbenefit_financial import (
                ExplanationOfBenefit_FinancialSchema,
            )

            return ExplanationOfBenefit_FinancialSchema
        elif resource_type == "FamilyMemberHistory":
            from spark_fhir_schemas.stu3.complex_types.familymemberhistory import (
                FamilyMemberHistorySchema,
            )

            return FamilyMemberHistorySchema
        elif resource_type == "FamilyMemberHistory_Condition":
            from spark_fhir_schemas.stu3.complex_types.familymemberhistory_condition import (
                FamilyMemberHistory_ConditionSchema,
            )

            return FamilyMemberHistory_ConditionSchema
        elif resource_type == "Flag":
            from spark_fhir_schemas.stu3.complex_types.flag import FlagSchema

            return FlagSchema
        elif resource_type == "Goal":
            from spark_fhir_schemas.stu3.complex_types.goal import GoalSchema

            return GoalSchema
        elif resource_type == "Goal_Target":
            from spark_fhir_schemas.stu3.complex_types.goal_target import (
                Goal_TargetSchema,
            )

            return Goal_TargetSchema
        elif resource_type == "GraphDefinition":
            from spark_fhir_schemas.stu3.complex_types.graphdefinition import (
                GraphDefinitionSchema,
            )

            return GraphDefinitionSchema
        elif resource_type == "GraphDefinition_Link":
            from spark_fhir_schemas.stu3.complex_types.graphdefinition_link import (
                GraphDefinition_LinkSchema,
            )

            return GraphDefinition_LinkSchema
        elif resource_type == "GraphDefinition_Target":
            from spark_fhir_schemas.stu3.complex_types.graphdefinition_target import (
                GraphDefinition_TargetSchema,
            )

            return GraphDefinition_TargetSchema
        elif resource_type == "GraphDefinition_Compartment":
            from spark_fhir_schemas.stu3.complex_types.graphdefinition_compartment import (
                GraphDefinition_CompartmentSchema,
            )

            return GraphDefinition_CompartmentSchema
        elif resource_type == "Group":
            from spark_fhir_schemas.stu3.complex_types.group import GroupSchema

            return GroupSchema
        elif resource_type == "Group_Characteristic":
            from spark_fhir_schemas.stu3.complex_types.group_characteristic import (
                Group_CharacteristicSchema,
            )

            return Group_CharacteristicSchema
        elif resource_type == "Group_Member":
            from spark_fhir_schemas.stu3.complex_types.group_member import (
                Group_MemberSchema,
            )

            return Group_MemberSchema
        elif resource_type == "GuidanceResponse":
            from spark_fhir_schemas.stu3.complex_types.guidanceresponse import (
                GuidanceResponseSchema,
            )

            return GuidanceResponseSchema
        elif resource_type == "HealthcareService":
            from spark_fhir_schemas.stu3.complex_types.healthcareservice import (
                HealthcareServiceSchema,
            )

            return HealthcareServiceSchema
        elif resource_type == "HealthcareService_AvailableTime":
            from spark_fhir_schemas.stu3.complex_types.healthcareservice_availabletime import (
                HealthcareService_AvailableTimeSchema,
            )

            return HealthcareService_AvailableTimeSchema
        elif resource_type == "HealthcareService_NotAvailable":
            from spark_fhir_schemas.stu3.complex_types.healthcareservice_notavailable import (
                HealthcareService_NotAvailableSchema,
            )

            return HealthcareService_NotAvailableSchema
        elif resource_type == "ImagingManifest":
            from spark_fhir_schemas.stu3.complex_types.imagingmanifest import (
                ImagingManifestSchema,
            )

            return ImagingManifestSchema
        elif resource_type == "ImagingManifest_Study":
            from spark_fhir_schemas.stu3.complex_types.imagingmanifest_study import (
                ImagingManifest_StudySchema,
            )

            return ImagingManifest_StudySchema
        elif resource_type == "ImagingManifest_Series":
            from spark_fhir_schemas.stu3.complex_types.imagingmanifest_series import (
                ImagingManifest_SeriesSchema,
            )

            return ImagingManifest_SeriesSchema
        elif resource_type == "ImagingManifest_Instance":
            from spark_fhir_schemas.stu3.complex_types.imagingmanifest_instance import (
                ImagingManifest_InstanceSchema,
            )

            return ImagingManifest_InstanceSchema
        elif resource_type == "ImagingStudy":
            from spark_fhir_schemas.stu3.complex_types.imagingstudy import (
                ImagingStudySchema,
            )

            return ImagingStudySchema
        elif resource_type == "ImagingStudy_Series":
            from spark_fhir_schemas.stu3.complex_types.imagingstudy_series import (
                ImagingStudy_SeriesSchema,
            )

            return ImagingStudy_SeriesSchema
        elif resource_type == "ImagingStudy_Instance":
            from spark_fhir_schemas.stu3.complex_types.imagingstudy_instance import (
                ImagingStudy_InstanceSchema,
            )

            return ImagingStudy_InstanceSchema
        elif resource_type == "Immunization":
            from spark_fhir_schemas.stu3.complex_types.immunization import (
                ImmunizationSchema,
            )

            return ImmunizationSchema
        elif resource_type == "Immunization_Practitioner":
            from spark_fhir_schemas.stu3.complex_types.immunization_practitioner import (
                Immunization_PractitionerSchema,
            )

            return Immunization_PractitionerSchema
        elif resource_type == "Immunization_Explanation":
            from spark_fhir_schemas.stu3.complex_types.immunization_explanation import (
                Immunization_ExplanationSchema,
            )

            return Immunization_ExplanationSchema
        elif resource_type == "Immunization_Reaction":
            from spark_fhir_schemas.stu3.complex_types.immunization_reaction import (
                Immunization_ReactionSchema,
            )

            return Immunization_ReactionSchema
        elif resource_type == "Immunization_VaccinationProtocol":
            from spark_fhir_schemas.stu3.complex_types.immunization_vaccinationprotocol import (
                Immunization_VaccinationProtocolSchema,
            )

            return Immunization_VaccinationProtocolSchema
        elif resource_type == "ImmunizationRecommendation":
            from spark_fhir_schemas.stu3.complex_types.immunizationrecommendation import (
                ImmunizationRecommendationSchema,
            )

            return ImmunizationRecommendationSchema
        elif resource_type == "ImmunizationRecommendation_Recommendation":
            from spark_fhir_schemas.stu3.complex_types.immunizationrecommendation_recommendation import (
                ImmunizationRecommendation_RecommendationSchema,
            )

            return ImmunizationRecommendation_RecommendationSchema
        elif resource_type == "ImmunizationRecommendation_DateCriterion":
            from spark_fhir_schemas.stu3.complex_types.immunizationrecommendation_datecriterion import (
                ImmunizationRecommendation_DateCriterionSchema,
            )

            return ImmunizationRecommendation_DateCriterionSchema
        elif resource_type == "ImmunizationRecommendation_Protocol":
            from spark_fhir_schemas.stu3.complex_types.immunizationrecommendation_protocol import (
                ImmunizationRecommendation_ProtocolSchema,
            )

            return ImmunizationRecommendation_ProtocolSchema
        elif resource_type == "ImplementationGuide":
            from spark_fhir_schemas.stu3.complex_types.implementationguide import (
                ImplementationGuideSchema,
            )

            return ImplementationGuideSchema
        elif resource_type == "ImplementationGuide_Dependency":
            from spark_fhir_schemas.stu3.complex_types.implementationguide_dependency import (
                ImplementationGuide_DependencySchema,
            )

            return ImplementationGuide_DependencySchema
        elif resource_type == "ImplementationGuide_Package":
            from spark_fhir_schemas.stu3.complex_types.implementationguide_package import (
                ImplementationGuide_PackageSchema,
            )

            return ImplementationGuide_PackageSchema
        elif resource_type == "ImplementationGuide_Resource":
            from spark_fhir_schemas.stu3.complex_types.implementationguide_resource import (
                ImplementationGuide_ResourceSchema,
            )

            return ImplementationGuide_ResourceSchema
        elif resource_type == "ImplementationGuide_Global":
            from spark_fhir_schemas.stu3.complex_types.implementationguide_global import (
                ImplementationGuide_GlobalSchema,
            )

            return ImplementationGuide_GlobalSchema
        elif resource_type == "ImplementationGuide_Page":
            from spark_fhir_schemas.stu3.complex_types.implementationguide_page import (
                ImplementationGuide_PageSchema,
            )

            return ImplementationGuide_PageSchema
        elif resource_type == "Library":
            from spark_fhir_schemas.stu3.complex_types.library import LibrarySchema

            return LibrarySchema
        elif resource_type == "Linkage":
            from spark_fhir_schemas.stu3.complex_types.linkage import LinkageSchema

            return LinkageSchema
        elif resource_type == "Linkage_Item":
            from spark_fhir_schemas.stu3.complex_types.linkage_item import (
                Linkage_ItemSchema,
            )

            return Linkage_ItemSchema
        elif resource_type == "List":
            from spark_fhir_schemas.stu3.complex_types.list import ListSchema

            return ListSchema
        elif resource_type == "List_Entry":
            from spark_fhir_schemas.stu3.complex_types.list_entry import (
                List_EntrySchema,
            )

            return List_EntrySchema
        elif resource_type == "Location":
            from spark_fhir_schemas.stu3.complex_types.location import LocationSchema

            return LocationSchema
        elif resource_type == "Location_Position":
            from spark_fhir_schemas.stu3.complex_types.location_position import (
                Location_PositionSchema,
            )

            return Location_PositionSchema
        elif resource_type == "Measure":
            from spark_fhir_schemas.stu3.complex_types.measure import MeasureSchema

            return MeasureSchema
        elif resource_type == "Measure_Group":
            from spark_fhir_schemas.stu3.complex_types.measure_group import (
                Measure_GroupSchema,
            )

            return Measure_GroupSchema
        elif resource_type == "Measure_Population":
            from spark_fhir_schemas.stu3.complex_types.measure_population import (
                Measure_PopulationSchema,
            )

            return Measure_PopulationSchema
        elif resource_type == "Measure_Stratifier":
            from spark_fhir_schemas.stu3.complex_types.measure_stratifier import (
                Measure_StratifierSchema,
            )

            return Measure_StratifierSchema
        elif resource_type == "Measure_SupplementalData":
            from spark_fhir_schemas.stu3.complex_types.measure_supplementaldata import (
                Measure_SupplementalDataSchema,
            )

            return Measure_SupplementalDataSchema
        elif resource_type == "MeasureReport":
            from spark_fhir_schemas.stu3.complex_types.measurereport import (
                MeasureReportSchema,
            )

            return MeasureReportSchema
        elif resource_type == "MeasureReport_Group":
            from spark_fhir_schemas.stu3.complex_types.measurereport_group import (
                MeasureReport_GroupSchema,
            )

            return MeasureReport_GroupSchema
        elif resource_type == "MeasureReport_Population":
            from spark_fhir_schemas.stu3.complex_types.measurereport_population import (
                MeasureReport_PopulationSchema,
            )

            return MeasureReport_PopulationSchema
        elif resource_type == "MeasureReport_Stratifier":
            from spark_fhir_schemas.stu3.complex_types.measurereport_stratifier import (
                MeasureReport_StratifierSchema,
            )

            return MeasureReport_StratifierSchema
        elif resource_type == "MeasureReport_Stratum":
            from spark_fhir_schemas.stu3.complex_types.measurereport_stratum import (
                MeasureReport_StratumSchema,
            )

            return MeasureReport_StratumSchema
        elif resource_type == "MeasureReport_Population1":
            from spark_fhir_schemas.stu3.complex_types.measurereport_population1 import (
                MeasureReport_Population1Schema,
            )

            return MeasureReport_Population1Schema
        elif resource_type == "Media":
            from spark_fhir_schemas.stu3.complex_types.media import MediaSchema

            return MediaSchema
        elif resource_type == "Medication":
            from spark_fhir_schemas.stu3.complex_types.medication import (
                MedicationSchema,
            )

            return MedicationSchema
        elif resource_type == "Medication_Ingredient":
            from spark_fhir_schemas.stu3.complex_types.medication_ingredient import (
                Medication_IngredientSchema,
            )

            return Medication_IngredientSchema
        elif resource_type == "Medication_Package":
            from spark_fhir_schemas.stu3.complex_types.medication_package import (
                Medication_PackageSchema,
            )

            return Medication_PackageSchema
        elif resource_type == "Medication_Content":
            from spark_fhir_schemas.stu3.complex_types.medication_content import (
                Medication_ContentSchema,
            )

            return Medication_ContentSchema
        elif resource_type == "Medication_Batch":
            from spark_fhir_schemas.stu3.complex_types.medication_batch import (
                Medication_BatchSchema,
            )

            return Medication_BatchSchema
        elif resource_type == "MedicationAdministration":
            from spark_fhir_schemas.stu3.complex_types.medicationadministration import (
                MedicationAdministrationSchema,
            )

            return MedicationAdministrationSchema
        elif resource_type == "MedicationAdministration_Performer":
            from spark_fhir_schemas.stu3.complex_types.medicationadministration_performer import (
                MedicationAdministration_PerformerSchema,
            )

            return MedicationAdministration_PerformerSchema
        elif resource_type == "MedicationAdministration_Dosage":
            from spark_fhir_schemas.stu3.complex_types.medicationadministration_dosage import (
                MedicationAdministration_DosageSchema,
            )

            return MedicationAdministration_DosageSchema
        elif resource_type == "MedicationDispense":
            from spark_fhir_schemas.stu3.complex_types.medicationdispense import (
                MedicationDispenseSchema,
            )

            return MedicationDispenseSchema
        elif resource_type == "MedicationDispense_Performer":
            from spark_fhir_schemas.stu3.complex_types.medicationdispense_performer import (
                MedicationDispense_PerformerSchema,
            )

            return MedicationDispense_PerformerSchema
        elif resource_type == "MedicationDispense_Substitution":
            from spark_fhir_schemas.stu3.complex_types.medicationdispense_substitution import (
                MedicationDispense_SubstitutionSchema,
            )

            return MedicationDispense_SubstitutionSchema
        elif resource_type == "MedicationRequest":
            from spark_fhir_schemas.stu3.complex_types.medicationrequest import (
                MedicationRequestSchema,
            )

            return MedicationRequestSchema
        elif resource_type == "MedicationRequest_Requester":
            from spark_fhir_schemas.stu3.complex_types.medicationrequest_requester import (
                MedicationRequest_RequesterSchema,
            )

            return MedicationRequest_RequesterSchema
        elif resource_type == "MedicationRequest_DispenseRequest":
            from spark_fhir_schemas.stu3.complex_types.medicationrequest_dispenserequest import (
                MedicationRequest_DispenseRequestSchema,
            )

            return MedicationRequest_DispenseRequestSchema
        elif resource_type == "MedicationRequest_Substitution":
            from spark_fhir_schemas.stu3.complex_types.medicationrequest_substitution import (
                MedicationRequest_SubstitutionSchema,
            )

            return MedicationRequest_SubstitutionSchema
        elif resource_type == "MedicationStatement":
            from spark_fhir_schemas.stu3.complex_types.medicationstatement import (
                MedicationStatementSchema,
            )

            return MedicationStatementSchema
        elif resource_type == "MessageDefinition":
            from spark_fhir_schemas.stu3.complex_types.messagedefinition import (
                MessageDefinitionSchema,
            )

            return MessageDefinitionSchema
        elif resource_type == "MessageDefinition_Focus":
            from spark_fhir_schemas.stu3.complex_types.messagedefinition_focus import (
                MessageDefinition_FocusSchema,
            )

            return MessageDefinition_FocusSchema
        elif resource_type == "MessageDefinition_AllowedResponse":
            from spark_fhir_schemas.stu3.complex_types.messagedefinition_allowedresponse import (
                MessageDefinition_AllowedResponseSchema,
            )

            return MessageDefinition_AllowedResponseSchema
        elif resource_type == "MessageHeader":
            from spark_fhir_schemas.stu3.complex_types.messageheader import (
                MessageHeaderSchema,
            )

            return MessageHeaderSchema
        elif resource_type == "MessageHeader_Destination":
            from spark_fhir_schemas.stu3.complex_types.messageheader_destination import (
                MessageHeader_DestinationSchema,
            )

            return MessageHeader_DestinationSchema
        elif resource_type == "MessageHeader_Source":
            from spark_fhir_schemas.stu3.complex_types.messageheader_source import (
                MessageHeader_SourceSchema,
            )

            return MessageHeader_SourceSchema
        elif resource_type == "MessageHeader_Response":
            from spark_fhir_schemas.stu3.complex_types.messageheader_response import (
                MessageHeader_ResponseSchema,
            )

            return MessageHeader_ResponseSchema
        elif resource_type == "NamingSystem":
            from spark_fhir_schemas.stu3.complex_types.namingsystem import (
                NamingSystemSchema,
            )

            return NamingSystemSchema
        elif resource_type == "NamingSystem_UniqueId":
            from spark_fhir_schemas.stu3.complex_types.namingsystem_uniqueid import (
                NamingSystem_UniqueIdSchema,
            )

            return NamingSystem_UniqueIdSchema
        elif resource_type == "NutritionOrder":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder import (
                NutritionOrderSchema,
            )

            return NutritionOrderSchema
        elif resource_type == "NutritionOrder_OralDiet":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder_oraldiet import (
                NutritionOrder_OralDietSchema,
            )

            return NutritionOrder_OralDietSchema
        elif resource_type == "NutritionOrder_Nutrient":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder_nutrient import (
                NutritionOrder_NutrientSchema,
            )

            return NutritionOrder_NutrientSchema
        elif resource_type == "NutritionOrder_Texture":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder_texture import (
                NutritionOrder_TextureSchema,
            )

            return NutritionOrder_TextureSchema
        elif resource_type == "NutritionOrder_Supplement":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder_supplement import (
                NutritionOrder_SupplementSchema,
            )

            return NutritionOrder_SupplementSchema
        elif resource_type == "NutritionOrder_EnteralFormula":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder_enteralformula import (
                NutritionOrder_EnteralFormulaSchema,
            )

            return NutritionOrder_EnteralFormulaSchema
        elif resource_type == "NutritionOrder_Administration":
            from spark_fhir_schemas.stu3.complex_types.nutritionorder_administration import (
                NutritionOrder_AdministrationSchema,
            )

            return NutritionOrder_AdministrationSchema
        elif resource_type == "Observation":
            from spark_fhir_schemas.stu3.complex_types.observation import (
                ObservationSchema,
            )

            return ObservationSchema
        elif resource_type == "Observation_ReferenceRange":
            from spark_fhir_schemas.stu3.complex_types.observation_referencerange import (
                Observation_ReferenceRangeSchema,
            )

            return Observation_ReferenceRangeSchema
        elif resource_type == "Observation_Related":
            from spark_fhir_schemas.stu3.complex_types.observation_related import (
                Observation_RelatedSchema,
            )

            return Observation_RelatedSchema
        elif resource_type == "Observation_Component":
            from spark_fhir_schemas.stu3.complex_types.observation_component import (
                Observation_ComponentSchema,
            )

            return Observation_ComponentSchema
        elif resource_type == "OperationDefinition":
            from spark_fhir_schemas.stu3.complex_types.operationdefinition import (
                OperationDefinitionSchema,
            )

            return OperationDefinitionSchema
        elif resource_type == "OperationDefinition_Parameter":
            from spark_fhir_schemas.stu3.complex_types.operationdefinition_parameter import (
                OperationDefinition_ParameterSchema,
            )

            return OperationDefinition_ParameterSchema
        elif resource_type == "OperationDefinition_Binding":
            from spark_fhir_schemas.stu3.complex_types.operationdefinition_binding import (
                OperationDefinition_BindingSchema,
            )

            return OperationDefinition_BindingSchema
        elif resource_type == "OperationDefinition_Overload":
            from spark_fhir_schemas.stu3.complex_types.operationdefinition_overload import (
                OperationDefinition_OverloadSchema,
            )

            return OperationDefinition_OverloadSchema
        elif resource_type == "OperationOutcome":
            from spark_fhir_schemas.stu3.complex_types.operationoutcome import (
                OperationOutcomeSchema,
            )

            return OperationOutcomeSchema
        elif resource_type == "OperationOutcome_Issue":
            from spark_fhir_schemas.stu3.complex_types.operationoutcome_issue import (
                OperationOutcome_IssueSchema,
            )

            return OperationOutcome_IssueSchema
        elif resource_type == "Organization":
            from spark_fhir_schemas.stu3.complex_types.organization import (
                OrganizationSchema,
            )

            return OrganizationSchema
        elif resource_type == "Organization_Contact":
            from spark_fhir_schemas.stu3.complex_types.organization_contact import (
                Organization_ContactSchema,
            )

            return Organization_ContactSchema
        elif resource_type == "Parameters":
            from spark_fhir_schemas.stu3.complex_types.parameters import (
                ParametersSchema,
            )

            return ParametersSchema
        elif resource_type == "Parameters_Parameter":
            from spark_fhir_schemas.stu3.complex_types.parameters_parameter import (
                Parameters_ParameterSchema,
            )

            return Parameters_ParameterSchema
        elif resource_type == "Patient":
            from spark_fhir_schemas.stu3.complex_types.patient import PatientSchema

            return PatientSchema
        elif resource_type == "Patient_Contact":
            from spark_fhir_schemas.stu3.complex_types.patient_contact import (
                Patient_ContactSchema,
            )

            return Patient_ContactSchema
        elif resource_type == "Patient_Animal":
            from spark_fhir_schemas.stu3.complex_types.patient_animal import (
                Patient_AnimalSchema,
            )

            return Patient_AnimalSchema
        elif resource_type == "Patient_Communication":
            from spark_fhir_schemas.stu3.complex_types.patient_communication import (
                Patient_CommunicationSchema,
            )

            return Patient_CommunicationSchema
        elif resource_type == "Patient_Link":
            from spark_fhir_schemas.stu3.complex_types.patient_link import (
                Patient_LinkSchema,
            )

            return Patient_LinkSchema
        elif resource_type == "PaymentNotice":
            from spark_fhir_schemas.stu3.complex_types.paymentnotice import (
                PaymentNoticeSchema,
            )

            return PaymentNoticeSchema
        elif resource_type == "PaymentReconciliation":
            from spark_fhir_schemas.stu3.complex_types.paymentreconciliation import (
                PaymentReconciliationSchema,
            )

            return PaymentReconciliationSchema
        elif resource_type == "PaymentReconciliation_Detail":
            from spark_fhir_schemas.stu3.complex_types.paymentreconciliation_detail import (
                PaymentReconciliation_DetailSchema,
            )

            return PaymentReconciliation_DetailSchema
        elif resource_type == "PaymentReconciliation_ProcessNote":
            from spark_fhir_schemas.stu3.complex_types.paymentreconciliation_processnote import (
                PaymentReconciliation_ProcessNoteSchema,
            )

            return PaymentReconciliation_ProcessNoteSchema
        elif resource_type == "Person":
            from spark_fhir_schemas.stu3.complex_types.person import PersonSchema

            return PersonSchema
        elif resource_type == "Person_Link":
            from spark_fhir_schemas.stu3.complex_types.person_link import (
                Person_LinkSchema,
            )

            return Person_LinkSchema
        elif resource_type == "PlanDefinition":
            from spark_fhir_schemas.stu3.complex_types.plandefinition import (
                PlanDefinitionSchema,
            )

            return PlanDefinitionSchema
        elif resource_type == "PlanDefinition_Goal":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_goal import (
                PlanDefinition_GoalSchema,
            )

            return PlanDefinition_GoalSchema
        elif resource_type == "PlanDefinition_Target":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_target import (
                PlanDefinition_TargetSchema,
            )

            return PlanDefinition_TargetSchema
        elif resource_type == "PlanDefinition_Action":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_action import (
                PlanDefinition_ActionSchema,
            )

            return PlanDefinition_ActionSchema
        elif resource_type == "PlanDefinition_Condition":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_condition import (
                PlanDefinition_ConditionSchema,
            )

            return PlanDefinition_ConditionSchema
        elif resource_type == "PlanDefinition_RelatedAction":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_relatedaction import (
                PlanDefinition_RelatedActionSchema,
            )

            return PlanDefinition_RelatedActionSchema
        elif resource_type == "PlanDefinition_Participant":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_participant import (
                PlanDefinition_ParticipantSchema,
            )

            return PlanDefinition_ParticipantSchema
        elif resource_type == "PlanDefinition_DynamicValue":
            from spark_fhir_schemas.stu3.complex_types.plandefinition_dynamicvalue import (
                PlanDefinition_DynamicValueSchema,
            )

            return PlanDefinition_DynamicValueSchema
        elif resource_type == "Practitioner":
            from spark_fhir_schemas.stu3.complex_types.practitioner import (
                PractitionerSchema,
            )

            return PractitionerSchema
        elif resource_type == "Practitioner_Qualification":
            from spark_fhir_schemas.stu3.complex_types.practitioner_qualification import (
                Practitioner_QualificationSchema,
            )

            return Practitioner_QualificationSchema
        elif resource_type == "PractitionerRole":
            from spark_fhir_schemas.stu3.complex_types.practitionerrole import (
                PractitionerRoleSchema,
            )

            return PractitionerRoleSchema
        elif resource_type == "PractitionerRole_AvailableTime":
            from spark_fhir_schemas.stu3.complex_types.practitionerrole_availabletime import (
                PractitionerRole_AvailableTimeSchema,
            )

            return PractitionerRole_AvailableTimeSchema
        elif resource_type == "PractitionerRole_NotAvailable":
            from spark_fhir_schemas.stu3.complex_types.practitionerrole_notavailable import (
                PractitionerRole_NotAvailableSchema,
            )

            return PractitionerRole_NotAvailableSchema
        elif resource_type == "Procedure":
            from spark_fhir_schemas.stu3.complex_types.procedure import ProcedureSchema

            return ProcedureSchema
        elif resource_type == "Procedure_Performer":
            from spark_fhir_schemas.stu3.complex_types.procedure_performer import (
                Procedure_PerformerSchema,
            )

            return Procedure_PerformerSchema
        elif resource_type == "Procedure_FocalDevice":
            from spark_fhir_schemas.stu3.complex_types.procedure_focaldevice import (
                Procedure_FocalDeviceSchema,
            )

            return Procedure_FocalDeviceSchema
        elif resource_type == "ProcedureRequest":
            from spark_fhir_schemas.stu3.complex_types.procedurerequest import (
                ProcedureRequestSchema,
            )

            return ProcedureRequestSchema
        elif resource_type == "ProcedureRequest_Requester":
            from spark_fhir_schemas.stu3.complex_types.procedurerequest_requester import (
                ProcedureRequest_RequesterSchema,
            )

            return ProcedureRequest_RequesterSchema
        elif resource_type == "ProcessRequest":
            from spark_fhir_schemas.stu3.complex_types.processrequest import (
                ProcessRequestSchema,
            )

            return ProcessRequestSchema
        elif resource_type == "ProcessRequest_Item":
            from spark_fhir_schemas.stu3.complex_types.processrequest_item import (
                ProcessRequest_ItemSchema,
            )

            return ProcessRequest_ItemSchema
        elif resource_type == "ProcessResponse":
            from spark_fhir_schemas.stu3.complex_types.processresponse import (
                ProcessResponseSchema,
            )

            return ProcessResponseSchema
        elif resource_type == "ProcessResponse_ProcessNote":
            from spark_fhir_schemas.stu3.complex_types.processresponse_processnote import (
                ProcessResponse_ProcessNoteSchema,
            )

            return ProcessResponse_ProcessNoteSchema
        elif resource_type == "Provenance":
            from spark_fhir_schemas.stu3.complex_types.provenance import (
                ProvenanceSchema,
            )

            return ProvenanceSchema
        elif resource_type == "Provenance_Agent":
            from spark_fhir_schemas.stu3.complex_types.provenance_agent import (
                Provenance_AgentSchema,
            )

            return Provenance_AgentSchema
        elif resource_type == "Provenance_Entity":
            from spark_fhir_schemas.stu3.complex_types.provenance_entity import (
                Provenance_EntitySchema,
            )

            return Provenance_EntitySchema
        elif resource_type == "Questionnaire":
            from spark_fhir_schemas.stu3.complex_types.questionnaire import (
                QuestionnaireSchema,
            )

            return QuestionnaireSchema
        elif resource_type == "Questionnaire_Item":
            from spark_fhir_schemas.stu3.complex_types.questionnaire_item import (
                Questionnaire_ItemSchema,
            )

            return Questionnaire_ItemSchema
        elif resource_type == "Questionnaire_EnableWhen":
            from spark_fhir_schemas.stu3.complex_types.questionnaire_enablewhen import (
                Questionnaire_EnableWhenSchema,
            )

            return Questionnaire_EnableWhenSchema
        elif resource_type == "Questionnaire_Option":
            from spark_fhir_schemas.stu3.complex_types.questionnaire_option import (
                Questionnaire_OptionSchema,
            )

            return Questionnaire_OptionSchema
        elif resource_type == "QuestionnaireResponse":
            from spark_fhir_schemas.stu3.complex_types.questionnaireresponse import (
                QuestionnaireResponseSchema,
            )

            return QuestionnaireResponseSchema
        elif resource_type == "QuestionnaireResponse_Item":
            from spark_fhir_schemas.stu3.complex_types.questionnaireresponse_item import (
                QuestionnaireResponse_ItemSchema,
            )

            return QuestionnaireResponse_ItemSchema
        elif resource_type == "QuestionnaireResponse_Answer":
            from spark_fhir_schemas.stu3.complex_types.questionnaireresponse_answer import (
                QuestionnaireResponse_AnswerSchema,
            )

            return QuestionnaireResponse_AnswerSchema
        elif resource_type == "ReferralRequest":
            from spark_fhir_schemas.stu3.complex_types.referralrequest import (
                ReferralRequestSchema,
            )

            return ReferralRequestSchema
        elif resource_type == "ReferralRequest_Requester":
            from spark_fhir_schemas.stu3.complex_types.referralrequest_requester import (
                ReferralRequest_RequesterSchema,
            )

            return ReferralRequest_RequesterSchema
        elif resource_type == "RelatedPerson":
            from spark_fhir_schemas.stu3.complex_types.relatedperson import (
                RelatedPersonSchema,
            )

            return RelatedPersonSchema
        elif resource_type == "RequestGroup":
            from spark_fhir_schemas.stu3.complex_types.requestgroup import (
                RequestGroupSchema,
            )

            return RequestGroupSchema
        elif resource_type == "RequestGroup_Action":
            from spark_fhir_schemas.stu3.complex_types.requestgroup_action import (
                RequestGroup_ActionSchema,
            )

            return RequestGroup_ActionSchema
        elif resource_type == "RequestGroup_Condition":
            from spark_fhir_schemas.stu3.complex_types.requestgroup_condition import (
                RequestGroup_ConditionSchema,
            )

            return RequestGroup_ConditionSchema
        elif resource_type == "RequestGroup_RelatedAction":
            from spark_fhir_schemas.stu3.complex_types.requestgroup_relatedaction import (
                RequestGroup_RelatedActionSchema,
            )

            return RequestGroup_RelatedActionSchema
        elif resource_type == "ResearchStudy":
            from spark_fhir_schemas.stu3.complex_types.researchstudy import (
                ResearchStudySchema,
            )

            return ResearchStudySchema
        elif resource_type == "ResearchStudy_Arm":
            from spark_fhir_schemas.stu3.complex_types.researchstudy_arm import (
                ResearchStudy_ArmSchema,
            )

            return ResearchStudy_ArmSchema
        elif resource_type == "ResearchSubject":
            from spark_fhir_schemas.stu3.complex_types.researchsubject import (
                ResearchSubjectSchema,
            )

            return ResearchSubjectSchema
        elif resource_type == "Resource":
            from spark_fhir_schemas.stu3.complex_types.resource import ResourceSchema

            return ResourceSchema
        elif resource_type == "RiskAssessment":
            from spark_fhir_schemas.stu3.complex_types.riskassessment import (
                RiskAssessmentSchema,
            )

            return RiskAssessmentSchema
        elif resource_type == "RiskAssessment_Prediction":
            from spark_fhir_schemas.stu3.complex_types.riskassessment_prediction import (
                RiskAssessment_PredictionSchema,
            )

            return RiskAssessment_PredictionSchema
        elif resource_type == "Schedule":
            from spark_fhir_schemas.stu3.complex_types.schedule import ScheduleSchema

            return ScheduleSchema
        elif resource_type == "SearchParameter":
            from spark_fhir_schemas.stu3.complex_types.searchparameter import (
                SearchParameterSchema,
            )

            return SearchParameterSchema
        elif resource_type == "SearchParameter_Component":
            from spark_fhir_schemas.stu3.complex_types.searchparameter_component import (
                SearchParameter_ComponentSchema,
            )

            return SearchParameter_ComponentSchema
        elif resource_type == "Sequence":
            from spark_fhir_schemas.stu3.complex_types.sequence import SequenceSchema

            return SequenceSchema
        elif resource_type == "Sequence_ReferenceSeq":
            from spark_fhir_schemas.stu3.complex_types.sequence_referenceseq import (
                Sequence_ReferenceSeqSchema,
            )

            return Sequence_ReferenceSeqSchema
        elif resource_type == "Sequence_Variant":
            from spark_fhir_schemas.stu3.complex_types.sequence_variant import (
                Sequence_VariantSchema,
            )

            return Sequence_VariantSchema
        elif resource_type == "Sequence_Quality":
            from spark_fhir_schemas.stu3.complex_types.sequence_quality import (
                Sequence_QualitySchema,
            )

            return Sequence_QualitySchema
        elif resource_type == "Sequence_Repository":
            from spark_fhir_schemas.stu3.complex_types.sequence_repository import (
                Sequence_RepositorySchema,
            )

            return Sequence_RepositorySchema
        elif resource_type == "ServiceDefinition":
            from spark_fhir_schemas.stu3.complex_types.servicedefinition import (
                ServiceDefinitionSchema,
            )

            return ServiceDefinitionSchema
        elif resource_type == "Slot":
            from spark_fhir_schemas.stu3.complex_types.slot import SlotSchema

            return SlotSchema
        elif resource_type == "Specimen":
            from spark_fhir_schemas.stu3.complex_types.specimen import SpecimenSchema

            return SpecimenSchema
        elif resource_type == "Specimen_Collection":
            from spark_fhir_schemas.stu3.complex_types.specimen_collection import (
                Specimen_CollectionSchema,
            )

            return Specimen_CollectionSchema
        elif resource_type == "Specimen_Processing":
            from spark_fhir_schemas.stu3.complex_types.specimen_processing import (
                Specimen_ProcessingSchema,
            )

            return Specimen_ProcessingSchema
        elif resource_type == "Specimen_Container":
            from spark_fhir_schemas.stu3.complex_types.specimen_container import (
                Specimen_ContainerSchema,
            )

            return Specimen_ContainerSchema
        elif resource_type == "StructureDefinition":
            from spark_fhir_schemas.stu3.complex_types.structuredefinition import (
                StructureDefinitionSchema,
            )

            return StructureDefinitionSchema
        elif resource_type == "StructureDefinition_Mapping":
            from spark_fhir_schemas.stu3.complex_types.structuredefinition_mapping import (
                StructureDefinition_MappingSchema,
            )

            return StructureDefinition_MappingSchema
        elif resource_type == "StructureDefinition_Snapshot":
            from spark_fhir_schemas.stu3.complex_types.structuredefinition_snapshot import (
                StructureDefinition_SnapshotSchema,
            )

            return StructureDefinition_SnapshotSchema
        elif resource_type == "StructureDefinition_Differential":
            from spark_fhir_schemas.stu3.complex_types.structuredefinition_differential import (
                StructureDefinition_DifferentialSchema,
            )

            return StructureDefinition_DifferentialSchema
        elif resource_type == "StructureMap":
            from spark_fhir_schemas.stu3.complex_types.structuremap import (
                StructureMapSchema,
            )

            return StructureMapSchema
        elif resource_type == "StructureMap_Structure":
            from spark_fhir_schemas.stu3.complex_types.structuremap_structure import (
                StructureMap_StructureSchema,
            )

            return StructureMap_StructureSchema
        elif resource_type == "StructureMap_Group":
            from spark_fhir_schemas.stu3.complex_types.structuremap_group import (
                StructureMap_GroupSchema,
            )

            return StructureMap_GroupSchema
        elif resource_type == "StructureMap_Input":
            from spark_fhir_schemas.stu3.complex_types.structuremap_input import (
                StructureMap_InputSchema,
            )

            return StructureMap_InputSchema
        elif resource_type == "StructureMap_Rule":
            from spark_fhir_schemas.stu3.complex_types.structuremap_rule import (
                StructureMap_RuleSchema,
            )

            return StructureMap_RuleSchema
        elif resource_type == "StructureMap_Source":
            from spark_fhir_schemas.stu3.complex_types.structuremap_source import (
                StructureMap_SourceSchema,
            )

            return StructureMap_SourceSchema
        elif resource_type == "StructureMap_Target":
            from spark_fhir_schemas.stu3.complex_types.structuremap_target import (
                StructureMap_TargetSchema,
            )

            return StructureMap_TargetSchema
        elif resource_type == "StructureMap_Parameter":
            from spark_fhir_schemas.stu3.complex_types.structuremap_parameter import (
                StructureMap_ParameterSchema,
            )

            return StructureMap_ParameterSchema
        elif resource_type == "StructureMap_Dependent":
            from spark_fhir_schemas.stu3.complex_types.structuremap_dependent import (
                StructureMap_DependentSchema,
            )

            return StructureMap_DependentSchema
        elif resource_type == "Subscription":
            from spark_fhir_schemas.stu3.complex_types.subscription import (
                SubscriptionSchema,
            )

            return SubscriptionSchema
        elif resource_type == "Subscription_Channel":
            from spark_fhir_schemas.stu3.complex_types.subscription_channel import (
                Subscription_ChannelSchema,
            )

            return Subscription_ChannelSchema
        elif resource_type == "Substance":
            from spark_fhir_schemas.stu3.complex_types.substance import SubstanceSchema

            return SubstanceSchema
        elif resource_type == "Substance_Instance":
            from spark_fhir_schemas.stu3.complex_types.substance_instance import (
                Substance_InstanceSchema,
            )

            return Substance_InstanceSchema
        elif resource_type == "Substance_Ingredient":
            from spark_fhir_schemas.stu3.complex_types.substance_ingredient import (
                Substance_IngredientSchema,
            )

            return Substance_IngredientSchema
        elif resource_type == "SupplyDelivery":
            from spark_fhir_schemas.stu3.complex_types.supplydelivery import (
                SupplyDeliverySchema,
            )

            return SupplyDeliverySchema
        elif resource_type == "SupplyDelivery_SuppliedItem":
            from spark_fhir_schemas.stu3.complex_types.supplydelivery_supplieditem import (
                SupplyDelivery_SuppliedItemSchema,
            )

            return SupplyDelivery_SuppliedItemSchema
        elif resource_type == "SupplyRequest":
            from spark_fhir_schemas.stu3.complex_types.supplyrequest import (
                SupplyRequestSchema,
            )

            return SupplyRequestSchema
        elif resource_type == "SupplyRequest_OrderedItem":
            from spark_fhir_schemas.stu3.complex_types.supplyrequest_ordereditem import (
                SupplyRequest_OrderedItemSchema,
            )

            return SupplyRequest_OrderedItemSchema
        elif resource_type == "SupplyRequest_Requester":
            from spark_fhir_schemas.stu3.complex_types.supplyrequest_requester import (
                SupplyRequest_RequesterSchema,
            )

            return SupplyRequest_RequesterSchema
        elif resource_type == "Task":
            from spark_fhir_schemas.stu3.complex_types.task import TaskSchema

            return TaskSchema
        elif resource_type == "Task_Requester":
            from spark_fhir_schemas.stu3.complex_types.task_requester import (
                Task_RequesterSchema,
            )

            return Task_RequesterSchema
        elif resource_type == "Task_Restriction":
            from spark_fhir_schemas.stu3.complex_types.task_restriction import (
                Task_RestrictionSchema,
            )

            return Task_RestrictionSchema
        elif resource_type == "Task_Input":
            from spark_fhir_schemas.stu3.complex_types.task_input import (
                Task_InputSchema,
            )

            return Task_InputSchema
        elif resource_type == "Task_Output":
            from spark_fhir_schemas.stu3.complex_types.task_output import (
                Task_OutputSchema,
            )

            return Task_OutputSchema
        elif resource_type == "TestReport":
            from spark_fhir_schemas.stu3.complex_types.testreport import (
                TestReportSchema,
            )

            return TestReportSchema
        elif resource_type == "TestReport_Participant":
            from spark_fhir_schemas.stu3.complex_types.testreport_participant import (
                TestReport_ParticipantSchema,
            )

            return TestReport_ParticipantSchema
        elif resource_type == "TestReport_Setup":
            from spark_fhir_schemas.stu3.complex_types.testreport_setup import (
                TestReport_SetupSchema,
            )

            return TestReport_SetupSchema
        elif resource_type == "TestReport_Action":
            from spark_fhir_schemas.stu3.complex_types.testreport_action import (
                TestReport_ActionSchema,
            )

            return TestReport_ActionSchema
        elif resource_type == "TestReport_Operation":
            from spark_fhir_schemas.stu3.complex_types.testreport_operation import (
                TestReport_OperationSchema,
            )

            return TestReport_OperationSchema
        elif resource_type == "TestReport_Assert":
            from spark_fhir_schemas.stu3.complex_types.testreport_assert import (
                TestReport_AssertSchema,
            )

            return TestReport_AssertSchema
        elif resource_type == "TestReport_Test":
            from spark_fhir_schemas.stu3.complex_types.testreport_test import (
                TestReport_TestSchema,
            )

            return TestReport_TestSchema
        elif resource_type == "TestReport_Action1":
            from spark_fhir_schemas.stu3.complex_types.testreport_action1 import (
                TestReport_Action1Schema,
            )

            return TestReport_Action1Schema
        elif resource_type == "TestReport_Teardown":
            from spark_fhir_schemas.stu3.complex_types.testreport_teardown import (
                TestReport_TeardownSchema,
            )

            return TestReport_TeardownSchema
        elif resource_type == "TestReport_Action2":
            from spark_fhir_schemas.stu3.complex_types.testreport_action2 import (
                TestReport_Action2Schema,
            )

            return TestReport_Action2Schema
        elif resource_type == "TestScript":
            from spark_fhir_schemas.stu3.complex_types.testscript import (
                TestScriptSchema,
            )

            return TestScriptSchema
        elif resource_type == "TestScript_Origin":
            from spark_fhir_schemas.stu3.complex_types.testscript_origin import (
                TestScript_OriginSchema,
            )

            return TestScript_OriginSchema
        elif resource_type == "TestScript_Destination":
            from spark_fhir_schemas.stu3.complex_types.testscript_destination import (
                TestScript_DestinationSchema,
            )

            return TestScript_DestinationSchema
        elif resource_type == "TestScript_Metadata":
            from spark_fhir_schemas.stu3.complex_types.testscript_metadata import (
                TestScript_MetadataSchema,
            )

            return TestScript_MetadataSchema
        elif resource_type == "TestScript_Link":
            from spark_fhir_schemas.stu3.complex_types.testscript_link import (
                TestScript_LinkSchema,
            )

            return TestScript_LinkSchema
        elif resource_type == "TestScript_Capability":
            from spark_fhir_schemas.stu3.complex_types.testscript_capability import (
                TestScript_CapabilitySchema,
            )

            return TestScript_CapabilitySchema
        elif resource_type == "TestScript_Fixture":
            from spark_fhir_schemas.stu3.complex_types.testscript_fixture import (
                TestScript_FixtureSchema,
            )

            return TestScript_FixtureSchema
        elif resource_type == "TestScript_Variable":
            from spark_fhir_schemas.stu3.complex_types.testscript_variable import (
                TestScript_VariableSchema,
            )

            return TestScript_VariableSchema
        elif resource_type == "TestScript_Rule":
            from spark_fhir_schemas.stu3.complex_types.testscript_rule import (
                TestScript_RuleSchema,
            )

            return TestScript_RuleSchema
        elif resource_type == "TestScript_Param":
            from spark_fhir_schemas.stu3.complex_types.testscript_param import (
                TestScript_ParamSchema,
            )

            return TestScript_ParamSchema
        elif resource_type == "TestScript_Ruleset":
            from spark_fhir_schemas.stu3.complex_types.testscript_ruleset import (
                TestScript_RulesetSchema,
            )

            return TestScript_RulesetSchema
        elif resource_type == "TestScript_Rule1":
            from spark_fhir_schemas.stu3.complex_types.testscript_rule1 import (
                TestScript_Rule1Schema,
            )

            return TestScript_Rule1Schema
        elif resource_type == "TestScript_Param1":
            from spark_fhir_schemas.stu3.complex_types.testscript_param1 import (
                TestScript_Param1Schema,
            )

            return TestScript_Param1Schema
        elif resource_type == "TestScript_Setup":
            from spark_fhir_schemas.stu3.complex_types.testscript_setup import (
                TestScript_SetupSchema,
            )

            return TestScript_SetupSchema
        elif resource_type == "TestScript_Action":
            from spark_fhir_schemas.stu3.complex_types.testscript_action import (
                TestScript_ActionSchema,
            )

            return TestScript_ActionSchema
        elif resource_type == "TestScript_Operation":
            from spark_fhir_schemas.stu3.complex_types.testscript_operation import (
                TestScript_OperationSchema,
            )

            return TestScript_OperationSchema
        elif resource_type == "TestScript_RequestHeader":
            from spark_fhir_schemas.stu3.complex_types.testscript_requestheader import (
                TestScript_RequestHeaderSchema,
            )

            return TestScript_RequestHeaderSchema
        elif resource_type == "TestScript_Assert":
            from spark_fhir_schemas.stu3.complex_types.testscript_assert import (
                TestScript_AssertSchema,
            )

            return TestScript_AssertSchema
        elif resource_type == "TestScript_Rule2":
            from spark_fhir_schemas.stu3.complex_types.testscript_rule2 import (
                TestScript_Rule2Schema,
            )

            return TestScript_Rule2Schema
        elif resource_type == "TestScript_Param2":
            from spark_fhir_schemas.stu3.complex_types.testscript_param2 import (
                TestScript_Param2Schema,
            )

            return TestScript_Param2Schema
        elif resource_type == "TestScript_Ruleset1":
            from spark_fhir_schemas.stu3.complex_types.testscript_ruleset1 import (
                TestScript_Ruleset1Schema,
            )

            return TestScript_Ruleset1Schema
        elif resource_type == "TestScript_Rule3":
            from spark_fhir_schemas.stu3.complex_types.testscript_rule3 import (
                TestScript_Rule3Schema,
            )

            return TestScript_Rule3Schema
        elif resource_type == "TestScript_Param3":
            from spark_fhir_schemas.stu3.complex_types.testscript_param3 import (
                TestScript_Param3Schema,
            )

            return TestScript_Param3Schema
        elif resource_type == "TestScript_Test":
            from spark_fhir_schemas.stu3.complex_types.testscript_test import (
                TestScript_TestSchema,
            )

            return TestScript_TestSchema
        elif resource_type == "TestScript_Action1":
            from spark_fhir_schemas.stu3.complex_types.testscript_action1 import (
                TestScript_Action1Schema,
            )

            return TestScript_Action1Schema
        elif resource_type == "TestScript_Teardown":
            from spark_fhir_schemas.stu3.complex_types.testscript_teardown import (
                TestScript_TeardownSchema,
            )

            return TestScript_TeardownSchema
        elif resource_type == "TestScript_Action2":
            from spark_fhir_schemas.stu3.complex_types.testscript_action2 import (
                TestScript_Action2Schema,
            )

            return TestScript_Action2Schema
        elif resource_type == "ValueSet":
            from spark_fhir_schemas.stu3.complex_types.valueset import ValueSetSchema

            return ValueSetSchema
        elif resource_type == "ValueSet_Compose":
            from spark_fhir_schemas.stu3.complex_types.valueset_compose import (
                ValueSet_ComposeSchema,
            )

            return ValueSet_ComposeSchema
        elif resource_type == "ValueSet_Include":
            from spark_fhir_schemas.stu3.complex_types.valueset_include import (
                ValueSet_IncludeSchema,
            )

            return ValueSet_IncludeSchema
        elif resource_type == "ValueSet_Concept":
            from spark_fhir_schemas.stu3.complex_types.valueset_concept import (
                ValueSet_ConceptSchema,
            )

            return ValueSet_ConceptSchema
        elif resource_type == "ValueSet_Designation":
            from spark_fhir_schemas.stu3.complex_types.valueset_designation import (
                ValueSet_DesignationSchema,
            )

            return ValueSet_DesignationSchema
        elif resource_type == "ValueSet_Filter":
            from spark_fhir_schemas.stu3.complex_types.valueset_filter import (
                ValueSet_FilterSchema,
            )

            return ValueSet_FilterSchema
        elif resource_type == "ValueSet_Expansion":
            from spark_fhir_schemas.stu3.complex_types.valueset_expansion import (
                ValueSet_ExpansionSchema,
            )

            return ValueSet_ExpansionSchema
        elif resource_type == "ValueSet_Parameter":
            from spark_fhir_schemas.stu3.complex_types.valueset_parameter import (
                ValueSet_ParameterSchema,
            )

            return ValueSet_ParameterSchema
        elif resource_type == "ValueSet_Contains":
            from spark_fhir_schemas.stu3.complex_types.valueset_contains import (
                ValueSet_ContainsSchema,
            )

            return ValueSet_ContainsSchema
        elif resource_type == "VisionPrescription":
            from spark_fhir_schemas.stu3.complex_types.visionprescription import (
                VisionPrescriptionSchema,
            )

            return VisionPrescriptionSchema
        elif resource_type == "VisionPrescription_Dispense":
            from spark_fhir_schemas.stu3.complex_types.visionprescription_dispense import (
                VisionPrescription_DispenseSchema,
            )

            return VisionPrescription_DispenseSchema
        else:
            raise Exception(f"Resource Type {resource_type} is unknown")
