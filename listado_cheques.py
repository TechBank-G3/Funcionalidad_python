
import csv
import datetime
from collections import defaultdict

with open("cheques.csv","w", newline="") as file:
    writer=csv.writer(file)
    writer.writerow(("NroCheque","CodigoBanco","CodigoScurusal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Estado"))

numeros_cheques = set()

def obtener_numero_cheque():
    while True:
        try:
            Nro=int(input("Ingrese el numero de cheque: "))
            if Nro not in numeros_cheques:
                numeros_cheques.add(Nro)
                break
            else:
                print("El número ya fue ingresado. Intente con otro número.")
        except ValueError:
                print("Por favor, ingrese un número válido.")
    return Nro

def obtener_codigo_banco():
    while True:
        try:
            codigo_sucursal=int(input("Ingrese el codigo del banco: "))
            if 1<=codigo_sucursal<=100:
                return codigo_sucursal
            else:
                print("Valor incorrecto, ingrese un numero entre 1 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def obtener_codigo_sucursal():
    while True:
        try:
            codigo_sucursal=int(input("Ingrese el codigo de la sucursal: "))
            if 1<=codigo_sucursal<=300:
                return codigo_sucursal
            else:
                print("Valor incorrecto, ingrese un numero entre 1 y 300.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def obtener_nro_cuenta_origen():
    while True:
        try:
            return int(input("Ingrese el numero de cuenta de origen: "))
        except ValueError:
            print("Por favor, ingrese un numero de cuenta valido")

def obtener_nro_cuenta_destino():
    while True:
        try:
            return int(input("Ingrese el numero de cuenta de destino: "))
        except ValueError:
            print("Por favor, ingrese un numero de cuenta valido")

def obtener_valor():
    while True:
        try:
            return float(input("Ingrese el valor del cheque: "))
        except ValueError:
            print("Por favor, ingrese un valor para el cheque valido")

def obtener_fecha_origen():
    while True:
        fecha_str = input("Por favor, ingrese la fecha de origen en el formato AAAA-MM-DD: ")
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")

def obtener_fecha_destino():
    while True:
        fecha_str = input("Por favor, ingrese la fecha de pago en el formato AAAA-MM-DD: ")
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")

def obtener_estado():
    while True:
        try:
            estado=(input("Ingrese el estado del cheque (pendiente,aprobado,rechazado): ")).lower()
            if estado=="pendiente" or estado=="aprobado" or estado=="rechazado": 
                return estado
            else:
                print("El estado es incorrecto, ingrese el estado (pendiente,aprobado,rechazado): ")
        except ValueError:
            print("Por favor, ingrese un estado valido (pendiente,aprobado,rechazado): ")

cheques=[]

def agregar_cheque():
    
    NroCheque=obtener_numero_cheque()
    CodigoBanco=obtener_codigo_banco()
    CodigoSucursal=obtener_codigo_sucursal()
    NumeroCuentaOrigen=obtener_nro_cuenta_origen()
    NumeroCuentaDestino=obtener_nro_cuenta_destino()
    Valor=obtener_valor()
    FechaOrigen=obtener_fecha_origen()
    FechaPago=obtener_fecha_destino()
    Dni=input("Ingrese el DNI sin puntos: ")
    Estado=obtener_estado()

    with open("cheques.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow((NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,Dni,Estado))

    cheque= {
        "NroCheque":NroCheque,
        "CodigoBanco":CodigoBanco,
        "CodigoSucursal":CodigoSucursal,
        "NumeroCuentaOrigen":NumeroCuentaOrigen,
        "NumeroCuentaDestino":NumeroCuentaDestino,
        "Valor":Valor,
        "FechaOrigen":FechaOrigen,
        "FechaPago":FechaPago,
        "DNI":Dni,
        "Estado":Estado
    }

    cheques.append(cheque)


agregar_cheque()
agregar_cheque()


def consultar_cheques_emitidos_dni():

    Dni=input("Ingrese el DNI sin puntos: ")

    with open("cheques.csv","r") as cheques:
        reader=csv.reader(cheques)
        encabezado = next(reader)
        
        dni_encontrado = False

        for cheque in reader:
                if Dni == cheque[8]:
                    print(encabezado)
                    print(cheque)
                    dni_encontrado = True
        if not dni_encontrado:
                    print("La persona con ese dni no tiene ningun cheque.")         

consultar_cheques_emitidos_dni()




def consultar_cheques_emitidos_dni_estado():
    Dni = input("Ingrese el DNI sin puntos: ")
    Estado = obtener_estado()
    persona_con_cheque = False

    with open("cheques.csv", "r") as cheques:
        reader = csv.reader(cheques)
        encabezado = next(reader)

        for cheque in reader:
            if Dni == cheque[8] and Estado == cheque[9].lower():
                print(encabezado)
                print(cheque)
                persona_con_cheque = True

        if not persona_con_cheque:
            print(f"La persona con el DNI {Dni} no tiene ningún cheque en el estado de {Estado}.")

consultar_cheques_emitidos_dni_estado()

def consultar_cheques_por_fecha_pago():
    FechaPago_inicio = obtener_fecha_origen() 
    FechaPago_fin = obtener_fecha_destino()    

    with open("cheques.csv", "r") as cheques:
        reader = csv.reader(cheques)
        encabezado = next(reader)  
        for cheque in reader:
            fecha_pago_cheque = datetime.datetime.strptime(cheque[7], "%Y-%m-%d").date()

            if FechaPago_inicio <= fecha_pago_cheque <= FechaPago_fin:
                print(encabezado)
                print(cheque)
    
consultar_cheques_por_fecha_pago()


input("Presiona Enter para salir...")
