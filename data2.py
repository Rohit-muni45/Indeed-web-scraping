# modules which need to imported
from bs4 import BeautifulSoup
import pandas as pd
import os

# function to parse the html files.

def extract_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup

# function to get the required data

def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')
    for item in divs:
        title = item.find('a').text.strip()
        link = 'https://www.indeed.co.in' + item.find('a')['href']
        company = item.find('span', class_='css-92r8pb eu4oa1w0').text.strip()
        location = item.find('div', class_='css-1p0sjhy eu4oa1w0').text
        try:
            salary = item.find('div', class_='css-1cvo3fd eu4oa1w0').text.strip()
        except:
            salary = 'Not mentioned'
       

        job = {
            'Role': title,
            'Company': company,
            'Location': location,
            'Salary': salary,
            'Link': link 
        }
        joblist.append(job)

joblist = []

# Directory where your index.html files are located

directory = 'html_files'

#This will read the html files path

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        file_path = os.path.join(directory, filename)
        print(f'Extracting data from {file_path}...')
        c = extract_from_file(file_path)
        transform(c)


df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv', index=False)

