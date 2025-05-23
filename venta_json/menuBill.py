from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from JsonFile import JsonFile
from company  import Company
from customer import RegularClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(green_color + "*"*90 + reset_color)
        gotoxy(30, 2); print(blue_color + "Registro de Cliente" + reset_color)
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        valor = input("Ingrese Valor: ")
        try:
            valor = float(valor)
        except ValueError:
            print("Valor debe ser numérico.")
            return
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        if any(cli["dni"] == dni for cli in clients):
            print("Cliente ya existe.")
        else:
            clients.append({"dni": dni, "nombre": nombre, "apellido": apellido, "valor": valor})
            json_file.save(clients)
            print("Cliente guardado correctamente.")
        input("Presione una tecla para continuar...")

    def update(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(blue_color + "Actualizar Cliente" + reset_color)
        dni = input("Ingrese DNI del cliente a actualizar: ")
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        for i, client in enumerate(clients):
            if client["dni"] == dni:
                nombre = input("Nuevo nombre (Enter para no cambiar): ")
                apellido = input("Nuevo apellido (Enter para no cambiar): ")
                valor = input("Nuevo valor (Enter para no cambiar): ")
                if nombre:
                    client["nombre"] = nombre
                if apellido:
                    client["apellido"] = apellido
                if valor:
                    try:
                        client["valor"] = float(valor)
                    except ValueError:
                        print("Valor inválido. No se cambió.")
                clients[i] = client
                json_file.save(clients)
                print("Cliente actualizado correctamente.")
                break
        else:
            print("Cliente no encontrado.")
        input("Presione una tecla para continuar...")

    def delete(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(red_color + "Eliminar Cliente" + reset_color)
        dni = input("Ingrese DNI del cliente a eliminar: ")
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        for i, client in enumerate(clients):
            if client["dni"] == dni:
                confirm = input(f"¿Está seguro de eliminar a {client['nombre']} {client['apellido']}? (s/n): ").lower()
                if confirm == "s":
                    clients.pop(i)
                    json_file.save(clients)
                    print("Cliente eliminado correctamente.")
                else:
                    print("Operación cancelada.")
                break
        else:
            print("Cliente no encontrado.")
        input("Presione una tecla para continuar...")

    def consult(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(green_color + "Consulta de Clientes" + reset_color)
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        for cli in clients:
            print(f"{cli['dni']}  {cli['nombre']}  {cli['apellido']}  Valor: {cli['valor']}")
        input("Presione una tecla para continuar...")


class CrudProducts(ICrud):
    def create(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(green_color + "Registrar Producto" + reset_color)
        id = input("ID Producto: ")
        descripcion = input("Descripción: ")
        precio = input("Precio: ")
        stock = input("Stock: ")

        try:
            id = int(id)
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            print("ID, precio o stock inválido.")
            return

        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        if any(prod["id"] == id for prod in productos):
            print("Producto ya existe.")
        else:
            productos.append({"id": id, "descripcion": descripcion, "precio": precio, "stock": stock})
            json_file.save(productos)
            print("Producto guardado correctamente.")
        input("Presione una tecla para continuar...")

    def update(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(blue_color + "Actualizar Producto" + reset_color)
        id = input("Ingrese ID del producto a actualizar: ")
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        for i, prod in enumerate(productos):
            if prod["id"] == int(id):
                descripcion = input("Nueva descripción (Enter para no cambiar): ")
                precio = input("Nuevo precio (Enter para no cambiar): ")
                stock = input("Nuevo stock (Enter para no cambiar): ")

                if descripcion:
                    prod["descripcion"] = descripcion
                if precio:
                    try:
                        prod["precio"] = float(precio)
                    except ValueError:
                        print("Precio inválido.")
                if stock:
                    try:
                        prod["stock"] = int(stock)
                    except ValueError:
                        print("Stock inválido.")

                productos[i] = prod
                json_file.save(productos)
                print("Producto actualizado correctamente.")
                break
        else:
            print("Producto no encontrado.")
        input("Presione una tecla para continuar...")

    def delete(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(red_color + "Eliminar Producto" + reset_color)
        id = input("Ingrese ID del producto a eliminar: ")
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        for i, prod in enumerate(productos):
            if prod["id"] == int(id):
                confirm = input(f"¿Eliminar producto {prod['descripcion']}? (s/n): ").lower()
                if confirm == "s":
                    productos.pop(i)
                    json_file.save(productos)
                    print("Producto eliminado correctamente.")
                else:
                    print("Operación cancelada.")
                break
        else:
            print("Producto no encontrado.")
        input("Presione una tecla para continuar...")

    def consult(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print(green_color + "Consulta de Productos" + reset_color)
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        for prod in productos:
            print(f"{prod['id']}  {prod['descripcion']}  ${prod['precio']}  Stock: {prod['stock']}")
        input("Presione una tecla para continuar...")

class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.solo_numeros("Error: Solo numeros",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line);
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            if invoices:
                ult_invoices = invoices[-1]["factura"] + 1
            else:
                ult_invoices = 1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
    
    def update(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Actualizar Venta"+reset_color)
        gotoxy(2,4);invoice = input("Ingrese número de factura a actualizar: ")
    
        if not invoice.isdigit():
            print("Número inválido.")
            return

        invoice = int(invoice)
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoices = json_file.read()

        for i, venta in enumerate(invoices):
            if venta["factura"] == invoice:
                gotoxy(2,6);print(f"Factura encontrada: {venta}")
                gotoxy(2,10);nuevo_cliente = input("Nuevo nombre del cliente (Enter para no cambiar): ")
                gotoxy(2,12);nuevo_total = input("Nuevo total (Enter para no cambiar): ")

                if nuevo_cliente:
                    venta["cliente"] = nuevo_cliente
                if nuevo_total:
                    try:
                        venta["total"] = float(nuevo_total)
                    except ValueError:
                        print("Total inválido. No se cambió.")

                invoices[i] = venta
                json_file.save(invoices)
                gotoxy(2,14);print(green_color+"Venta actualizada correctamente."+reset_color)
                break
        else:
            gotoxy(2,6);print(red_color+"Factura no encontrada."+reset_color)

        input("Presione una tecla para continuar...")
    
    def delete(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(red_color+"*"*90+reset_color)
        gotoxy(30,2);print(red_color+"Eliminar Venta"+reset_color)
        gotoxy(2,4);invoice = input("Ingrese número de factura a eliminar: ")

        if not invoice.isdigit():
            gotoxy(2,6);print("Número inválido.")
            return

        invoice = int(invoice)
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoices = json_file.read()

        for i, venta in enumerate(invoices):
            if venta["factura"] == invoice:
                gotoxy(2,6);print(f"Factura encontrada: {venta}")
                gotoxy(2,8);confirm = input("¿Está seguro que desea eliminar esta venta? (s/n): ").lower()
                if confirm == 's':
                    invoices.pop(i)
                    json_file.save(invoices)
                    gotoxy(2,10);print(red_color+"Venta eliminada correctamente."+reset_color)
                else:
                    gotoxy(2,10);print("Operación cancelada.")
                break
        else:
            gotoxy(2,6);print(red_color+"Factura no encontrada."+reset_color)

        input("Presione una tecla para continuar...")
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            print(f"Impresion de la Factura#{invoice}")
            print(invoices)
        else:    
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            print("Consulta de Facturas")
            for fac in invoices:
                print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")
            
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), 
            invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))
            total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            print("filter cliente: ",total_client)
            print(f"map Facturas:{totales_map}")
            print(f"              max Factura:{max_invoice}")
            print(f"              min Factura:{min_invoice}")
            print(f"              sum Factura:{tot_invoices}")
            print(f"              reduce Facturas:{suma}")
        x=input("presione una tecla para continuar...")    

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()  
            customer = CrudClients()  
            menu_clients = Menu("Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                customer.create()
            elif opc1 == "2":
                customer.update()
            elif opc1 == "3":
                customer.delete()
            elif opc1 == "4":
                customer.consult()
            print("Regresando al menu Clientes...")
            # time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()   
            product = CrudProducts() 
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                product.create()
            elif opc2 == "2":
                product.update()
            elif opc2 == "3":
                product.delete()
            elif opc2 == "4":
                product.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            
            elif opc3 == "3":
                sales.update()
                time.sleep(2)
            
            elif opc3 == "4":
                sales.delete()
                time.sleep(2)
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()

input("Presione una tecla para salir...")
borrarPantalla()

