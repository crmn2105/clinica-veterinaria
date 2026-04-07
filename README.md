# 🐾 Veterinary Chatbot API

API backend para un chatbot de clínica veterinaria enfocado en gestión de esterilización y logística clínica.

## 🚀 Deploy

API en producción:

https://clinica-veterinaria-crmn.vercel.app/api

## 📡 Endpoints

### 🔹 Health check
### 🔹 Health check

GET:
https://clinica-veterinaria-crmn.vercel.app/api/health

Respuesta:
{
  "status": "ok",
  "service": "veterinary-chatbot-api"
}

---

### 🔹 Chat endpoint

GET:
https://clinica-veterinaria-crmn.vercel.app/api?msg=mensaje

Ejemplo:
https://clinica-veterinaria-crmn.vercel.app/api?msg=quiero%20esterilizar%20a%20mi%20gato

Respuesta:
{
  "msg": "quiero esterilizar a mi gato",
  "respuesta": "Para esterilizar a tu gato..."
}