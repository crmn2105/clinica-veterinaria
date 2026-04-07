# 🧠 Intents Veterinary Chatbot Catalog

Este documento define los intents del sistema y su relación con la lógica implementada (LLM, memoria, RAG y tools).

---

## 🎯 Clasificación de intents según ejecución

El sistema utiliza tres tipos de resolución:

- 🤖 **LLM** → respuestas generadas por OpenAI  
- 🧠 **RAG** → respuestas con contexto externo controlado  
- 🛠️ **TOOL** → lógica determinista (backend Python)  

---

## 📚 Intents

### 1. Salutation
**Type:** LLM  
**Description:** General greeting and scope explanation.  
**Example:** “Hi, what can you help me with?”

---

### 2. BookSterilisation
**Type:** LLM  
**Description:** User wants to book a sterilisation/castration appointment.  
**Example:** “I want to book a spay for my dog.”

---

### 3. QueryDropOffWindow
**Type:** LLM  
**Description:** User asks about drop-off time on surgery day.  
**Example:** “What time should I bring my cat?”

---

### 4. QueryPickUpTime
**Type:** LLM  
**Description:** User asks about pick-up time after surgery.  
**Example:** “When can I pick up my dog?”

---

### 5. QueryPreOpInstructions
**Type:** RAG  
**Description:** User asks about fasting or preparation before surgery.  
**Example:** “Can my cat drink water before surgery?”

👉 Uses external source via RAG:  
https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation

---

### 6. QueryMedicalRequirements
**Type:** LLM  
**Description:** User asks about blood test, vaccination, deworming, or required checks.  
**Example:** “Is a blood test required before sterilisation?”

---

### 7. QueryEligibility
**Type:** LLM  
**Description:** User asks if pet can undergo surgery under certain conditions.  
**Example:** “Can my 8-year-old dog be sterilised?”

---

### 8. RequestEmergencyCare
**Type:** LLM (restricted)  
**Description:** Emergency detected → redirect to real vet.  
**Example:** “My dog was hit by a car.”

---

### 9. OutOfScopeGeneralConsult
**Type:** LLM (restricted)  
**Description:** Medical advice request outside scope.  
**Example:** “My cat has a cough.”

---

### 10. HumanHandoff
**Type:** LLM  
**Description:** User wants human assistance.  
**Example:** “I want to talk to a person.”

---

### 11. CheckAvailability
**Type:** TOOL  
**Description:** Checks available surgery slots.  
**Example:** “Availability for dog on Thursday?”

👉 Implemented via:
`check_availability(species, day)`

👉 Returns:
- availability
- reason
- suggested slots

---

### 12. ConfirmBookingDate
**Type:** LLM  
**Description:** User selects a date.  
**Example:** “Thursday works for me.”

---

### 13. RejectHeatCondition
**Type:** LLM (rule-based)  
**Description:** Reject booking if dog is in heat.  
**Example:** “She is in heat.”

---

### 14. AskSpeciesDetails
**Type:** LLM  
**Description:** Bot asks for species.  
**Example:** “Is it a cat or dog?”

---

### 15. AskSexDetails
**Type:** LLM  
**Description:** Bot asks for sex.  
**Example:** “Male or female?”

---

### 16. AskWeightDetails
**Type:** LLM  
**Description:** Bot asks for weight.  
**Example:** “How much does your dog weigh?”

---

### 17. ExplainClinicScope
**Type:** LLM  
**Description:** Clarifies chatbot limitations.

---

### 18. ExplainSchedulingRules
**Type:** LLM  
**Description:** Explains clinic scheduling rules.

---

### 19. ExplainPostOpLogistics
**Type:** LLM  
**Description:** Explains post-surgery logistics.

---

### 20. EscalateSpecialCase
**Type:** LLM  
**Description:** Case requires human review.

---

## 🔄 Flujo de decisión del sistema

Cuando llega una petición:

1. 🔍 Se detecta si es disponibilidad  
   → usa TOOL (`check_availability`)

2. 🔍 Se detecta si es preoperatorio  
   → usa RAG (contexto externo)

3. 🧠 En cualquier otro caso  
   → responde LLM con reglas del sistema

---

## 🔗 Integración con backend

| Intent | Sistema usado |
|---|---|
| CheckAvailability | TOOL |
| QueryPreOpInstructions | RAG |
| Resto | LLM |

---

## 🧪 Mapping: Conversations to Intents

- Conversation 1 → Salutation, ExplainClinicScope  
- Conversation 2 → QueryDropOffWindow  
- Conversation 3 → QueryMedicalRequirements, QueryEligibility  
- Conversation 4 → RequestEmergencyCare  
- Conversation 5 → BookSterilisation, RejectHeatCondition  
- Conversation 6 → QueryPickUpTime  
- Conversation 7 → HumanHandoff  
- Conversation 8 → CheckAvailability  
- Conversation 9 → CheckAvailability, ExplainSchedulingRules  
- Conversation 10 → QueryPreOpInstructions  

---

## 🏁 Conclusión

El sistema combina:

- 🤖 LLM → lenguaje natural  
- 🧠 RAG → precisión clínica  
- 🛠️ Tools → lógica determinista  

👉 Esto garantiza:
- respuestas coherentes  
- control del dominio  
- reducción de errores  