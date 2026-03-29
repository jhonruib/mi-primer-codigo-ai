# mi-primer-codigo-ai

Repositorio de práctica del curso de Anthropic, donde exploro el desarrollo de software asistido por inteligencia artificial usando **Claude Code CLI**.

---

## Descripción

Este proyecto contiene mis primeros scripts en Python, desarrollados paso a paso con la ayuda de Claude Code. El objetivo es aprender a programar mientras me familiarizo con las herramientas de IA de Anthropic.

---

## Archivos

### `hola.py`
Script interactivo que:
1. Pide tu nombre y te saluda con un mensaje divertido.
2. Lee el archivo `datos.json` para obtener tu lenguaje favorito y tu nivel de programación.
3. Muestra un consejo personalizado según tu nivel (Principiante, Intermedio o Avanzado).

**Cómo ejecutarlo:**
```bash
python3 hola.py
```

### `datos.json`
Archivo de configuración personal que almacena:
- `lenguaje_favorito`: el lenguaje de programación preferido.
- `nivel`: el nivel actual del estudiante.

```json
{
  "lenguaje_favorito": "Python",
  "nivel": "Principiante"
}
```

Puedes editar este archivo para personalizar los mensajes de `hola.py`.

---

## Tecnologías usadas

- **Python 3**
- **JSON**
- **Git / GitHub**
- **[Claude Code CLI](https://claude.ai/code)** — toda la escritura, modificación y gestión del código fue realizada mediante conversaciones con Claude Code en la terminal.

---

## Sobre este proyecto

Este repositorio es parte de mi aprendizaje en el curso de Anthropic. Cada archivo fue creado y refinado usando la CLI de Claude Code, lo que me permitió aprender programación y buenas prácticas de desarrollo al mismo tiempo.

> Desarrollado por **Jhon Alexander Ruiz Buitrago**
