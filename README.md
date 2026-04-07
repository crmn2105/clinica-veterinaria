# 🐾 Veterinary Chatbot API

API backend para un chatbot de clínica veterinaria enfocado en la **gestión de esterilización y logística clínica**.

---

## 🚀 Deploy

API en producción:

https://clinica-veterinaria-crmn.vercel.app/api

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

El sistema sigue una arquitectura basada en API:

Usuario → API (Python en Vercel) → OpenAI → Respuesta

### Componentes:

- Backend en Python (Serverless)
- API REST desplegada en Vercel
- Integración con OpenAI (LLM)
- Lógica basada en reglas del dominio
- Memoria conversacional (session_id)
- RAG (Retrieval-Augmented Generation)

---

## 🧠 Memoria Conversacional

El sistema mantiene contexto mediante `session_id`.

Ejemplo:

/api?msg=tengo un gato&session_id=1  
/api?msg=y si tuviera 7 años?&session_id=1  

✔ Permite conversaciones multi-turno  
✔ Mantiene coherencia entre preguntas  

---

## 🧠 Retrieval-Augmented Generation (RAG)

El sistema incorpora un mecanismo de **RAG** para mejorar la precisión en respuestas críticas.

### 📌 Cuándo se activa

Cuando el usuario pregunta sobre:

- Ayuno
- Agua
- Instrucciones preoperatorias

### ⚙️ Cómo funciona

1. Se detecta intención del usuario  
2. Se recupera contexto relevante  
3. Se inyecta en el prompt del modelo  
4. El modelo responde usando SOLO ese contexto  

### 🔗 Fuente utilizada

https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation

### 🎯 Beneficios

- Evita alucinaciones del modelo  
- Garantiza coherencia clínica  
- Alinea respuestas con documentación oficial  

### 🧪 Ejemplo

/api?msg=y puede beber agua&session_id=3  

Respuesta incluye:

{
  "rag_used": true,
  "rag_source": "https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation"
}

---

## 📡 Endpoints

### 🔹 Chat endpoint

GET /api?msg=texto&session_id=id

Ejemplo:

/api?msg=hola

---

### 🔹 Health Check

GET /api/health

Respuesta:

{
  "status": "ok",
  "service": "veterinary-chatbot-api"
}

---

## 🧪 Ejemplos de uso

### Conversación básica

/api?msg=hola  
/api?msg=quiero esterilizar a mi gato  

### Conversación con contexto

/api?msg=tengo un gato&session_id=2  
/api?msg=y si tuviera 7 años?&session_id=2  

### RAG activado

/api?msg=puede beber agua antes de la cirugía&session_id=3  

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
https://github.com/crmn2105/clinica-veterinaria  

API desplegada:  
https://clinica-veterinaria-crmn.vercel.app/api  

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
- Control de dominio  
- Reducción de errores del modelo  
- Experiencia conversacional realista  

---

## 🧠 Nivel del proyecto

Este proyecto supera un chatbot básico al incluir:

- ✔ Memoria (stateful)  
- ✔ Control de reglas  
- ✔ RAG con fuente externa  
- ✔ Arquitectura desplegada  

👉 Nivel: **Avanzado (cercano a producción real)**