# 🐾 Veterinary Chatbot API

API backend para un chatbot de clínica veterinaria enfocado en la gestión de esterilización y logística clínica.

---

## 🚀 Deploy

API en producción:

https://clinica-veterinaria-crmn.vercel.app/api

---

## 🧠 Dominio del Problema

Este sistema implementa un chatbot especializado en la **gestión de citas de esterilización veterinaria**.

Su objetivo es:

> Automatizar la atención al cliente para reducir tiempos de gestión y errores en la comunicación.

El chatbot está diseñado específicamente para:
- Informar sobre esterilización
- Gestionar citas
- Explicar requisitos preoperatorios
- Resolver dudas logísticas

---

## ⚠️ Alcance y limitaciones

El sistema NO está diseñado para:

- ❌ Emergencias veterinarias
- ❌ Diagnósticos médicos
- ❌ Tratamientos clínicos

En estos casos, el chatbot redirige al usuario a atención veterinaria directa.

---

## 📋 Reglas de Negocio

El chatbot se rige por reglas explícitas del dominio veterinario:

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
- Perros: 12:00 aprox.
- Gatos: 15:00 aprox.

### 🚫 Cancelaciones
- Aviso mínimo de 24 horas

---

## 🤖 Arquitectura del Sistema

El sistema sigue una arquitectura sencilla basada en API:

Usuario → API (FastAPI en Vercel) → OpenAI → Respuesta

Componentes:

- Backend en Python
- API REST desplegada en Vercel
- Integración con OpenAI
- Lógica basada en reglas del dominio

---

## 📡 Endpoints

### 🔹 Health Check

GET /api/health

Ejemplo:
