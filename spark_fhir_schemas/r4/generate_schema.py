import json
import os
from pathlib import Path
import shutil
from typing import Dict, Optional, List

from attr import dataclass


@dataclass
class PropertyInfo:
    Name: str
    Type: Optional[str]
    UnderlyingDataType: Optional[str]

    def __str__(self) -> str:
        return f"property_name:{self.Name}, type={self.Type}, underlying_type={self.UnderlyingDataType}"


def main() -> bool:
    resources = ['Account', 'ActivityDefinition', 'AdverseEvent', 'AllergyIntolerance', 'Appointment',
                 'AppointmentResponse', 'AuditEvent', 'Basic', 'Binary', 'BiologicallyDerivedProduct', 'BodyStructure',
                 'Bundle', 'CapabilityStatement', 'CarePlan', 'CareTeam', 'CatalogEntry', 'ChargeItem',
                 'ChargeItemDefinition', 'Claim', 'ClaimResponse', 'ClinicalImpression', 'CodeSystem', 'Communication',
                 'CommunicationRequest', 'CompartmentDefinition', 'Composition', 'ConceptMap', 'Condition', 'Consent',
                 'Contract', 'Coverage', 'CoverageEligibilityRequest', 'CoverageEligibilityResponse', 'DetectedIssue',
                 'Device', 'DeviceDefinition', 'DeviceMetric', 'DeviceRequest', 'DeviceUseStatement',
                 'DiagnosticReport', 'DocumentManifest', 'DocumentReference', 'EffectEvidenceSynthesis', 'Encounter',
                 'Endpoint', 'EnrollmentRequest', 'EnrollmentResponse', 'EpisodeOfCare', 'EventDefinition',
                 'ExampleScenario', 'ExplanationOfBenefit', 'FamilyMemberHistory', 'Flag', 'Goal',
                 'GraphDefinition', 'Group', 'GuidanceResponse', 'HealthcareService', 'ImagingStudy', 'Immunization',
                 'ImmunizationEvaluation', 'ImmunizationRecommendation', 'ImplementationGuide', 'InsurancePlan',
                 'Invoice', 'Library', 'Linkage', 'List', 'Location', 'Measure', 'MeasureReport', 'Media', 'Medication',
                 'MedicationAdministration', 'MedicationDispense', 'MedicationKnowledge', 'MedicationRequest',
                 'MedicationStatement', 'MedicinalProduct', 'MedicinalProductAuthorization',
                 'MedicinalProductContraindication', 'MedicinalProductIndication',
                 'MedicinalProductPackaged',
                 'MedicinalProductPharmaceutical', 'MessageDefinition',
                 'MessageHeader', 'MolecularSequence', 'NamingSystem', 'NutritionOrder', 'Observation',
                 'OperationDefinition', 'Organization',
                 'OrganizationAffiliation', 'Patient', 'PaymentNotice', 'PaymentReconciliation', 'Person',
                 'PlanDefinition', 'Practitioner', 'PractitionerRole', 'Procedure', 'Provenance', 'Questionnaire',
                 'QuestionnaireResponse', 'RelatedPerson', 'RequestGroup', 'ResearchDefinition',
                 'ResearchElementDefinition', 'ResearchStudy', 'ResearchSubject', 'RiskAssessment',
                 'RiskEvidenceSynthesis', 'Schedule', 'SearchParameter', 'ServiceRequest', 'Slot', 'Specimen',
                 'SpecimenDefinition', 'StructureDefinition', 'StructureMap', 'Subscription', 'Substance',
                 'SubstanceSpecification', 'SupplyDelivery', 'SupplyRequest', 'Task',
                 'TerminologyCapabilities', 'TestReport', 'TestScript', 'ValueSet', 'VerificationResult',
                 'VisionPrescription']

    data_dir: Path = Path(__file__).parent.joinpath('./')

    with open(data_dir.joinpath("fhir.schema.json"), "r+") as file:
        contents = file.read()

    fhir_schema = json.loads(contents)
    definitions = fhir_schema["definitions"]
    # print(definitions)
    # print(type(definitions))
    # for key, value in definitions.items():
    #     print(f"{key}:{value}")
    # print(definitions["Patient"])
    resource_name: str = "Patient"
    resource = definitions[resource_name]
    properties = resource["properties"]
    properties_info: List[PropertyInfo] = []
    print("---- Properties ----")
    for key, value in {k: v for k, v in properties.items() if not k.startswith("_")}.items():
        property_name = key
        description: str = value["description"]
        items: Optional[Dict[str, str]] = value["items"] if "items" in value else None
        type_: Optional[str] = value["type"] if "type" in value else None
        ref_: Optional[str] = (
            value["$ref"] if "$ref" in value and type_ != "array"
            else value["items"]["$ref"] if "items" in value
            else None
        )
        print(f"{key}:{value}")
        # type_ == None means string
        ref_clean: Optional[str] = ref_[ref_.rfind("/") + 1:] if ref_ else None
        # print(f"property_name:{property_name}, type={type_}, ref={ref_}, ref_clean={ref_clean}")
        properties_info.append(
            PropertyInfo(
                Name=property_name,
                Type=type_,
                UnderlyingDataType=ref_clean
            )
        )
        print(properties_info[-1])
        print("")

    with open(data_dir.joinpath("template.jinja2"), "r+") as file:
        template_contents: str = file.read()
        from jinja2 import Template
        template = Template(template_contents)
        result: str = template.render(resource=resource_name, properties=properties_info)

        with open(data_dir.joinpath("resources").joinpath(f"{resource_name}.py"), "w+") as file2:
            file2.write(result)
        print(result)
    return True


if __name__ == "__main__":
    exit(main())
