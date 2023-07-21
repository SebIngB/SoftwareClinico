import tkinter as tk

def show_info(treeview, data):
    treeview.delete(*treeview.get_children())
    treeview["columns"] = list(data.columns)# type: ignore

    for col in data.columns:# type: ignore
        treeview.heading(col, text=col)
        treeview.column(col,minwidth=250, width=250, stretch=False) 
        #Stretch en False evito que se modifiquen el tamaño de las columnas, además de tener un ancho de columna estatico
        
    for index, row in data.iterrows():# type: ignore
        treeview.insert("", tk.END, values=list(row))

