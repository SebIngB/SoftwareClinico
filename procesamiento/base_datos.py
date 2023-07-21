import procesamiento.conexion_sheet as conexion
import pandas as pd

class database:
    def __init__(self, filename, count):
        self.filename = filename
        self.count = count

    def data_base(self):

        worksheet = conexion.sheet(self.filename)
        worksheet_list = [0]*self.count
        sheet_list = [0]*self.count
        df_list = [0]*self.count
        name_sheet = []
        name = worksheet.worksheets()

        for i in range(self.count):
            worksheet_list[i] = worksheet.get_worksheet(i) # type: ignore
            sheet_list[i] = worksheet.get_worksheet(i).get_all_values()  # type: ignore
            df = pd.DataFrame(sheet_list[i], columns=sheet_list[i][0]) # type: ignore
            df_list[i] = df.drop([0], axis=0) # type: ignore

        for n in name:
            name_sheet.append(n.title)

        return df_list, sheet_list, worksheet_list, name_sheet
        '''
        #print(sheet[1])
        sheet1 = worksheet.get_worksheet(0)
        sheet2 = worksheet.get_worksheet(1)
        sheet3 = worksheet.get_worksheet(2)
        
        TEC_MEDICA = sheet1.get_all_values()
        METROLOGIA = sheet2.get_all_values()
        EJE_GUIA = sheet3.get_all_values()

        df = pd.DataFrame(TEC_MEDICA, columns=TEC_MEDICA[0])
        df_tec = df.drop([0], axis=0)
        df1 = pd.DataFrame(METROLOGIA, columns=METROLOGIA[0])
        df_met = df1.drop([0], axis=0)
        df2 = pd.DataFrame(EJE_GUIA, columns=EJE_GUIA[0])
        df_guia = df2.drop([0], axis=0)
        print(df_tec)
        return df_tec,df_met, df_guia, sheet1, sheet2, sheet3
        '''


    
