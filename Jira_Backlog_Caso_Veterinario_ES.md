# Jira Backlog – Caso Veterinario

## EPIC 1 – SET UP

### VET-1 – Crear repositorio y configuración inicial

* Crear repositorio en GitHub
* Configurar entorno local
* Añadir .gitignore y .env.example

### VET-2 – README inicial

* Explicar cómo ejecutar el proyecto
* Describir funcionalidades básicas

### VET-3 – Despliegue en Vercel

* Conectar repositorio a Vercel
* Configurar variables de entorno
* Obtener URL pública

---

## EPIC 2 – SDD (Diseño y especificación)

### VET-4 – Configuración del flujo de trabajo

* Crear tablero Jira
* Definir estructura de tickets

### VET-5 – Definición de intents

* Crear catálogo de intents
* Mapear intents con conversaciones

### VET-6 – Implementación del flujo

* Definir reglas del negocio
* Integrar lógica en el chatbot

---

## EPIC 3 – CHATBOT

### VET-7 – Backend FastAPI

* Crear endpoints (/ y /ask_bot)
* Configurar API

### VET-8 – Interfaz básica

* Uso de Swagger para pruebas
* Preparación para UI futura

### VET-9 – Integración LLM

* Conectar con OpenAI
* Implementar system prompt

### VET-10 – Memoria de sesión

* Uso de session_id
* Mantener contexto de conversación

### VET-11 – RAG (opcional)

* Conectar fuente externa
* Recuperar información relevante

### VET-12 – Tool de disponibilidad

* Simular agenda
* Aplicar reglas (240 min, 2 perros)

### VET-13 – Calendario real (opcional)

* Integrar calendario externo

### VET-14 – Documentación del dominio

* Reglas veterinarias
* Casos de uso

