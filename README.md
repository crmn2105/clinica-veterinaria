# 🐾 Veterinary Chatbot API

API backend para un chatbot de clínica veterinaria enfocado en la **gestión de esterilización y logística clínica**.

---

## 👨‍💻 Equipo

Proyecto desarrollado por:

- 👤 Ángel Carmona Gómez  
- 🎓 Proyecto académico — Chatbot Veterinario  

---

## 🔗 Enlaces del Proyecto

- 🌐 API en producción:  
👉 https://clinica-veterinaria-crmn.vercel.app/api  

- ❤️ Health Check:  
👉 https://clinica-veterinaria-crmn.vercel.app/api/health  

- 📦 Repositorio GitHub:  
👉 https://github.com/crmn2105/clinica-veterinaria  

- 📊 Jira (gestión del proyecto):  
👉 https://crmn2105.atlassian.net/jira/software/projects/VET/boards/2  

---

## 🚀 Cómo probar el sistema (IMPORTANTE)

El sistema está desplegado en Vercel, no requiere instalación.

### 🔹 Test básico

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola  

---

### 🔹 Test memoria (multi-turno)

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=tengo%20un%20gato&session_id=2  
👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20si%20tuviera%207%20años&session_id=2  

✔ Mantiene contexto  
✔ Aplica reglas de negocio  

---

### 🔹 Test RAG

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=puede%20beber%20agua&session_id=3  

✔ `rag_used = true`  
✔ Usa fuente externa  

---

### 🔹 Test Tool (availability)

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=availability%20for%20dog%20on%20thursday&session_id=99  

✔ Usa tool  
✔ No inventa respuestas  
✔ Aplica lógica real  

---

## 🧠 Dominio del Problema

Sistema especializado en la **gestión de citas de esterilización veterinaria**.

### 🎯 Objetivo

> Automatizar la atención al cliente reduciendo errores y tiempos de gestión.

---

## 🧩 Funcionalidades principales

- Gestión de citas  
- Información sobre esterilización  
- Requisitos preoperatorios  
- Resolución de dudas logísticas  
- Memoria conversacional (multi-turno)  
- RAG (contexto externo)  
- Tool de disponibilidad  

---

## ⚠️ Alcance y Limitaciones

El sistema NO realiza:

- ❌ Diagnósticos  
- ❌ Tratamientos  
- ❌ Emergencias  

👉 En estos casos redirige a atención veterinaria real.

---

## 📋 Reglas de Negocio

### 🧪 Analítica preoperatoria
- Obligatoria > 6 años  
- Recomendada en jóvenes  

### 🔥 Restricción por celo
- No esterilizar perras en celo  
- Espera de 2 meses  

### 🍽️ Ayuno
- Comida: 8–12h  
- Agua: hasta 1–2h antes  

### 🐾 Requisitos
- Vacunas  
- Desparasitación  
- Microchip  
- Rabia obligatoria  

### 📦 Logística
- Gatos → transportín  
- Perros → correa / bozal  

### ⏰ Horarios
- Perros → 12:00  
- Gatos → 15:00  

---

## 🤖 Arquitectura del Sistema


Usuario → API → Memoria → RAG → Tool → OpenAI → Respuesta


### Componentes

- Backend en Python (Serverless)  
- API REST desplegada en Vercel  
- Integración con OpenAI  
- Memoria (`session_id`)  
- RAG  
- Tool de disponibilidad  

---

## 🧠 Memoria Conversacional

El sistema mantiene contexto mediante `session_id`.

✔ Conversaciones coherentes  
✔ Persistencia de contexto  

---

## 📚 RAG (Retrieval-Augmented Generation)

El sistema utiliza información externa para mejorar precisión.

### 🔗 Fuente

👉 https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation  

### ✔ Beneficios

- Evita alucinaciones  
- Garantiza coherencia clínica  

---

## 🛠️ Availability Tool

### 🎯 Función

- Controlar disponibilidad real  
- Evitar respuestas inventadas  

### ✔ Resultado

- `tool_used`  
- `tool_result`  
- Respuesta natural  

---

## 📡 Endpoints

### 🔹 Chat endpoint

GET /api?msg=texto&session_id=id  

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola  

---

### 🔹 Health Check

GET /api/health  

```json
{
  "status": "ok",
  "service": "veterinary-chatbot-api"
}
🧪 Ejemplos de uso
Conversación básica

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola

Memoria

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=tengo%20un%20gato&session_id=2

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20si%20tuviera%207%20años&session_id=2

RAG

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=puede%20beber%20agua&session_id=3

Tool

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=availability%20for%20dog%20on%20thursday&session_id=99

⚙️ Configuración (.env)
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
📊 Jira / Backlog

Proyecto gestionado con metodología SCRUM:

EPIC 1 → Setup
EPIC 2 → SDD
EPIC 3 → Chatbot

Incluye:

API
Memoria
RAG
Tool
Reglas de negocio
🏁 Conclusión

Sistema completo que combina:

LLM
Memoria
RAG
Tool

✔ Preparado para evaluación directa desde navegador
✔ Sin instalación necesaria

💥 Resultado final
Alta coherencia
Control del dominio
Reducción de errores
Arquitectura robusta
Experiencia conversacional realista

---

# 🎯 Ahora haz esto (último paso)

1. Pega esto en `README.md`
2. Guarda (Cmd + S)
3. En terminal:

```bash
git add README.md
git commit -m "final README ready for evaluation"
git push origin HEAD:main
🧠 Resultado real

👉 Ahora el profesor puede:

probar todo sin preguntarte nada
entender el sistema en 1 minuto
ver arquitectura + Jira + tests

➡️ esto es exactamente lo que sube de 9 a 10

Si quieres, ya solo queda una cosa final:

👉 te preparo cómo defenderlo en 30 segundos delante del profesor (muy top)

no quiero que me pases un unico bloque de codigo no en varios que si no no puedo pegarlo en codigo

Perfecto, ahora sí — te lo dejo en UN SOLO BLOQUE CONTINUO, sin cortes ni partes separadas, para que lo puedas copiar y pegar directamente en README.md en Cursor 👇

# 🐾 Veterinary Chatbot API

API backend para un chatbot de clínica veterinaria enfocado en la **gestión de esterilización y logística clínica**.

---

## 👨‍💻 Equipo

Proyecto desarrollado por:

- 👤 Ángel Carmona Gómez  
- 🎓 Proyecto académico — Chatbot Veterinario  

---

## 🔗 Enlaces del Proyecto

- 🌐 API en producción:  
👉 https://clinica-veterinaria-crmn.vercel.app/api  

- ❤️ Health Check:  
👉 https://clinica-veterinaria-crmn.vercel.app/api/health  

- 📦 Repositorio GitHub:  
👉 https://github.com/crmn2105/clinica-veterinaria  

- 📊 Jira (gestión del proyecto):  
👉 https://crmn2105.atlassian.net/jira/software/projects/VET/boards/2  

---

## 🚀 Cómo probar el sistema (IMPORTANTE)

El sistema está desplegado en Vercel, no requiere instalación.

### 🔹 Test básico

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola  

---

### 🔹 Test memoria (multi-turno)

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=tengo%20un%20gato&session_id=2  
👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20si%20tuviera%207%20años&session_id=2  

✔ Mantiene contexto  
✔ Aplica reglas de negocio  

---

### 🔹 Test RAG

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=puede%20beber%20agua&session_id=3  

✔ `rag_used = true`  
✔ Usa fuente externa  

---

### 🔹 Test Tool (availability)

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=availability%20for%20dog%20on%20thursday&session_id=99  

✔ Usa tool  
✔ No inventa respuestas  
✔ Aplica lógica real  

---

## 🧠 Dominio del Problema

Sistema especializado en la **gestión de citas de esterilización veterinaria**.

### 🎯 Objetivo

> Automatizar la atención al cliente reduciendo errores y tiempos de gestión.

---

## 🧩 Funcionalidades principales

- Gestión de citas  
- Información sobre esterilización  
- Requisitos preoperatorios  
- Resolución de dudas logísticas  
- Memoria conversacional (multi-turno)  
- RAG (contexto externo)  
- Tool de disponibilidad  

---

## ⚠️ Alcance y Limitaciones

El sistema NO realiza:

- ❌ Diagnósticos  
- ❌ Tratamientos  
- ❌ Emergencias  

👉 En estos casos redirige a atención veterinaria real.

---

## 📋 Reglas de Negocio

### 🧪 Analítica preoperatoria
- Obligatoria > 6 años  
- Recomendada en jóvenes  

### 🔥 Restricción por celo
- No esterilizar perras en celo  
- Espera de 2 meses  

### 🍽️ Ayuno
- Comida: 8–12h  
- Agua: hasta 1–2h antes  

### 🐾 Requisitos
- Vacunas  
- Desparasitación  
- Microchip  
- Rabia obligatoria  

### 📦 Logística
- Gatos → transportín  
- Perros → correa / bozal  

### ⏰ Horarios
- Perros → 12:00  
- Gatos → 15:00  

---

## 🤖 Arquitectura del Sistema

Usuario → API → Memoria → RAG → Tool → OpenAI → Respuesta

### Componentes

- Backend en Python (Serverless)  
- API REST desplegada en Vercel  
- Integración con OpenAI  
- Memoria (`session_id`)  
- RAG  
- Tool de disponibilidad  

---

## 🧠 Memoria Conversacional

El sistema mantiene contexto mediante `session_id`.

✔ Conversaciones coherentes  
✔ Persistencia de contexto  

---

## 📚 RAG (Retrieval-Augmented Generation)

El sistema utiliza información externa para mejorar precisión.

### 🔗 Fuente

👉 https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation  

### ✔ Beneficios

- Evita alucinaciones  
- Garantiza coherencia clínica  

---

## 🛠️ Availability Tool

### 🎯 Función

- Controlar disponibilidad real  
- Evitar respuestas inventadas  

### ✔ Resultado

- `tool_used`  
- `tool_result`  
- Respuesta natural  

---

## 📡 Endpoints

### 🔹 Chat endpoint

GET /api?msg=texto&session_id=id  

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola  

---

### 🔹 Health Check

GET /api/health  

```json
{
  "status": "ok",
  "service": "veterinary-chatbot-api"
}
🧪 Ejemplos de uso
Conversación básica

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola

Memoria

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=tengo%20un%20gato&session_id=2

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20si%20tuviera%207%20años&session_id=2

RAG

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=puede%20beber%20agua&session_id=3

Tool

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=availability%20for%20dog%20on%20thursday&session_id=99

⚙️ Configuración (.env)
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
📊 Jira / Backlog

Proyecto gestionado con metodología SCRUM:

EPIC 1 → Setup
EPIC 2 → SDD
EPIC 3 → Chatbot

Incluye:

API
Memoria
RAG
Tool
Reglas de negocio
🏁 Conclusión

Sistema completo que combina:

LLM
Memoria
RAG
Tool

✔ Preparado para evaluación directa desde navegador
✔ Sin instalación necesaria

💥 Resultado final
Alta coherencia
Control del dominio
Reducción de errores
Arquitectura robusta
Experiencia conversacional realista