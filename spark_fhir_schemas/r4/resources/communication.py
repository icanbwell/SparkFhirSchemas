from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Communication:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An occurrence of information being transmitted; e.g. an alert that was sent to
        a responsible provider, a public health agency that was notified about a
        reportable condition.


        resourceType: This is a Communication resource

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

        identifier: Business identifiers assigned to this communication by the performer or other
            systems which remain constant as the resource is updated and propagates from
            server to server.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this Communication.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this Communication.

        basedOn: An order, proposal or plan fulfilled in whole or in part by this
            Communication.

        partOf: Part of this action.

        inResponseTo: Prior communication that this communication is in response to.

        status: The status of the transmission.

        statusReason: Captures the reason for the current state of the Communication.

        category: The type of message conveyed such as alert, notification, reminder,
            instruction, etc.

        priority: Characterizes how quickly the planned or in progress communication must be
            addressed. Includes concepts such as stat, urgent, routine.

        medium: A channel that was used for this communication (e.g. email, fax).

        subject: The patient or group that was the focus of this communication.

        topic: Description of the purpose/content, similar to a subject line in an email.

        about: Other resources that pertain to this communication and to which this
            communication should be associated.

        encounter: The Encounter during which this Communication was created or to which the
            creation of this record is tightly associated.

        sent: The time when this communication was sent.

        received: The time when this communication arrived at the destination.

        recipient: The entity (e.g. person, organization, clinical information system, care team
            or device) which was the target of the communication. If receipts need to be
            tracked by an individual, a separate resource instance will need to be created
            for each recipient.  Multiple recipient communications are intended where
            either receipts are not tracked (e.g. a mass mail-out) or a receipt is
            captured in aggregate (all emails confirmed received by a particular time).

        sender: The entity (e.g. person, organization, clinical information system, or device)
            which was the source of the communication.

        reasonCode: The reason or justification for the communication.

        reasonReference: Indicates another resource whose existence justifies this communication.

        payload: Text, attachment(s), or resource(s) that was communicated to the recipient.

        note: Additional notes or commentary about the communication by the sender, receiver
            or other interested parties.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.communication_payload import Communication_Payload
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Communication resource
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
                # Business identifiers assigned to this communication by the performer or other
                # systems which remain constant as the resource is updated and propagates from
                # server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this Communication.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this Communication.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # An order, proposal or plan fulfilled in whole or in part by this
                # Communication.
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Part of this action.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Prior communication that this communication is in response to.
                StructField(
                    "inResponseTo",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The status of the transmission.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Captures the reason for the current state of the Communication.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The type of message conveyed such as alert, notification, reminder,
                # instruction, etc.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Characterizes how quickly the planned or in progress communication must be
                # addressed. Includes concepts such as stat, urgent, routine.
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # A channel that was used for this communication (e.g. email, fax).
                StructField(
                    "medium",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The patient or group that was the focus of this communication.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # Description of the purpose/content, similar to a subject line in an email.
                StructField(
                    "topic", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Other resources that pertain to this communication and to which this
                # communication should be associated.
                StructField(
                    "about",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The Encounter during which this Communication was created or to which the
                # creation of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The time when this communication was sent.
                StructField(
                    "sent", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The time when this communication arrived at the destination.
                StructField(
                    "received", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The entity (e.g. person, organization, clinical information system, care team
                # or device) which was the target of the communication. If receipts need to be
                # tracked by an individual, a separate resource instance will need to be created
                # for each recipient.  Multiple recipient communications are intended where
                # either receipts are not tracked (e.g. a mass mail-out) or a receipt is
                # captured in aggregate (all emails confirmed received by a particular time).
                StructField(
                    "recipient",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The entity (e.g. person, organization, clinical information system, or device)
                # which was the source of the communication.
                StructField(
                    "sender", Reference.get_schema(recursion_depth + 1), True
                ),
                # The reason or justification for the communication.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates another resource whose existence justifies this communication.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Text, attachment(s), or resource(s) that was communicated to the recipient.
                StructField(
                    "payload",
                    ArrayType(
                        Communication_Payload.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Additional notes or commentary about the communication by the sender, receiver
                # or other interested parties.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
