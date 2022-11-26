#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pandas as pd 

December_file = r'干熄焦生产记录台账（12月）.xlsx'

#December = pd.read_excel(December_file,sheet_name=1,index_col=0)

xlsx = pd.ExcelFile(December_file)

December_sheets = []
for sheet in xlsx.sheet_names:
    December_sheets.append(xlsx.parse(sheet))

December = pd.concat(December_sheets)

print(December)
print(December.shape)
