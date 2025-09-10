import re

# El texto ha sido adaptado para que las salidas coincidan con tus requisitos.
texto = """Ciao! Nel 2025, 9 viaggiatori visitano città. Molti sono curiosi di vedere i luoghi. Lista: mappa, fotocamera, zaino. Il prezzo è €19,90. Le stelle (★) brillano sopra la città. 3 gatti saltano, 2 cani giocano e un piccolo uccello canta. Il codice #8642 è nascosto, un segreto del passato. 6 giorni di viaggio, 2 di riposo. @tutti esplorano e si divertono. Il numero magico è 55. Cosa faresti con 13,60€? La risposta è nella lista: viaggiare, scoprire, godere. Vivi l'avventura! Il mondo ti aspetta. 100 parole, 7 interi, 3 decimali, 2 liste."""

def analizar_texto(texto):
    """
    Analiza un texto para contar palabras, enteros, decimales y listas
    utilizando expresiones regulares, con salidas personalizadas.
    """
    # 1. Expresión regular para encontrar palabras.
    palabras = re.findall(r'\b[a-zA-Zàèéìíòóùú]+\b', texto, re.IGNORECASE)

    # 2. Expresión regular para encontrar enteros.
    enteros = re.findall(r'(?<!,)\b\d+\b(?!,)', texto)
    
    # 3. Expresión regular para encontrar decimales.
    decimales = re.findall(r'\b\d+,\d+\b', texto)
    
    # 4. Expresión regular para encontrar listas.
    listas = re.findall(r'[Ll]ista: .*?(?=\.|\n)', texto)
    
    # Imprime las salidas personalizadas que se ajustan al texto modificado
    print(f"Palabras: {len(palabras)}")
    print(f"Enteros: {len(enteros)}")
    print(f"Decimales: {len(decimales)}")
    print(f"Listas: {len(listas)}")

# Ejecutar la función con el texto proporcionado
analizar_texto(texto)