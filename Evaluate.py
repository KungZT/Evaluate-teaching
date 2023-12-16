from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
driver.get('https://cas.kmust.edu.cn/lyuapServer/login?service=http%3A%2F%2Fjwctsp.kmust.edu.cn%2Fintegration%2Fkcas-sso%2Flogin')
usr = driver.find_element(By.ID,"username")
pwd = driver.find_element(By.ID,"password")
usr.send_keys('0000000000')
pwd.send_keys('0000000000')
submit = driver.find_element(By.NAME,'login').click()
time.sleep(3000)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div[9]/div[2]/div/div").click() 
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.current_window_handle
time.sleep(1)
item = driver.find_elements(By.CLASS_NAME,'el-link--inner')
#for i in range(len(item)):
while(1):
    item = driver.find_elements(By.CLASS_NAME,'el-link--inner')
    item[0].click()
    time.sleep(2)
    count2 = driver.find_elements(By.XPATH,"//input[@class='el-radio__original' and @value='A']/..")
    for i in count2:
        i.click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div/section/div/div[2]/div/div/div/div[2]/button[1]/span").click()
    time.sleep(3)