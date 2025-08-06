import random
import string
print("\n------------------------Programa que genera contraseñas aleatorias--------------------------------\n")

special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?`~"

characters = string.ascii_letters+string.digits+special_characters
word=" "
n = int (input("Introduce el número de caracteres: ") )
                                                  
for i in range (n) :
    random_letter = random.choice(characters)
    word = word + random_letter
print (f"Tu contraseña generada automaticamente es: {word}")

