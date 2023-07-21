import pandas as pd

def process(mode, dataframe, column_common, column_data, worksheet_list):
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()

    if mode == "A=<-B":
        df1 = dataframe[0].copy()
        df1.drop_duplicates(subset=['Serial'], inplace=True)
        df1.replace(['NO REGISTRA',"",'NO REIGSTRA','','no registra'], pd.NA, inplace=True) # type: ignore
        df1.dropna(subset=['Serial'], inplace=True)

        df2 = dataframe[1].copy()
        df2.drop_duplicates(subset=['Serial'], inplace=True)
        df2.replace(['NO REGISTRA',"",'NO REIGSTRA','','no registra'], pd.NA, inplace=True) # type: ignore
        df2.dropna(subset=['Serial',f'{column_data}'], inplace=True)

        combination = df2[df2[f'{column_common}'].isin(df1[f'{column_common}'])]# type: ignore
        worksheet_cons = worksheet_list[0]
        data_pending = df1[df1[f'{column_data}'].isnull()]
        data_send = combination[combination[f'{column_common}'].isin(data_pending[f'{column_common}'])]
        search = dataframe[1]

        return data_send, worksheet_cons, search

