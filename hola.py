import json

nombre = input("¿Cuál es tu nombre? ")

print(f"\n¡Hola, {nombre}!")
print(f"Dicen que las personas llamadas {nombre} son increíblemente inteligentes...")
print("...¡y claramente tienen muy buen gusto para programar en Python!")

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

lenguaje = datos["lenguaje_favorito"]
nivel = datos["nivel"]

consejos = {
    "Principiante": (
        f"Veo que estás aprendiendo {lenguaje} como principiante. ¡Excelente elección!\n"
        "Consejo: Practica escribiendo pequeños programas cada día. No necesitas entender\n"
        "todo a la vez — aprende una cosa, pruébala, y luego sigue adelante."
    ),
    "Intermedio": (
        f"Ya tienes experiencia en {lenguaje}. ¡Vas muy bien!\n"
        "Consejo: Empieza a leer código de otros y contribuye a proyectos pequeños."
    ),
    "Avanzado": (
        f"Eres todo un experto en {lenguaje}.\n"
        "Consejo: Comparte tu conocimiento enseñando a otros o escribiendo documentación."
    ),
}

consejo = consejos.get(nivel, f"Sigue practicando {lenguaje}, ¡cada día cuentas!")

print(f"\n--- Consejo para ti ({nivel}) ---")
print(consejo)
