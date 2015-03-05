#!/usr/bin/python

import webapp
import calculadora
import sys


class calculadoraREST(webapp.webApp):

    def operacion(self, parsedRequest, n, sig):
            operando1 = float(parsedRequest[1])
            operando2 = float(parsedRequest[2])
            try:
                if n == 0:
                    op = calculadora.suma(operando1, operando2)
                if n == 1:
                    op = calculadora.resta(operando1, operando2)
                if n == 2:
                    op = calculadora.multiplicacion(operando1, operando2)
                if n == 3:
                    try:
                        op = op = calculadora.division(operando1, operando2)
                    except ZeroDivisionError:
                        return ("200 OK", "<html><body><h1>Division por cero" +
                                "</html></body></h1>")

                return ("200 OK", "<html><body><h1>" +
                        "La operacion" + "</h1><p>" + parsedRequest[1] + sig +
                        parsedRequest[2] + " = " + str(op) + "</body></html>")
            except ValueError:
                return ("200 OK", "<html><body><h1>Operandos incorrectos<" +
                        "/html></body></h1>")
            except IndexError:
                return ("200 OK", "<html><body><h1>Uso:" +
                        "/suma/op1/op2</html></body></h1>")

    def process(self, parserequest):
        (verb, rec, cuerpo) = parserequest
        if verb == "GET":
            if rec[0] == "suma":
                return(self.operacion(rec, 0, "+"))
            elif rec[0] == "resta":
                return(self.operacion(rec, 1, "-"))
            elif rec[0] == "multiplicacion":
                return(self.operacion(rec, 2, "*"))
            elif rec[0] == "division":
                return(self.operacion(rec, 3, "/"))
            else:
                return("Operacion no soportada")

        elif verb == "PUT":
                paquete = (cuerpo[1], cuerpo[0], cuerpo[2])
                if paquete[0] == "+":
                    return(self.operacion(paquete, 0, "+"))
                elif paquete[0] == "-":
                    return(self.operacion(paquete, 1, "-"))
                elif paquete[0] == "*":
                    return(self.operacion(paquete, 2, "-"))
                elif paquete[0] == "/":
                    return(self.operacion(paquete, 3, "-"))
                else:
                    return("Operacion no soportada")


if __name__ == "__main__":
    try:
        caluladora = calculadoraREST("localhost", 1234)
    except KeyboardInterrupt:
        sys.exit()
