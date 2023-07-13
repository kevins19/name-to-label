import pandas as pd
# import arcgis

PROJECT_NAME = "WKRD_AGC_Transects_Fieldnotes_Survey123Connect"

d_df = pd.read_excel(PROJECT_NAME+'.xlsx', sheet_name = ['choices'])
df = d_df.get('choices')

fo = open('output.txt', 'w')

print(df)

label_dict = {}
for ind in df.index:
    name = str(df.loc[ind, 'name'])
    label = str(df.loc[ind, 'label'])
    if not pd.isnull(df.loc[ind, 'name']):
        label_dict[name] = label

print(label_dict)

fo.write('def convert_to_labels(original_dict):\n')
fo.write('\toutput = {}\n')
func = '\'for key in original_dict:\\n'
func += '\\toutput[key] = original_dict[key]\\n'

for name in label_dict:
    func += ('\\tif original_dict[key] == \\\'' + name + '\\\':\\n')
    func += ('\\t\\toutput[key] = \\\'' + label_dict[name] + '\\\'\\n')

fo.write('\texec(' + func + '\')\n')
fo.write('\treturn output')
fo.close()