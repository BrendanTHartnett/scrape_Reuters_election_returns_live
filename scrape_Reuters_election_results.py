#!/usr/bin/env python
# coding: utf-8


# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


#### SENATE ######
# Create an URL object
url = 'https://www.reuters.com/graphics/USA-ELECTION/RESULTS/dwvkdgzdqpm/'
# Create object page
page = requests.get(url)



# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
soup


solid_dem_table = soup.find('table', class_='table-results solid-dem svelte-2c3yut')
print(solid_dem_table)


headers_solid_dem = []
for i in solid_dem_table.find_all("th"):
 title = i.text
 headers_solid_dem.append(title)


solid_dem_dat = pd.DataFrame(columns = headers_solid_dem)



solid_dem_dat.drop('Solid Democratic', axis=1, inplace=True)
solid_dem_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)



for j in solid_dem_table.find_all("tr")[2:7]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(solid_dem_dat)
 solid_dem_dat.loc[length] = row



solid_dem_dat



solid_rep_table = soup.find('table', class_='table-results solid-rep svelte-2c3yut')
print(solid_rep_table)



headers_solid_rep = []
for i in solid_rep_table.find_all("th"):
 title = i.text
 headers_solid_rep.append(title)



solid_rep_dat = pd.DataFrame(columns = headers_solid_rep)



solid_rep_dat.drop('Solid Republican', axis=1, inplace=True)
solid_rep_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)



for j in solid_rep_table.find_all("tr")[2:16]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(solid_rep_dat)
 solid_rep_dat.loc[length] = row



lean_dem_table = soup.find('table', class_='table-results lean-dem svelte-2c3yut')
print(lean_dem_table)



headers_lean_dem = []
for i in lean_dem_table.find_all("th"):
 title = i.text
 headers_lean_dem.append(title)



lean_dem_dat = pd.DataFrame(columns = headers_lean_dem)



lean_dem_dat.drop('Lean Democratic', axis=1, inplace=True)
lean_dem_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)



for j in lean_dem_table.find_all("tr")[2:4]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(lean_dem_dat)
 lean_dem_dat.loc[length] = row




lean_dem_dat



lean_rep_table = soup.find('table', class_='table-results lean-rep svelte-2c3yut')
print(lean_rep_table)



headers_lean_rep = []
for i in lean_rep_table.find_all("th"):
 title = i.text
 headers_lean_rep.append(title)



lean_rep_dat = pd.DataFrame(columns = headers_lean_rep)




lean_rep_dat.drop('Lean Republican', axis=1, inplace=True)
lean_rep_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)



for j in lean_rep_table.find_all("tr")[2:5]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(lean_rep_dat)
 lean_rep_dat.loc[length] = row



lean_rep_dat



toss_up_table = soup.find('table', class_='table-results tossup svelte-2c3yut')
print(toss_up_table)




headers_toss_up = []
for i in toss_up_table.find_all("th"):
 title = i.text
 headers_toss_up.append(title)



toss_up_dat = pd.DataFrame(columns = headers_toss_up)



toss_up_dat.drop('Competitive', axis=1, inplace=True)
toss_up_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)


for j in toss_up_table.find_all("tr")[2:10]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(toss_up_dat)
 toss_up_dat.loc[length] = row



dataframes = [solid_dem_dat, lean_dem_dat, toss_up_dat, lean_rep_dat, solid_rep_dat]
merged_senate = pd.concat(dataframes, ignore_index=True)



merged_senate['State'] = merged_senate['state_scrape'].str.partition('\n')[0]


merged_senate['dem_vote_percent'] = merged_senate['dem_scrape'].map(lambda x: x.lstrip('Democrats:\n ').rstrip('%'))


merged_senate['rep_vote_percent'] = merged_senate['rep_scrape'].map(lambda x: x.lstrip('Republicans:\n ').rstrip('%'))


merged_senate['percent_vote_in'] = merged_senate['percent_in_scrape'].map(lambda x: x.lstrip('Share of expected votes counted:\n ').rstrip('%'))


merged_senate['office'] = 'Senate'


Senate_Results = merged_senate.filter(['State', 'dem_vote_percent', 'rep_vote_percent', 'percent_vote_in', 'office'])

Senate_Results


from selenium import webdriver



url = "https://www.reuters.com/graphics/USA-ELECTION/RESULTS/dwvkdgzdqpm/"

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

browser = webdriver.Chrome()

# Get button and click it
python_button = driver.find_element('xpath', '//*[@id="elex-main-page"]/div/div[7]/div[1]/div[1]/button[3]')
python_button.click() #click load more button

# Pass to BS4
soup=BeautifulSoup(driver.page_source)



solid_dem_table = soup.find('table', class_='table-results solid-dem svelte-2c3yut')
print(solid_dem_table)



headers_solid_dem = []
for i in solid_dem_table.find_all("th"):
 title = i.text
 headers_solid_dem.append(title)


solid_dem_dat = pd.DataFrame(columns = headers_solid_dem)



solid_dem_dat.drop('Solid Democratic', axis=1, inplace=True)
solid_dem_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)



for j in solid_dem_table.find_all("tr")[2:6]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(solid_dem_dat)
 solid_dem_dat.loc[length] = row



solid_rep_table = soup.find('table', class_='table-results solid-rep svelte-2c3yut')
print(solid_rep_table)



headers_solid_rep = []
for i in solid_rep_table.find_all("th"):
 title = i.text
 headers_solid_rep.append(title)



solid_rep_dat = pd.DataFrame(columns = headers_solid_rep)


solid_rep_dat.drop('Solid Republican', axis=1, inplace=True)
solid_rep_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)


for j in solid_rep_table.find_all("tr")[2:14]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(solid_rep_dat)
 solid_rep_dat.loc[length] = row



lean_dem_table = soup.find('table', class_='table-results lean-dem svelte-2c3yut')
print(lean_dem_table)



headers_lean_dem = []
for i in lean_dem_table.find_all("th"):
 title = i.text
 headers_lean_dem.append(title)



lean_dem_dat = pd.DataFrame(columns = headers_lean_dem)



lean_dem_dat.drop('Lean Democratic', axis=1, inplace=True)
lean_dem_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)



for j in lean_dem_table.find_all("tr")[2:10]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(lean_dem_dat)
 lean_dem_dat.loc[length] = row


lean_rep_table = soup.find('table', class_='table-results lean-rep svelte-2c3yut')
print(lean_rep_table)



headers_lean_rep = []
for i in lean_rep_table.find_all("th"):
 title = i.text
 headers_lean_rep.append(title)



lean_rep_dat = pd.DataFrame(columns = headers_lean_rep)



lean_rep_dat.drop('Lean Republican', axis=1, inplace=True)
lean_rep_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)


for j in lean_rep_table.find_all("tr")[2:7]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(lean_rep_dat)
 lean_rep_dat.loc[length] = row


toss_up_table = soup.find('table', class_='table-results tossup svelte-2c3yut')
print(toss_up_table)


headers_toss_up = []
for i in toss_up_table.find_all("th"):
 title = i.text
 headers_toss_up.append(title)


toss_up_dat = pd.DataFrame(columns = headers_toss_up)



toss_up_dat.drop('Competitive', axis=1, inplace=True)
toss_up_dat.rename(columns={'': 'state_scrape', 'Dem': 'dem_scrape', 'Rep': 'rep_scrape', '% Exp.': "percent_in_scrape"}, inplace=True)




for j in toss_up_table.find_all("tr")[2:9]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(toss_up_dat)
 toss_up_dat.loc[length] = row


dataframes = [solid_dem_dat, lean_dem_dat, toss_up_dat, lean_rep_dat, solid_rep_dat]
merged_governors = pd.concat(dataframes, ignore_index=True)


merged_governors['state'] = merged_governors['state_scrape'].str.partition('\n')[0]
merged_governors['State'] = merged_governors['state'].str.split(' ', 1).str[0]



merged_governors['dem_vote_percent'] = merged_governors['dem_scrape'].map(lambda x: x.lstrip('Democrats:\n ').rstrip('%')


merged_governors['rep_vote_percent'] = merged_governors['rep_scrape'].map(lambda x: x.lstrip('Republicans:\n ').rstrip('%'))


merged_governors['percent_vote_in'] = merged_governors['percent_in_scrape'].map(lambda x: x.lstrip('Share of expected votes counted:\n ').rstrip('%'))


merged_governors['office'] = 'Governor'



Governors_Results = merged_governors.filter(['State', 'dem_vote_percent', 'rep_vote_percent', 'percent_vote_in', 'office'])


Governors_Results
Governors_Results.to_csv("Governors_Results_Reuters.csv")


Governors_Results


# Combine Senate and Governors results  ####

dataframes = [Senate_Results, Governors_Results]
Reuters_Election_Results = pd.concat(dataframes, ignore_index=True)
Reuters_Election_Results.to_csv("Reuters_Election_Results.csv")

