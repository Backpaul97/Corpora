# Необходиме библиотеки: pandas, openpyxl
import pandas as pd

input_table = pd.read_excel('C:\\Users\\Nikita\\Desktop\\Project6\\Разметка по словам.xlsx')

output_table_data = []

i = 0
while i < input_table.shape[0]:
    if input_table.loc[i, 'language_function_Vlasova'] == 'O':
        output_table_data.append([input_table.loc[i, 'word'], 'O'])
    else:
        tag = input_table.loc[i, 'language_function_Vlasova']
        collocation = str(input_table.loc[i, 'word'])
        i += 1
        while input_table.loc[i, 'language_function_Vlasova'] == tag:
            collocation += ' ' + str(input_table.loc[i, 'word'])
            i += 1
        i -= 1
        output_table_data.append([collocation, tag])
    i += 1

output_table = pd.DataFrame(output_table_data, columns=['word', 'language_function_Vlasova'])
output_table.to_excel('C:\\Users\\Nikita\\Desktop\\Project6\\Разметка по словосочетаниям.xlsx', index=False)
