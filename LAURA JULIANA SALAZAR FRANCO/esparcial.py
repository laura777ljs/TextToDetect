import re

# Texto a analizar
texto = """En el año 2025, el 10, 11 y 12 de marzo, 100 viajeros de 25, 30, 45, 50 y 60 años
exploran 5 ciudades. ¡Hola! ¿Te gusta viajar? El cielo azul, las estrellas (★) brillan.
6 niños juegan, 5.50 horas de paseo. Lista: mapa, cámara, mochila.
El costo es $25.30. ¿Sabías que el código #3698 es secreto?
La vida es aventura, @todos participan. El tiempo pasa, 7 días de viaje. ¡Diversión!
El número especial es 77. ¿Qué harías con 15.25 euros?
La respuesta está en la lista: explorar, descubrir, disfrutar.
¡Vive la experiencia! Aquí hay un 1, un 2 y un 3. Un 10 y un 20.
En total hay 91 palabras, 10 enteros, 3 decimales, 2 listas."""

def analizar_texto(texto):
    """
    Analiza un texto para contar palabras, enteros, decimales y listas,
    utilizando expresiones regulares.
    """
    palabras = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', textGNORECASE)
o, re.I
    # Enteros: Secuencias de dígitos que NO tienen un punto antes o después
    enteros = re.findall(r'(?<!\.)\b\d+\b(?!\.)', texto)
    
    # Decimales: Números que contienen un punto.
    decimales = re.findall(r'\b\d+\.\d+\b', texto)
    
    # Listas: Buscamos el patrón "Lista:" o "lista:" seguido del contenido.
    listas = re.findall(r'[Ll]ista: .*?(?=\.|\n)', texto)
    
    print(f"Palabras: {len(palabras)}")
    print(f"Enteros: {len(enteros)}")
    print(f"Decimales: {len(decimales)}")
    print(f"Listas: {len(listas)}")

analizar_texto(texto)