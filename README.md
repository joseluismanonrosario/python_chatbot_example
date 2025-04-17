# 🤖 Chatbot Python

Un chatbot básico en Python utilizando `ChatterBot` y `NLTK`. Proyecto creado para aprender a construir un asistente conversacional desde cero, utilizando herramientas de código abierto, Git y GitHub.

---

## 🚀 Tecnologías Utilizadas

- [Python 3.x](https://www.python.org/)
- [ChatterBot](https://github.com/gunthercox/ChatterBot)
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/)
- Entorno virtual (`venv`)
- Git y GitHub para control de versiones

---

## 🛠️ Instalación y Configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/chatbot-python.git
cd chatbot-python
```

### 2. Crea y activa un entorno virtual

```bash
python -m venv env
```

- En **Windows**:
  ```bash
  .\env\Scripts\activate
  ```
- En **Mac/Linux**:
  ```bash
  source env/bin/activate
  ```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

---

## 🤖 Entrenamiento del Chatbot

El chatbot se entrena automáticamente usando el corpus de conversación en inglés:

```python
trainer.train("chatterbot.corpus.english")
```

También puedes personalizar el entrenamiento usando tus propios datos si lo deseas.

---

## 💬 Cómo usarlo

Ejecuta el archivo principal desde la terminal:

```bash
python chatbot.py
```

Chatea con tu bot en la consola. Para salir, escribe:

```
exit
```

---

## 📁 Estructura del Proyecto

```
chatbot-python/
│
├── env/                    # Entorno virtual (ignorado en Git)
├── chatbot.py              # Archivo principal del bot
├── requirements.txt        # Dependencias del proyecto
├── .gitignore              # Archivos ignorados por Git
└── README.md               # Este archivo
```

---

## 🔄 Flujo de Trabajo con Git

Este proyecto sigue un flujo de trabajo sencillo basado en ramas:

- `main`: Rama principal de producción.
- `develop`: Rama de desarrollo (opcional si se implementa GitFlow).
- Para nuevas funciones o pruebas, se recomienda crear ramas como:
  ```bash
  git checkout -b feature/nombre-de-la-funcion
  ```

### Recomendaciones:

- Hacer commits descriptivos.
- Usar `pull requests` para fusionar ramas.
- Proteger la rama `main` desde GitHub.

---

## 📌 Características Pendientes / Ideas

- [ ] Soporte para idioma español
- [ ] Interfaz gráfica con Tkinter o Web
- [ ] Conexión con GPT-3 o GPT-4 vía API
- [ ] Chatbot web con Flask + GitHub Pages
- [ ] Integración con bases de datos para respuestas personalizadas

---

## 🧪 En desarrollo

Este proyecto es parte de una serie de prácticas para aprender:

- Flujo de trabajo con Git y GitHub
- Chatbots con inteligencia artificial
- Automatización de despliegue
- Integración de interfaces web

---

## 🤝 Contribuciones

¿Quieres colaborar? ¡Genial!

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b feature/mi-funcion`
3. Realiza tus cambios y haz commit: `git commit -m "Agrega nueva función"`
4. Sube tus cambios: `git push origin feature/mi-funcion`
5. Abre un Pull Request 🚀

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

MIT © 2025 [Jose Luis Mañón](https://github.com/joseluismanonrosario)
