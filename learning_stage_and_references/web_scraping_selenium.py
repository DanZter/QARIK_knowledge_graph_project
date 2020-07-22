from selenium import webdriver
PATH = r'C:/Program Files (x86)/chromedriver.exe'

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("http://aims.niassembly.gov.uk/officialreport/reports.aspx")

driver.quit()