import time
import datetime

def modify_view(codigo, ubi_col, worksheet, value_mod, frame2_view, label_view, columna):
    anterior = datetime.datetime.now()

    elem_to_minute = 50

    # Calcular cuántos ciclos se necesitan
    num_ciclos = len(codigo) // elem_to_minute
    nu=num_ciclos
    start_time = time.perf_counter()
    print(f'Faltan {nu} minutos')
    label_view.config(text=f'Faltan {nu} minutos')
    frame2_view.update()
    aditional = 0
    for i in range(num_ciclos):
                
        inicio = i * elem_to_minute
        fin = inicio + elem_to_minute
        elementos_a_enviar = codigo[inicio:fin]
        for i in elementos_a_enviar:
            hoja = ''
            if columna.get() == 'Descripcion':
                hoja = f'{chr(ubi_col.col + 64)}{i.row}'

            if columna.get() == 'Serial':
                hoja = f'{chr(ubi_col.col + 64)}{i.row}'

            if columna.get() == 'Centro de Costo':
                hoja = f'{chr(ubi_col.col + 64)}{i.row}'
            
            print(hoja)
                    
            worksheet.update(hoja, value_mod.get())# type: ignore
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        if elapsed_time < 60:
            aditional = 65-elapsed_time
        time.sleep(aditional)
        nu -= 1
        label_view.config(text=f'Faltan {nu} minutos')
        frame2_view.update()
        print(f'Faltan {nu} minutos')
    print('termino ciclo')
    # Comprobar si hay elementos adicionales para enviar
    if len(codigo) % elem_to_minute > 0:
        # Obtener los elementos restantes
        elementos_a_enviar = codigo[num_ciclos * elem_to_minute:]
        print(len(elementos_a_enviar))
        for i in elementos_a_enviar:
                    
            if ubi_col.col == 1:
                hoja = f'A{i.row}'

            if ubi_col.col == 2:
                hoja = f'B{i.row}'

            if ubi_col.col == 3:
                hoja = f'C{i.row}'
            print(value_mod.get())
            worksheet.update(hoja, value_mod.get())# type: ignore

    actual = datetime.datetime.now()
    label_view.config(text=f'Terminado')
    frame2_view.update()
    return print(f'Se demoro {actual.minute - anterior.minute} minutos','\n','modify') # type: ignore
    