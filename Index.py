import pandas as pd
import openpyxl

#显示所有列
pd.set_option('display.max_columns', None)

path= 'C:/Users/Administrator/Downloads/'
fname= 'export_indices_from_wglh.csv'
ofname= 'export_indices_from_wglh.xlsx'
sname= '202303'

workbook = openpyxl.load_workbook(path + ofname)

list = workbook.get_sheet_names()

if sname in list:
    std = workbook.get_sheet_by_name(sname)
    workbook.remove_sheet(std)
    workbook.save(path + ofname)

df = pd.read_csv(path + fname)
print(df.columns)
df1 = df.rename(columns = {'PE.市值加权': '加权PE'
                         ,'百分位': 'PE百分比'
                         ,'PB.市值加权': '加权PB'
                         ,'百分位.1': 'PB百分比'})

df2 = df1.drop(df1.index[0])

df2['加权PE'] = pd.to_numeric(df2['加权PE'].replace("'-1.00", 1000), errors='coerce')

df2['加权PB'] = pd.to_numeric(df2['加权PB'], errors='coerce')

df2['股息'] = df2['股息'].str.rstrip('%').astype('float')/100.0

df2['收益率'] = df2['加权PB']/df2['加权PE']*100 - df2['股息']*(df2['加权PB']-1)

df2 = df2.sort_values(by=['收益率'], ascending=False)

with pd.ExcelWriter(path + ofname,  mode="a", engine="openpyxl") as writer:
    df2.to_excel(writer, sheet_name=sname, index=False)