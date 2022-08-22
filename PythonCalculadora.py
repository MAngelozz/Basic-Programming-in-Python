from ast import Add
from ipaddress import summarize_address_range
from msilib.schema import _Validation_records
from pdb import Restart
from shutil import SameFileError
from tkinter import N


number1=int(input("Ingrese un numero: "))
number2=int(input("Ingrese otro numero: "))

elección = 0

while elección != 6:
    print('''
    Indique operación a realizar:

    1) Suma
    2)Resta
    3)Multiplicacion
    4)Division
    5)Cambio de valores
    6) Salir 
    ''')

    elección = int(input())

    if elección == 1:
        print(" ")
        print("Resultado: ", number1, "+", number2, "=", number1+number2)

    if elección == 2:
        print("")
        print("Resultado: ", number1, "-", number2, "=", number1-number2)

    if elección == 3:
        print("")
        print("Resultado: ", number1, "*", number2, "=", number1*number2)
    if elección == 4:
        print("")
        print("Resultado: ", number1, "/", number2, "=", number1/number2)

    if elección == 5:
        number1=int(input("Ingrese un numero: "))
        number2=int(input("Ingrese otro numero: "))

    if elección == 6:
        print("Gracias por usar la calculadora")
