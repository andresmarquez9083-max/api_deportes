API Deportiva – Documentación del Contrato
 Descripción general

¿Qué hace la API?

La API Deportiva es un servicio REST desarrollado en Python con FastAPI que permite consultar información de ligas deportivas de fútbol.
La API actúa como una capa intermedia que consume datos desde una API pública externa (TheSportsDB) y los expone de forma estructurada y simplificada.

¿Qué información devuelve?

La API retorna información relevante de ligas deportivas, incluyendo:

Identificador de la liga
Nombre de la liga
Tipo de deporte
País al que pertenece la liga


¿Para qué sirve?
Esta API puede ser utilizada en:

-Proyectos académicos
-Aplicaciones deportivas
-Sistemas de consulta de estadísticas

Ejemplos prácticos de consumo de APIs externas

Prácticas de arquitectura cliente–servidor y APIs REST

🔗 Puntos finales disponibles
🔹 Obtener ligas de fútbol
📍 URL del punto final
GET /api/deportes/ligas

📌 Método HTTP
GET

📌 Parámetros requeridos

Este endpoint no requiere parámetros.

📤 Ejemplo de petición
GET http://127.0.0.1:8000/api/deportes/ligas

📥 Respuestas
✅ Respuesta exitosa (200 OK)
{
  "leagues": [
    {
      "idLeague": "4328",
      "strLeague": "English Premier League",
      "strSport": "Soccer",
      "strCountry": "England"
    }
  ]
}

📌 Descripción de los campos

idLeague: Identificador único de la liga deportiva

strLeague: Nombre de la liga

strSport: Tipo de deporte (fútbol)

strCountry: País al que pertenece la liga

⚠️ Manejo de errores
❌ Error 500 – Error interno del servidor

Ejemplo de respuesta

{
  "detail": "Error al consumir la API deportiva"
}


Explicación
Este error se presenta cuando ocurre un problema al comunicarse con la API externa o cuando falla el procesamiento de la información recibida.

autor: andres marquez
