from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# use chrome to access web
driver = webdriver.Chrome()

# open site
driver.get('https://myview.pptparkview.com/')

# wait for page to fully load
driver.implicitly_wait(60)

# select id box and input username
driver.find_element_by_xpath("//input[@ng-model='login.model.username']").send_keys('jdinh')

# find password box and input password
driver.find_element_by_xpath("//input[@ng-model='login.model.password']").send_keys('Cyb3rM4k')

# find login button and click
driver.find_element_by_class_name('btn').click()

# find menu button and wait until button is clickable
wait = WebDriverWait(driver, 60)
wait.until(EC.element_to_be_clickable((By.ID, 'header-menu-toggle'))).click()

# find configuration tab and click
wait.until(EC.element_to_be_clickable((By.ID, 'configuration'))).click()

# find managed devices tab and click
wait.until(EC.element_to_be_clickable((By.ID, 'configuration-servers'))).click()

# find agent to update
count = 6
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'jqx-tree-grid-expand-button jqx-grid-group-expand jqx-icon-arrow-down'))).click()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'jqx-tree-grid-collapse-button jqx-grid-group-collapse jqx-icon-arrow-right'))).click()
while count < 208:
    wait.until(EC.element_to_be_clickable((By.ID, 'eventGrpTreeGridMenuButton' + str(count)))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'event_action_deployInstall'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'HardwareKM10201_ConLib18_WIN'))).click()
    wait.until(EC.element_to_be_clickable((By.ID, 'kmDeploy'))).click()