import sys
sys.path.append('src')
from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}
df1 = DataFrame(data_dict, column_order = ['John', 'Sarah', 'Pete'])
if df1.data_dict != {'Pete': [1, 0, 1, 0], 'John': [2, 1, 0, 2], 'Sarah': [3, 1, 4, 0]}:
    print('data_dict failed on input for df1')
if df1.column_order != ['John', 'Sarah', 'Pete']:
    print('column_order failed on input for df1')
if df1.to_array() != [[2, 3, 1], [1, 1, 0], [0, 4, 1], [2, 0, 0]]:
    print('to_array failed on input for df1')
df2 = df1.select_columns(['Sarah', 'Pete'])
if df2.to_array() != [[3,1], [1,0], [4,1], [0,0]]:
    print('to_array failed on input for df2')
if df2.column_order != ['Sarah', 'Pete']:
    print('column_order failed on input for df2')
df3 = df1.select_rows([1,3])
if df3.to_array() != [[1,1,0], [2,0,0]]:
    print('to_array failed on input for df3')
arr = [['Kevin ', 'Fray ', 5], 
       ['Charles ', 'Trapp ', 17], 
       ['Anna ', 'Smith ', 13], 
       ['Sylvia ', 'Mendez ', 9]]
df4 = DataFrame.from_array(arr, column_order = ['firstname', 'lastname', 'age'])
if df4.order_by('age', ascending = True).to_array() != [['Kevin ', 'Fray ', 5], ['Sylvia ', 'Mendez ', 9], ['Anna ', 'Smith ', 13], ['Charles ', 'Trapp ', 17]]:
    print('test failed')
if df4.order_by('firstname', ascending = False).to_array() != [['Sylvia ', 'Mendez ', 9], ['Kevin ', 'Fray ', 5], ['Charles ', 'Trapp ', 17], ['Anna ', 'Smith ', 13]]:
    print('test failed')
if df4.to_json() != [{'firstname': 'Kevin ', 'lastname': 'Fray ', 'age': 5}, {'firstname': 'Charles ', 'lastname': 'Trapp ', 'age': 17}, {'firstname': 'Anna ', 'lastname': 'Smith ', 'age': 13}, {'firstname': 'Sylvia ', 'lastname': 'Mendez ', 'age': 9}]:
    print('to_json failed on input for df4')
json1 = df4.to_json()
df5 = DataFrame.from_json(json1, column_order = ['firstname', 'lastname', 'age'])
if df4.to_array() != df5.to_array():
    print('test failed')
if df4.to_json() != df5.to_json():
    print('test failed')
if df4.data_dict != df5.data_dict:
    print('test failed')

data_dict_a = {
    'Christine': [8, 2, 3],
    'Michael': [4, 7, 6],
    'Nora': [3, 5, 1]
}
dfa = DataFrame(data_dict_a, column_order = ['Christine', 'Michael', 'Nora'])
if dfa.data_dict != {'Christine': [8, 2, 3], 'Michael': [4, 7, 6], 'Nora': [3, 5, 1]}:
    print('data_dict failed on input for dfa')
if dfa.column_order != ['Christine', 'Michael', 'Nora']:
    print('column_order failed on input for dfa')
if dfa.to_array() != [[8,4,3], [2,7,5], [3,6,1]]:
    print('to_array failed on input for df1')
dfb = dfa.select_columns(['Christine', 'Michael'])
if dfb.to_array() != [[8,4], [2,7], [3,6]]:
    print('to_array failed on input for dfb')
if dfb.column_order != ['Christine', 'Michael']:
    print('column_order failed on input for dfb')
dfc = dfa.select_rows([1,2])
if dfc.to_array() != [[2,7,5], [3,6,1]]:
    print('to_array failed on input for dfc')
arr = [['Alique ', 'Klahejian ', 15], 
       ['Brenden ', 'Aldana ', 16], 
       ['Mike ', 'Manoukian ', 46], 
       ['Sarine ', 'Kaloghlian ', 9]]
dfd = DataFrame.from_array(arr, column_order = ['firstname', 'lastname', 'age'])
if dfd.order_by('age', ascending = False).to_array() != [['Mike ', 'Manoukian ', 46], ['Brenden ', 'Aldana ', 16], ['Alique ', 'Klahejian ', 15], ['Sarine ', 'Kaloghlian ', 9]]:
    print('test failed')
if dfd.order_by('lastname', ascending = False).to_array() != [['Mike ', 'Manoukian ', 46], ['Alique ', 'Klahejian ', 15], ['Sarine ', 'Kaloghlian ', 9], ['Brenden ', 'Aldana ', 16]]:
    print('test failed')
if dfd.to_json() != [{'firstname': 'Alique ', 'lastname': 'Klahejian ', 'age': 15}, {'firstname': 'Brenden ', 'lastname': 'Aldana ', 'age': 16}, {'firstname': 'Mike ', 'lastname': 'Manoukian ', 'age': 46}, {'firstname': 'Sarine ', 'lastname': 'Kaloghlian ', 'age': 9}]:
    print('to_json failed on input for dfd')
jsona = dfd.to_json()
dfe = DataFrame.from_json(jsona, column_order = ['firstname', 'lastname', 'age'])
if dfd.to_array() != dfe.to_array():
    print('test failed')
if dfd.to_json() != dfe.to_json():
    print('test failed')
if dfd.data_dict != dfe.data_dict:
    print('test failed')
