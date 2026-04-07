# 🐾 Veterinary Chatbot API

API backend para un chatbot de clínica veterinaria enfocado en la **gestión de esterilización y logística clínica**.

---

## 🚀 Deploy

API en producción:

👉 https://clinica-veterinaria-crmn.vercel.app/api

Health check:

👉 https://clinica-veterinaria-crmn.vercel.app/api/health

---

## 🧠 Dominio del Problema

Este sistema implementa un chatbot especializado en la **gestión de citas de esterilización veterinaria**.

### 🎯 Objetivo

> Automatizar la atención al cliente para reducir tiempos de gestión y errores en la comunicación.

### 🧩 Funcionalidades principales

El chatbot está diseñado para:

- Informar sobre esterilización  
- Gestionar citas  
- Explicar requisitos preoperatorios  
- Resolver dudas logísticas  
- Mantener contexto conversacional (multi-turno)  

---

## ⚠️ Alcance y Limitaciones

El sistema NO está diseñado para:

- ❌ Emergencias veterinarias  
- ❌ Diagnósticos médicos  
- ❌ Tratamientos clínicos  

👉 En estos casos, el chatbot redirige al usuario a atención veterinaria directa.

---

## 📋 Reglas de Negocio

El sistema implementa reglas explícitas del dominio veterinario:

### 🧪 Analítica preoperatoria
- Obligatoria en animales mayores de 6 años  
- Recomendada en animales jóvenes  

### 🔥 Restricción por celo
- No se puede esterilizar una perra en celo  
- Espera recomendada: 2 meses tras finalizar el celo  

### 🍽️ Ayuno
- Comida: 8–12 horas antes  
- Agua: hasta 1–2 horas antes  

### 🐾 Requisitos
- Vacunación al día  
- Desparasitación  
- Microchip obligatorio  
- Vacuna de rabia obligatoria  

### 📦 Logística

#### Gatos
- Transportín rígido obligatorio  
- Un gato por transportín  

#### Perros
- Correa obligatoria  
- Bozal si es necesario  

### ⏰ Horarios
- Perros: recogida ~12:00  
- Gatos: recogida ~15:00  

### 🚫 Cancelaciones
- Aviso mínimo de 24 horas  

---

## 🤖 Arquitectura del Sistema

Flujo del sistema:

Usuario → API → Memoria → RAG → OpenAI → Respuesta

### Componentes

- Backend en Python (Serverless)  
- API REST desplegada en Vercel  
- Integración con OpenAI (LLM)  
- Lógica basada en reglas del dominio  
- Memoria conversacional (`session_id`)  
- RAG (Retrieval-Augmented Generation)  

---

## 🧠 Memoria Conversacional

El sistema mantiene contexto mediante `session_id`.

### Ejemplo real

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=tengo%20un%20gato&session_id=2  
👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20si%20tuviera%207%20años&session_id=2  

✔ Conversación multi-turno  
✔ Mantiene coherencia entre preguntas  

---

## 📚 Retrieval-Augmented Generation (RAG)

El sistema incorpora **RAG** para mejorar la precisión en respuestas críticas.

### 📌 Cuándo se activa

Cuando el usuario pregunta sobre:

- Ayuno  
- Agua  
- Instrucciones preoperatorias  

### ⚙️ Funcionamiento

1. Se detecta intención del usuario  
2. Se recupera contexto relevante  
3. Se añade al prompt del modelo  
4. El modelo responde usando ese contexto  

### 🔗 Fuente utilizada

👉 https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation

### 🎯 Beneficios

- Evita alucinaciones del modelo  
- Garantiza coherencia clínica  
- Usa información real  

### 🧪 Ejemplo real

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20puede%20beber%20agua&session_id=3  

Respuesta:

```json
{
  "session_id": "3",
  "msg": "y puede beber agua",
  "respuesta": "...",
  "rag_used": true,
  "rag_source": "https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation"
}
```

---

## 📡 Endpoints

### 🔹 Chat endpoint

GET /api?msg=texto&session_id=id

Ejemplo:

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola  

---

### 🔹 Health Check

GET /api/health

Respuesta:

```json
{
  "status": "ok",
  "service": "veterinary-chatbot-api"
}
```

---

## 🧪 Ejemplos de uso

### Conversación básica

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=hola  
👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=quiero%20esterilizar%20a%20mi%20gato  

---

### Conversación con memoria

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=tengo%20un%20gato&session_id=2  
👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=y%20si%20tuviera%207%20años&session_id=2  

---

### RAG activado

👉 https://clinica-veterinaria-crmn.vercel.app/api?msg=puede%20beber%20agua%20antes%20de%20la%20cirugia&session_id=3  

---

## 📊 Trazabilidad con requisitos del curso

### ✔ VET-7 — Backend API
- API REST implementada  
- Endpoints funcionales  
- Despliegue en Vercel  

### ✔ VET-9 — LLM Integration
- Integración con OpenAI  
- Respuestas dinámicas  
- Uso de contexto del dominio  

### ✔ Conversaciones (1–7)

El chatbot responde correctamente a:

- Saludos  
- Solicitudes de esterilización  
- Preguntas sobre horarios  
- Validación de restricciones  
- Rechazo de casos fuera de alcance  
- Redirección en emergencias  

---

## 🧾 Documentación adicional

El proyecto incluye:

- Intents del chatbot  
- Conversaciones de validación  
- Casos de uso  
- Backlog en Jira  

---

## 📦 Información del Proyecto

Repositorio:  
👉 https://github.com/crmn2105/clinica-veterinaria  

API desplegada:  
👉 https://clinica-veterinaria-crmn.vercel.app/api  

---

## 🏁 Conclusión

Este proyecto implementa un sistema completo de chatbot basado en:

- Arquitectura API  
- Integración con LLM  
- Reglas de negocio explícitas  
- Memoria conversacional  
- RAG para control de precisión  

👉 Siguiendo metodología **Spec First (SDD)**  
👉 Cumpliendo los requisitos del curso  

---

## 💥 Resultado final

Sistema listo para producción con:

- Alta coherencia  
- Control del dominio  
- Reducción de errores del modelo  
- Experiencia conversacional realista  