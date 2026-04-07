# Intents Veterinary Chatbot Catalog

## 1. Salutation

**Description:** General greeting and scope explanation.
**Example:** “Hi, what can you help me with?”

## 2. BookSterilisation

**Description:** User wants to book a sterilisation/castration appointment.
**Example:** “I want to book a spay for my dog.”

## 3. QueryDropOffWindow

**Description:** User asks about drop-off time on surgery day.
**Example:** “What time should I bring my cat?”

## 4. QueryPickUpTime

**Description:** User asks about pick-up time after surgery.
**Example:** “When can I pick up my dog?”

## 5. QueryPreOpInstructions

**Description:** User asks about fasting or preparation before surgery.
**Example:** “How long should my dog fast before the operation?”

## 6. QueryMedicalRequirements

**Description:** User asks about blood test, vaccination, deworming, or required pre-op checks.
**Example:** “Is a blood test required before sterilisation?”

## 7. QueryEligibility

**Description:** User asks whether the pet can undergo surgery under certain conditions.
**Example:** “Can my 8-year-old dog be sterilised?”

## 8. RequestEmergencyCare

**Description:** User describes an emergency situation.
**Example:** “My dog was hit by a car and is bleeding.”

## 9. OutOfScopeGeneralConsult

**Description:** User asks for diagnosis, prescription, or routine illness advice.
**Example:** “My cat has a cough for three days—can you prescribe something?”

## 10. HumanHandoff

**Description:** User wants to speak with a human staff member.
**Example:** “I’d rather speak to a person about my invoice.”

## 11. CheckAvailability

**Description:** User asks which days have capacity for surgery.
**Example:** “What days do you have capacity next week?”

## 12. ConfirmBookingDate

**Description:** User chooses one of the proposed dates.
**Example:** “Thursday works for me.”

## 13. RejectHeatCondition

**Description:** Booking must be rejected because a female dog is in heat.
**Example:** “She is currently in heat.”

## 14. AskSpeciesDetails

**Description:** Bot requests species information to continue booking.
**Example:** “Is it a cat or a dog?”

## 15. AskSexDetails

**Description:** Bot requests sex of the pet.
**Example:** “Is your pet male or female?”

## 16. AskWeightDetails

**Description:** Bot requests weight to estimate dog surgery duration.
**Example:** “How much does your dog weigh?”

## 17. ExplainClinicScope

**Description:** Bot clarifies it only handles sterilisation-related logistics and information.
**Example:** “I can help with sterilisation booking and pre-op instructions.”

## 18. ExplainSchedulingRules

**Description:** Bot explains scheduling rules such as weekdays, minute quota, or dog limits.
**Example:** “We schedule surgeries Monday to Thursday.”

## 19. ExplainPostOpLogistics

**Description:** Bot explains recovery, collection, or after-surgery logistics.
**Example:** “Your cat can usually be collected around 15:00.”

## 20. EscalateSpecialCase

**Description:** Bot detects a case that should be reviewed by staff.
**Example:** “Please contact the clinic directly so a staff member can review this case.”

---

# Mapping: Conversations to Intents

* Conversation 1 → Salutation, ExplainClinicScope, OutOfScopeGeneralConsult
* Conversation 2 → QueryDropOffWindow
* Conversation 3 → QueryMedicalRequirements, QueryEligibility
* Conversation 4 → RequestEmergencyCare
* Conversation 5 → BookSterilisation, RejectHeatCondition
* Conversation 6 → QueryPickUpTime
* Conversation 7 → HumanHandoff
* Conversation 8 → CheckAvailability
* Conversation 9 → CheckAvailability, ExplainSchedulingRules
* Conversation 10 → QueryPreOpInstructions
