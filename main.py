
#  texto[start: end: step ]    es como un slice, se usa en los areglos y como una cadena es un arreglo de 
# caracteres funciona también. start (donde se empieza el recorte), end (donde termina), step( cada cuanto
#  devuelve un caracter), si step es -1 ser reccore de forma inversa

fraseOriginal = """
    Tu trabajo va a llenar gran parte de tu vida, la única manera de estar realmente satisfecho 
    es hacer lo que creas que es un gran trabajo y la única manera de hacerlo es amar lo que haces. 
    Si no lo has encontrado aún, sigue buscando. 
    Como con todo lo que tiene que ver con el corazón, lo sabrás cuando lo hayas encontrado
"""


frase = fraseOriginal.lower()

letras = []
cantidad = []

print(fraseOriginal)
fraseOriginal = fraseOriginal.strip()

letras.append( input("Ingrese la letra 1: ").lower() )
letras.append( input("Ingrese la letra 2: ").lower() )
letras.append( input("Ingrese la letra 3: ").lower() )

# Cuantas veces aparece cada letra
cantidad.append( frase.count( letras[0]) )
cantidad.append( frase.count( letras[1]) )
cantidad.append( frase.count( letras[2]) )
print(f"Letras: ({letras[0]}:{cantidad[0]}), ({letras[1]}:{cantidad[1]}), ({letras[2]}:{cantidad[2]})")

#Cuantas palabras hay en total

palabras = frase.split()
cantidadPalabras = len(palabras)
print(f"Palabras: {cantidadPalabras}")

#Primera y ultima letra
print(f"Primera letra: {fraseOriginal[0]}, Ultima letra: {fraseOriginal[-1]}")

#Palabras en orden inverso
palabras.reverse()
print(f"Orden Inverso: \n{' '.join(palabras)}")

#Aparece python
mensaje = {
    "True": "Si aparece!!",
    "False": "No aparece"
}
res = 'python' in frase
res = f"{res}"
print(f"Aparece Python: {mensaje[res]}") # Es como el includes en otros lenguajes
