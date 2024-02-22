nota1Flt = float(input('ingrese la nota ->')) 
nota2Flt = float(input('ingrese la nota ->'))
nota3Flt = float (input('ingrese la nota ->'))
nota4Flt = float (input('ingrese la nota ->'))

definitivaFlt = (nota1Flt * 0.20 ) +(nota2Flt * 0.30) + (nota3Flt * 0.40 )+ (nota4Flt * 0.10) 
if definitivaFlt >= 3.5:
    print('Has aprobado')
else:
    print('No has aprobado')
print('Su nota definitiva es:  ',definitivaFlt)