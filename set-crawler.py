from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

driver.get('https://www.cs.cmu.edu/~mleone/gdead/72.html')

a_elements = driver.find_elements(By.TAG_NAME, 'a')

csv_data = []
headers = []

for a in a_elements:

    a.click()
    
    time.sleep(2) 
    
    page_text = driver.find_element(By.TAG_NAME, 'body').text
    
    lines = page_text.splitlines()
    
    if lines:
        header = lines[0]
        headers.append(header)
        
        while len(csv_data) < len(lines) - 1:
            csv_data.append([''] * len(headers))
        
        for index, line in enumerate(lines[1:], start=0):
            if index >= len(csv_data):
                csv_data.append([''] * len(headers))
            if len(csv_data[index]) < len(headers):
                csv_data[index].extend([''] * (len(headers) - len(csv_data[index])))
            csv_data[index][len(headers) - 1] = line
    
    driver.back()
    
    time.sleep(2)

with open('song_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(headers)
    

    writer.writerows(csv_data)

driver.quit()
