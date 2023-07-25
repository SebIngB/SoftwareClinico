import tkinter as tk
from tkinter import ttk
from procesamiento.base_datos import database 
#import pandas as pd
#from gspread_dataframe import set_with_dataframe 
#import time
#import datetime
#from collections import Counter
from procesamiento.select_sheets import view_select
from procesamiento.modificar_view import modify_view
from procesamiento.config_consult import process
from procesamiento.send_inf_cons import send_information
from procesamiento.creation_treeview import show_info

class app:
    def __init__(self):
        #---------------------- Configuración de la ventana principal ----------------------
        self.master = tk.Tk()
        self.master.title('Ventana principal')
        # obtener el tamaño de la pantalla
        self.width_window = self.master.winfo_screenwidth()
        self.height_window = self.master.winfo_screenheight()

        # ajustar el tamaño de la ventana de acuerdo al tamaño de la pantalla
        self.master.geometry(f"{self.width_window}x{self.height_window}")

        #---------------------- Creación variables globales --------------------------
        self.name_sheet = tk.StringVar() #Variable que guarda el nombre de la sheet a conectar
        self.select_count = tk.StringVar() #Variable que guarda la cantidad de sheets a visualizar
        self.select_view = tk.StringVar() #Variable que guarda la seleccion de la sheet a visualizar
        self.resaltar = tk.StringVar() #variable que guarda la seleccion de resaltar los datos del view
        self.cod_equipo_view = tk.StringVar() #variable que guarda el codigo del equipo del view
        self.select_mod_view = tk.StringVar() #variable que guarda el modo de modificacion del view
        self.select_colum_view = tk.StringVar() #variable que guarda la columna a modificar del view
        self.modification_value_view = tk.StringVar() #variable que guarda el valor a modificar del view
        self.select_common = tk.StringVar() #variable que guarda el valor de la columna comun del consult
        self.select_mode_cons = tk.StringVar() #variable que guarda el modo de consulta del consult
        self.select_column_data = tk.StringVar() #variable que guarda la selección de la columna de datos agregar del consult

        self.create_widgets_principal()
        self.master.mainloop()

    def create_frame(self):
        # ---------------- Frames para la pestaña view_modify -------------------------
        self.frame_view = tk.Frame(self.second_window)
        self.view_mod = tk.Frame(self.frame_view)
        self.view_mod1 = tk.Frame(self.frame_view)
        self.view_mod2 = tk.Frame(self.frame_view)

        self.view_mod.config(width=self.width_window, height=self.height_window//4.5, bg='turquoise1') 
        self.view_mod1.config(width=self.width_window, height=self.height_window//2.2)
        self.view_mod2.config(width=self.width_window, height=self.height_window//4.5, bg='turquoise1') # type: ignore

        # --------------- Frame para la pestaña consult --------------------------------- 
        self.frame_consult = tk.Frame(self.second_window)
        self.cons = tk.Frame(self.frame_consult)
        self.cons1 = tk.Frame(self.frame_consult)
        self.cons2 = tk.Frame(self.frame_consult)

        self.cons.config(width=self.width_window, height=self.height_window//4.5, bg='turquoise1')
        self.cons1.config(width=self.width_window, height=self.height_window//2.2)
        self.cons2.config(width=self.width_window, height=self.height_window//4.5, bg='turquoise1')  

    def create_widgets_principal(self):
        # ---------------------- Creación de los widgets -------------------
        label_principal = tk.Label(self.master, text="Ingresar nombre del Google Sheet a trabajar: ")
        label_principal.place(relx=0.42, rely=0.3)

        entry_principal = tk.Entry(self.master, textvariable=self.name_sheet)
        entry_principal.place(relx=0.435, rely=0.35, width=200, height=25)

        label_count_principal = tk.Label(self.master, text="Ingrese la cantidas de hojas del Google Sheet:")
        label_count_principal.place(relx=0.42, rely=0.4)

        entry_count_principal = tk.Entry(self.master, textvariable=self.select_count)
        entry_count_principal.place(relx=0.435, rely=0.45, width=200, height=25)

        boton_principal = tk.Button(self.master, text="Conectar", command=self.creation_secondwindow)
        boton_principal.place(relx=0.45, rely=0.5, width=150, height=25)

    def creation_widgets_second(self):
        # ------------------------------ Creación de las pestañas -----------------------------------------
        self.option_menu = tk.Menu(self.second_window)
        self.option_menu.add_command(label="Inicio", command=self.second_window.destroy)
        self.option_menu.add_command(label="Visualizar y modificar", command=self.view_modify)
        self.option_menu.add_command(label="Consultar", command=self.consult)
        self.second_window.config(menu=self.option_menu)

        #----------------------------- Widgets de la pestaña view_modify -----------------------------------
        self.combobox_view = ttk.Combobox(self.view_mod, textvariable=self.select_view, values=self.namesheet_list)
        self.combobox_view.place(relx=0.1, rely=0.45)

        btn_show_view = tk.Button(self.view_mod, text="Mostrar", command=self.show)
        btn_show_view.place(relx=0.2, rely=0.45)

        self.entry_view = ttk.Combobox(self.view_mod, textvariable=self.resaltar, values=['Serial','Estado'])
        self.entry_view.place()
        self.entry_view.place_forget()

        self.btn1_show_view = tk.Button(self.view_mod, text="Resaltar", command=self.resaltar_view)
        self.btn1_show_view.place()
        self.btn1_show_view.place_forget()

        self.scrol_vertical_view = tk.Scrollbar(self.view_mod1, orient='vertical')
        self.scrol_vertical_view.place(x=self.width_window-25, y=0, width=25, height=self.height_window//2.2)

        self.scrol_horizontal_view = tk.Scrollbar(self.view_mod1, orient='horizontal')
        self.scrol_horizontal_view.place(x=0, y=(self.height_window//2.2)-20, width=self.width_window, height=20)

        self.treeview_view = ttk.Treeview(self.view_mod1, show="headings")
        self.treeview_view.place(x=0, y=0, width=self.width_window-25, height=self.height_window//2.32)

        self.treeview_view.configure(yscrollcommand=self.scrol_vertical_view.set, xscrollcommand=self.scrol_horizontal_view.set, selectmode='extended')
        self.scrol_vertical_view.configure(command=self.treeview_view.yview)
        self.scrol_horizontal_view.configure(command=self.treeview_view.xview)

        self.label_cantidad_view = tk.Label(self.view_mod2, text=" ")
        self.label_cantidad_view.place()
        self.label_cantidad_view.place_forget()

        self.label_codigo_view = tk.Label(self.view_mod2, text="Digite el codigo del equipo:")
        self.label_codigo_view.place()
        self.label_codigo_view.place_forget()

        self.entry_codigo_view = tk.Entry(self.view_mod2, textvariable=self.cod_equipo_view)
        self.entry_codigo_view.place()
        self.entry_codigo_view.place_forget()

        self.label_modo_view = tk.Label(self.view_mod2, text="Escoja el modo de modificacion:")
        self.label_modo_view.place()
        self.label_modo_view.place_forget()

        self.combobox_modo_view = ttk.Combobox(self.view_mod2, textvariable=self.select_mod_view, values=['Descripcion/Serial/Centro de Costo',
                                                                                                   'Modificar otras columnas']) 
        self.combobox_modo_view.place()
        self.combobox_modo_view.place_forget()

        self.label_colum_mod = tk.Label(self.view_mod2, text='Seleccione la columna a modificar:')
        self.label_colum_mod.place()
        self.label_colum_mod.place_forget()

        self.combobox_colum_mod_view = ttk.Combobox(self.view_mod2, textvariable=self.select_colum_view)
        self.combobox_colum_mod_view.place()
        self.combobox_colum_mod_view.place_forget()
        
        self.label_value_mod = tk.Label(self.view_mod2, text='Escriba el valor a modificar:')
        self.label_value_mod.place()
        self.label_value_mod.place_forget()

        self.entry_value_mod = tk.Entry(self.view_mod2, textvariable=self.modification_value_view)
        self.entry_value_mod.place()
        self.entry_value_mod.place_forget()

        self.btn_modificar_view = ttk.Button(self.view_mod2, text="Modificar", command=self.modificar)
        self.btn_modificar_view.place()
        self.btn_modificar_view.place_forget()

        self.label_time_view = tk.Label(self.view_mod2, text='')
        self.label_time_view.place()
        self.label_time_view.place_forget()

        #----------------------------- Widgets de la pestaña consult -----------------------------------
        self.label_column_common_consult = tk.Label(self.cons, text="Seleccione columna en comun:")
        self.label_column_common_consult.place(relx=0.06, rely=0.3)

        self.combobox_cons_common = ttk.Combobox(self.cons, textvariable=self.select_common,  values=['Serial','Descripcion','Activo Fijo','Fecha'])
        self.combobox_cons_common.place(relx=0.07, rely=0.45)

        self.label_mode_cons = tk.Label(self.cons, text="Modo consulta:")
        self.label_mode_cons.place(relx=0.18, rely=0.3)

        self.combobox_mode_cons = ttk.Combobox(self.cons, textvariable=self.select_mode_cons, values= ['A=<-B', 'A=->B'])
        self.combobox_mode_cons.place(relx=0.18, rely=0.45)

        self.label_consult_data = tk.Label(self.cons, text="Datos agregar:")
        self.label_consult_data.place(relx=0.3, rely=0.3)

        self.combobox_data = tk.Entry(self.cons, textvariable=self.select_column_data)
        self.combobox_data.place(relx=0.3, rely=0.45)

        self.btn_show_cons = tk.Button(self.cons, text="Mostrar", command=self.show_data_cons)
        self.btn_show_cons.place(relx=0.42, rely=0.45)

        self.btn_send_cons = tk.Button(self.cons, text="Transferir", command=self.send_data_cons)
        self.btn_send_cons.place()
        self.btn_send_cons.place_forget()

        self.scrol_vertical_cons = tk.Scrollbar(self.cons1, orient='vertical')
        self.scrol_vertical_cons.place(x=self.width_window-25, y=0, width=25, height=self.height_window//2.2)

        self.scrol_horizontal_cons = tk.Scrollbar(self.cons1, orient='horizontal')
        self.scrol_horizontal_cons.place(x=0, y=(self.height_window//2.2)-20, width=self.width_window, height=20)

        self.treeview_cons = ttk.Treeview(self.cons1, show="headings")
        self.treeview_cons.place(x=0, y=0, width=self.width_window-25, height=self.height_window//2.32)

        self.treeview_cons.configure(yscrollcommand=self.scrol_vertical_cons.set, xscrollcommand=self.scrol_horizontal_cons.set, selectmode='extended')
        self.scrol_vertical_cons.configure(command=self.treeview_cons.yview)
        self.scrol_horizontal_cons.configure(command=self.treeview_cons.xview)

        self.label_amount_data_cons = tk.Label(self.cons2, text=" ")
        self.label_amount_data_cons.place()
        self.label_amount_data_cons.place_forget()

    def connect_sheet(self):
        filename = self.name_sheet.get()
        self.count = int(self.select_count.get())
        mySheet = database(filename, self.count)
        self.df_list, self.sheet_list, self.worksheet_list, self.namesheet_list = mySheet.data_base()

    def creation_secondwindow(self):
        self.connect_sheet()
        # --------------------- Creacion ventana secundaria -----------------
        self.second_window = tk.Toplevel(self.master)
        self.second_window.title('Ventana secundaria')

        # ajustar el tamaño de la ventana de acuerdo al tamaño de la pantalla
        self.second_window.geometry(f"{self.width_window}x{self.height_window}")

        # Ejecuto los frames
        self.create_frame()

        # Ejecuto creacion de los widgets
        self.creation_widgets_second()

    # Pestaña de visualizacion y modificacion de celdas
    def view_modify(self):
        self.frame_consult.pack_forget()  # Ocultar el frame consultar
  
        print('visualizacion')
        self.frame_view.pack()
        self.view_mod.pack()
        self.view_mod1.pack()
        self.view_mod2.pack()

    # Pestaña de consultar igualdades y concatenar informacion
    def consult(self):
        self.frame_view.pack_forget()  # Ocultar el frame visualizar

        print('consultar')
        self.frame_consult.pack() 
        self.cons.pack()
        self.cons1.pack()
        self.cons2.pack()
    
    def show(self):
        self.connect_sheet()

        self.selected = self.select_view.get()

        df_view, self.worksheet_view = view_select(self.count, self.selected, self.df_list, self.worksheet_list, self.namesheet_list)

        if self.selected != "":
            self.entry_view.place(relx=0.25, rely=0.45)
            self.btn1_show_view.place(relx=0.35, rely=0.45)

            self.label_cantidad_view.place(relx=0.025, rely=0.1)
            self.label_codigo_view.place(relx=0.025, rely=0.2)
            self.entry_codigo_view.place(relx=0.025, rely=0.3)

            self.label_modo_view.place(relx=0.125, rely=0.2)
            self.combobox_modo_view.place(relx=0.125, rely=0.3)

            self.label_colum_mod.place(relx=0.244, rely=0.2)
            self.combobox_colum_mod_view.configure(values=list(df_view.columns))
            self.combobox_colum_mod_view.place(relx=0.244, rely=0.3)

            self.label_value_mod.place(relx=0.37, rely=0.2)
            self.entry_value_mod.place(relx=0.37, rely=0.3)

            self.btn_modificar_view.place(relx=0.47, rely=0.3)

            self.label_time_view.place(relx=0.52, rely=0.3)

        tamaño = df_view.shape

        self.label_cantidad_view['text'] = f'La {self.selected} tiene {tamaño[0]} filas y {tamaño[1]} columnas'
        show_info(self.treeview_view, df_view)
   
    def resaltar_view(self):
        
        self.columnas_view = list(self.treeview_view['columns'])
         
        if self.resaltar.get() == 'Serial':
            self.treeview_view.tag_configure('filas_vacias', background='red')
            self.indice_serial = self.columnas_view.index('Serial')

             # Iterar sobre los elementos del Treeview y aplicar la etiqueta a las filas que contienen celdas vacías o "NO REGISTRA"
            for row in self.treeview_view.get_children():
                values = self.treeview_view.item(row)['values']
                if 'NO REGISTRA' in str(values[self.indice_serial]) or '' == str(values[self.indice_serial]) or 'Desconocido'==str(values[self.indice_serial]): 
                    self.treeview_view.item(row, tags=('filas_vacias',))
        
        elif self.resaltar.get() == 'Estado':
            self.treeview_view.tag_configure('filas_vacias', background='yellow')
            self.indice_estado = self.columnas_view.index('Estado')

             # Iterar sobre los elementos del Treeview y aplicar la etiqueta a las filas que contienen celdas vacías o "NO REGISTRA"
            for row in self.treeview_view.get_children():
                values = self.treeview_view.item(row)['values']
                if 'I - Dado de Baja' == str(values[self.indice_estado]):
                    self.treeview_view.item(row, tags=('filas_vacias',))
    
    def modificar(self):
        
        if self.select_mod_view.get() == 'Descripcion/Serial/Centro de Costo':
            equipo = self.worksheet_view.findall(self.cod_equipo_view.get()) #Me devuelve un valor de R#C# que indica fila,columna, selecciona la fila # type: ignore

            ubicacion = self.worksheet_view.find(self.select_colum_view.get()) #Solo selecciono el valor de la columna # type: ignore

            modify_view(equipo, ubicacion, self.worksheet_view, self.modification_value_view, 
                                   self.view_mod2, self.label_time_view, self.select_colum_view)
            self.update_view()
        
        elif self.select_mod_view.get() == 'Modificar otras columnas':
            fila = self.worksheet_view.find(self.cod_equipo_view.get()) #Me devuelve un valor de R#C# que indica fila,columna, selecciona la fila# type: ignore

            columna = self.worksheet_view.find(self.select_colum_view.get()) #Solo selecciono el valor de la columna # type: ignore

            self.worksheet_view.update_cell(fila.row, columna.col, self.modification_value_view.get())# type: ignore

            self.update_view()
         
    def update_view(self):
        self.connect_sheet()
        self.show()

        equipo = self.worksheet_view.findall(self.cod_equipo_view.get())# type: ignore
        objectivo = self.worksheet_view.findall(self.modification_value_view.get())# type: ignore

        estado_anterior = len(equipo)
        estado_actual = len(objectivo)

        self.label_time_view['text'] = f'Hay {self.cod_equipo_view.get()}: {estado_anterior}/Hay {self.modification_value_view.get()}: {estado_actual}'

        self.cod_equipo_view.set('')
        self.select_mod_view.set('')
        self.select_colum_view.set('')
        self.modification_value_view.set('')

    def show_data_cons(self):
        self.connect_sheet()
        self.common_column = self.select_common.get()
        self.column_data = self.select_column_data.get()
        
        self.send_data, self.worksheet_cons, self.sheet_inf_extract = process(self.combobox_mode_cons.get(), self.df_list, self.common_column, self.column_data, self.worksheet_list) # type: ignore
        
        #----------------------------- Ubication widgets -------------------------------
        self.btn_show_cons.config(text='Actualizar')
        
        self.btn_send_cons.place(relx=0.52, rely=0.45)
        self.label_amount_data_cons.place(relx=0.45, rely=0.45)

        #----------------------------- Information filter ------------------------------
        print(self.send_data[[f'{self.common_column}',f'{self.column_data}']])
        
        show_info(self.treeview_cons, self.send_data)

        shape_data_cons = self.send_data.shape #type: ignore

        self.label_amount_data_cons['text'] = f'Hay {shape_data_cons[0]} datos para enviar'
    
    def send_data_cons(self):
        
        send_information(self.send_data, self.worksheet_cons, self.common_column, self.column_data)





       










