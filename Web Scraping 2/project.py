from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table')
temp_list = []
table_rows = table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Name = []
Distance = []
Mass = []
Radius = []


for i in range(1, len(temp_list)):
    Name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Name, Distance, Mass, Radius,)), columns=[
                   'Star_name', 'Distance', 'Mass', 'Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')
