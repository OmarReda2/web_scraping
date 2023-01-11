import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

main_url = 'https://www.drugs.com'
def req_page(url):
    html_text = requests.get(f'{main_url}{url}').text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup
    

## extract url
my_page = req_page('/condition/a.html') 
A = my_page.find('ul', class_='ddc-list-column-2')
diseases = A.findAll('li')


# A_disease = np.array([][])

data = pd.DataFrame()

for disease in diseases:
    
    disease_name = disease.find('a').text
    drug_url = disease.find('a').get('href')


    ## extract info
    drugs_list = []
    drugs = req_page(drug_url)
    all_page = drugs.find('li', class_='ddc-paging-show-all')
    if(all_page):
        all_page = all_page.find('a').get('href')
        drugs = req_page(all_page)

    drugs_table = drugs.find('table', class_='ddc-table-secondary ddc-table-sortable condition-table')
    drugs_name = drugs_table.findAll('tr', class_='condition-table__summary')
    drugs_generic = drugs_table.findAll('p', class_='condition-table__generic-name' )
    drugs_rate =  drugs_table.findAll('td', class_='condition-table__rating')



    for i in range(len(drugs_name)):
            drug_info = []
            name = drugs_name[i].find('a', class_='condition-table__drug-name__link ddc-text-wordbreak').text

            rate = drugs_rate[i].text.replace('\n', '').replace('\t','')
            if rate != 'Rate':
                name = f'{name} - {rate}' 

            generic = drugs_generic[i].text.replace('Generic name:', '').replace('\t', '').replace('\n', '').replace('\xa0', '')

            drug_info.append(name)    
            drug_info.append(generic)    
            drugs_list.append(drug_info)

    # A_drugs = {disease_name: drugs_list}
    # df = pd.DataFrame(A_drugs)
    # data = data.append(df)







# df_array = df.transpose()
# df_array_df = pd.DataFrame(df_array)
# print(df_array_df)














