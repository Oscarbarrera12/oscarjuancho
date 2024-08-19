## Comentarios en Python
""" Podemos agregar un comentario demas usando los 
atajos de teclado """

# Tipos de variables

# print = Imprime una variable o cadena que contenga 

#1: Texto, Cadena, Alfanumerico (Strings)
variableTexto = "Hola bienvenidos a Python";
print(variableTexto);

variableTexto2 = "Aqui hay un texto para concatenar";
print(variableTexto, variableTexto2);

print(variableTexto.upper());
print(variableTexto2.find("t"));

variableTexto3 = "AQUI HAY UN TEXTO MÁS"

print(variableTexto3.lower());

variableTexto4 = "Texto reemplazo"

print(variableTexto4.replace("Text","Palabra"));

# 2: Numérica (Int, Float, BigInt, etc) BigInt = 0 - 999999, Int = 0 - 9, Float = 0 - Infinito

variableNumEntero = 10;
variableNumDecimal = 7.5;
variableNumMillon = 1000000;

print(variableNumEntero, variableNumDecimal);

# 3: Bcolean(Verdadero Falso) True = Verdadero , False = Falso 

variableV = True;
variableF = False;  

print(variableV, "O" ,variableF);

# 4: 