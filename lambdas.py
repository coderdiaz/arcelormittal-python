# Lambda
#
# lambda arguments : body

sumar = lambda val1, val2 : val1 + val2
operacion = lambda val1, val2, funcion : funcion(val1, val2)

resultado = operacion(10, 20, sumar)
print(resultado)
