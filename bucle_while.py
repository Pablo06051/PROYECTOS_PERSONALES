"""
HAZ UN PROGRAMA QUE PIDA NOTAS DE 
CLASE Y NO PARE HASTA QUE INTRODUZCASUNA 
NOTA NEGATIVA.
LUEGO IMPRIME LA SUMA 
"""
nota = 0

suma = 0

while nota >= 0:
    nota = int(input("Introduce una nota: "))
    if nota >= 0: 
        suma += nota
         
         
print("su nota es:", suma)

  