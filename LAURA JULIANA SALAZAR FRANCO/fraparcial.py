import re
texto = """Bonjour! En 2025, 8 voyageurs découvrent le monde. La vie est une aventure, un long voyage. Liste: carte, appareil, sac. Le prix est de 22,40€. Les étoiles (★) brillent la nuit. 4 chats jouent, 3 chiens dorment. Le code #2468 est caché, un mystère. 7 jours de voyage, 1 jour de repos. @tous explorent et profitent. Le numéro magique est 99. Que feriez-vous avec 18,75€? La réponse est dans la liste: voyager, découvrir, profiter. Vivez l'aventure! Un voyage, une expérience, une découverte. 100 mots, 7 entiers, 3 décimaux, 2 listes."""

def analizar_texto(texto):
    """
    Analiza un texto para contar palabras, enteros, decimales y listas.
    """
    # se agregan los acentos franceses.
    palabras = re.findall(r'\b[a-zA-Záàâäéèêëíìîïóòôöúùûüçñ]+\b', texto, re.IGNORECASE)

    # encontrar enteros.
    enteros = re.findall(r'(?<!,)\b\d+\b(?!,)', texto)
    
    # se cambia el . por la ,
    decimales = re.findall(r'\b\d+,\d+\b', texto)
    
    listas = re.findall(r'[Ll]iste: .*?(?=\.|\n)', texto)

    print(f"Palabras: {len(palabras)}")
    print(f"Enteros: {len(enteros)}")
    print(f"Decimales: {len(decimales)}")
    print(f"Listas: {len(listas)}")

analizar_texto(texto)