#!usr/bin/python
import sys


def suma(operando1, operando2):
    return operando1 + operando2


def resta(termino1, termino2):
    return termino1 - termino2


def multiplicacion(producto1, producto2):
    return producto1*producto2


def division(dividendo, divisor):
    return dividendo/divisor

if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print "Uso: operacion numero1 numero2"
        sys.exit()
    argumentos = sys.argv
    try:
        oper1 = float(argumentos[2])
        oper2 = float(argumentos[3])
        if(argumentos[1] == 'suma'):
            print suma(oper1, oper2)
        elif(argumentos[1] == 'resta'):
            print resta(oper1, oper2)
        elif(argumentos[1] == 'multiplicacion'):
            print multiplicacion(oper1, oper2)
        elif(argumentos[1] == 'division'):
            print division(oper1, oper2)
        else:
            print "Operacion incorrecta"
    except ValueError:
        print "Termino no valido"
    except ZeroDivisionError:
        print "Division por cero"
