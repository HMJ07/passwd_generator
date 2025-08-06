import random
import string
print("\n------------------------Programa que genera contraseñas aleatorias--------------------------------\n")
characters = string.ascii_letters+"1234567890"
word=" "
n = int (input("Introduce el número de caracteres: ") )
                                                  
for i in range (n) :
    random_letter = random. choice (characters)
    word = word + random_letter
print (f"Tu contraseña generada automaticamente es: {word}")
