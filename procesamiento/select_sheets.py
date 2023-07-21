import pandas as pd

def view_select(count, selection, df, sheet, name_sheet):
    df_view = pd.DataFrame()
    worksheet = None
    if count == 3:
        if selection == name_sheet[0]:
            df_view = df[0]
            worksheet = sheet[0]

        elif selection == name_sheet[1]: 
            df_view = df[1]
            worksheet = sheet[1]
            
        elif selection == name_sheet[2]:
            df_view = df[2]
            worksheet = sheet[2]
        
    elif count == 2:
        if selection == name_sheet[0]:
            df_view = df[0]
            worksheet = sheet[0]

        elif selection == name_sheet[1]: 
            df_view = df[1]
            worksheet = sheet[1]
        
    elif count == 1:
        if selection == name_sheet[0]:
            df_view = df[0]
            worksheet = sheet[0]
    
    return df_view, worksheet

