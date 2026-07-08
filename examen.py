# Matias_Seco_ET
def validar_codigo(codigo):
    return bool(codigo and codigo.strip())
def validar_nombre(nombre):
    return bool(nombre and nombre.strip())
def validar_tipo(tipo):
    return tipo.strip().lower() in ['mensual' , ' trimestral,' 'anual']
def validar_duracion(duracion):
    try:
        return int(duracion) > 0
    except ValueError:
        return False
def validar_acceso_piscina(acceso):
    return acceso.strip().lower() in ['s', 'n']
def validar_incluye_clases(clases):
    return clases.strip().lower() in ['s', 'n']
def validar_horario(horario):
    return bool(horario and horario.strip())
def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        return int(cupos) >= 0
    except ValueError:
        return False
    
def eliminar_plan_sistema(codigo):
    codigo_norm = codigo.strip().upper()
    if buscar_codigo(codigo_norm):
        del planes[codigo_norm]    


def leer_opcion():
    print("\n======= MENU PRINCIPAL =======")
    print("1. Cupos por tipo de plan")
    print("2. Busqueda de planes por rango de precio")
    print("3. Acualizar precio de plan")
    print("4. Agregar plan") 
    print("5. Eliminar plan")
    print("6. Salir")
    print("============================")

    try:
        opcion = int(input("Ingrese opcion: "))
        if 1 <= opcion <= 6:
            return opcion
        print("Debe seleccionar una opcion valida")
        return None
    except ValueError:
        print("Debe seleccionar una opcion valida")
        return None
    
    
    
def cupos_tipo(tipo, planes, inscripciones):
    tipo_norm = tipo.strip().lower()
    total_acumulado = 0

    for codigo, datos in planes.items():
        if datos[1].lower() == tipo_norm:
            cupos = inscripciones[codigo][1]
            total_acumulado += cupos
    print(f"El total de cupos disponibles es: {total_acumulado}")

def busqueda_precio(p_min, p_max, planes, inscripciones):
    lista_resultados = []
    for codigo, datos_ins in inscripciones.items():
        precio = datos_ins[0]
        cupos = datos_ins[1]
        if p_min <= precio <= p_max and cupos > 0:
            nombre_plan = planes[codigo][0]
            formato = f"{nombre_plan}--{codigo}"
            lista_resultados.append(f"{nombre_plan}---{codigo}")

    if not lista_resultados:
        print("No hay planes en ese rango de precios.")
    else:
        lista_resultados.sort()
        print(f"Los planes encotrados son: {lista_resultados}")

def buscar_codigo(codigo, inscripciones):
    return codigo.strip().upper() in inscripciones
def actualizar_precio(codigo, nuevo_precio, inscripciones):
    codigo_norm = codigo.strip().upper()
    if buscar_codigo(codigo_norm, inscripciones):
        inscripciones[codigo_norm][0] = nuevo_precio
        return True
    return False


def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    codigo_norm = codigo.strip().upper()
    piscina_bool = True if acceso_piscina.strip().lower() == 's' else False
    clases_bool = True if incluye_clases.strip().lower() == 's' else False

    planes[codigo_norm] = [nombre, tipo.strip().lower(), int(duracion), piscina_bool, clases_bool, horario]
    inscripciones[codigo_norm] = [int(precio), int(cupos)]

def eliminar_plan(codigo, planes, inscripciones):
    codigo_norm = codigo.strip().upper()
    if buscar_codigo(codigo_norm, inscripciones):
        del planes[codigo_norm]
        del inscripciones[codigo_norm]
        return True
    return False


def main():
    planes = {
        'F001': ['Plan Basico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
    }

    inscripciones = {

        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15],
        
    }

        

while True:
    opcion = leer_opcion()
    if opcion is None:
        continue
    
    if opcion == 1:
        tipo = input("Ingrese tipo de plan a consultar: ")
        cupos_tipo(tipo, planes, inscripciones)
    elif opcion == 2:
        try:

            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
            if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                busqueda_precio(p_min, p_max, planes, inscripciones)
            else:
                print("Debe ingresar valores enteros validos (minimo menor o igual al maximo).")
        except ValueError:
            print("Debe ingresar valores enteros")

    elif opcion == 3:
        while True:
            codigo = input("Ingrese codigo del plan: ").strip().upper()
            nuevo_precio_raw = input("Ingrese nuevo precio: ")

            if validar_precio(nuevo_precio_raw):
                exito = actualizar_precio(codigo, int(nuevo_precio_raw), inscripciones)
                if exito:
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")
            else:
                print("El nuevo precio debe ser un valor entero positivo.")

            resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
            if resp != 's':
                break

    elif opcion == 4:

        c = input("Ingrese codigo del plan: ")
        if not validar_codigo(c):
            print("Error: El codigo no puede estar vacio."); continue
        if buscar_codigo(c, inscripciones,):
            print("El codigo ya existe"); continue

        n = input("Ingrese nombre del plan: ")
        if not validar_nombre(n):
            print("Error: El nombre no puede estar vacio. "); continue
        
        t = input("Ingrese tipo (mensual/trimestral/anual): ")
        if not validar_tipo(t):
            print("Error: Tipo incorrecto."); continue
        d = input("Ingrese duracion (meses): ")
        if not validar_duracion(d):
            print("Error: Duracion incorrecta"); continue
        ap = input("¿Incluye acceso a piscina? (s/n): ")
        if not validar_acceso_piscina(ap):
            print("Error Debe ser 's' o 'n'." ); continue
        ic = input("¿Incluye clases grupales? (s/n): ")
        if not validar_incluye_clases(ic):
            print("Error: Debe ser  's' o 'n'."); continue
        h = input("Ingrese horario: ")
        if not validar_horario(h):
            print("Error: El horario no puede estar vacio."); continue
        p = input("Ingrese precio: ")
        if not validar_precio(p):
            print("Error: Precio incorrecto."); continue
        cu = input("Ingrese cupos: ")
        if not validar_cupos(cu):
            print("Eror: Cupos incorrectos"); continue
        
        agregar_plan(c, n, t, d, ap, ic, h, p, cu, planes, inscripciones)
        print("Plan agregado")

   
        
        


        
                                                  

    



                                          
    
                   
