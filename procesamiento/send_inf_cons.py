import time
import datetime

def send_information(data, worksheet, column_common, column_data):
    Serial = []
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resp = ''
    adition_cons = 0

    ubi_column_data = worksheet.find(column_data) #Solo selecciono el valor de la columna # type: ignore
    number = ubi_column_data.col
    print(number)

    before_time_cons = datetime.datetime.now()

    amount_min_cons = 50 # Cantidad de elementos a enviar

    # Calcular cuántos ciclos se necesitan
    print(len(data))
    num_ciclos_cons = len(data) // amount_min_cons
    start_time_cons = time.perf_counter()
    fin = 0

    if num_ciclos_cons <= 0:
        num_ciclos_cons = 1
        amount_min_cons = len(data)
        print('menor a 1')

    print(f'Faltan {num_ciclos_cons} minutos')

    for i in range(num_ciclos_cons):
                
        inicio = i * amount_min_cons
        fin = inicio + amount_min_cons
            
        buscar = data[inicio:fin][column_common].values
        enviar = data[inicio:fin][column_data].values
        print(f'seriales {buscar}')
        print(f'elementos a enviar {enviar}')
        for fil in buscar:
            Serial.append(worksheet.find(f"{fil}"))# type: ignore
  
        elementos_a_enviar_cons = Serial[inicio:fin]
        print(elementos_a_enviar_cons)
        while number > 0:
            indice = (number - 1) % 26
            resp = letras[indice] + resp
            number = (number - 1) // 26
        co = 0
        for e in elementos_a_enviar_cons:
            column_sheet_data_cons = f'{resp}{e.row}'
            worksheet.update(column_sheet_data_cons,f'{enviar[i]}')# type: ignore
            co += 1
            print(f've{co}')

        end_time_cons = time.perf_counter()
        elapsed_time_cons = end_time_cons - start_time_cons
        print(elapsed_time_cons)
        if elapsed_time_cons < 70:
            adition_cons = 70-elapsed_time_cons
        print(adition_cons)
        time.sleep(adition_cons)
        num_ciclos_cons -= 1
        print(f'Faltan {num_ciclos_cons} minutos')


    print('termino ciclo')
   
    print(fin)
    print(data[fin:][column_common])
    buscar = data[fin:][column_common].values
    print(f'elementos a buscar 2{buscar}')

    for fil in buscar:
        Serial.append(worksheet.find(f"{fil}"))# type: ignore

    # Comprobar si hay elementos adicionales para enviar
    if len(Serial) % amount_min_cons > 0:
        # Obtener los elementos restantes
            ubi_data_cons = Serial[num_ciclos_cons * amount_min_cons:]
            enviar = data[num_ciclos_cons * amount_min_cons:][column_data].values
            print(f'elementos a enviar 2 {buscar} {enviar}')
            co = 0
            print(f'ubicaciones {buscar}')
            for i in ubi_data_cons:
                    
                ubi_sheet_data_cons = f'{resp}{i.row}'
                worksheet.update(ubi_sheet_data_cons,f'{enviar[co]}')# type: ignore
                co += 1
                print(f'va{co}')
            
    actual_cons = datetime.datetime.now()
        
       

    return print(f'Se demoro {actual_cons.minute - before_time_cons.minute} minutos')