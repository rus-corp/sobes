import pdfplumber
from pdfrw import PdfReader
import json
import re



# new_dict = {}
# for i in range(15, 22):
#     with pdfplumber.open('pasport_spr_oazis__endj8Y.pdf') as pdf:
#         first_page = pdf.pages[i]
#         data = first_page.extract_text()
#         with open('data.txt', 'a', encoding='utf-8') as file:
#             file.write(data)



with open('data.txt', 'r', encoding='utf-8') as file:
    data = file.read()
new_list = []
type = re.findall(r'(OC-\d*-\d-\d*).*(\d{2},\d{1})\s(\d{1},\d{3})', data)
for item in type:
    new_list.append(item[0])
    new_list.append(item[-1])
    
    with open('data1.txt', 'a', encoding='utf-8') as file:
        file.write(new_list)





# (OC-\d*-\d-\d*).*(\d{2},\d{1})\s(\d{1},\d{3})



