
#ejercicio 12
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

numero_ocurrencias = frase.lower().count(vocal.lower())
print(f"La vocal '{vocal}' aparece {numero_ocurrencias} veces en la frase.")

