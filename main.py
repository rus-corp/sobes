import pdfplumber
from pdfrw import PdfReader
import json
import re




# for i in range(7, 29):
#     with pdfplumber.open('pasport_spr_oazis__endj8Y.pdf') as pdf:
#         first_page = pdf.pages[i]
#         data = first_page.extract_text()
#         with open('data.txt', 'a', encoding='utf-8') as file:
#             file.write(data)



with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read()
# print(len(data))


type_ = re.findall(r'(OC-\d{2}-\d{1}-\d{2})\s\d*\s*\d*\s*\d*\s*\d*\s*\d*\s*\D*\d*\S*\s*\d*,\d*\s*(\d{1},\d{3})', data)
# print(type_)

f = open('data1.txt', 'w')
for item in type_:
    s1 = str(item[0])
    s2 = str(item[-1])
    f.write(s1 + ' ' + s2 + '\n')




# print(type_)
# new_dict = {}
# for item in type_:
#     with open('data1.txt', 'a', encoding='utf-8') as file:
#         file.write(item[0], item[-1])



    
    # with open('data1.txt', 'a', encoding='utf-8') as file:
    #     file.write(new_list)









