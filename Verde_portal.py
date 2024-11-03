from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# set webdriver path here it may vary
# browser = webdriver.Chrome("F:/C Programming/Python/chromedriver.exe")

website_URL = "https://app.verdemobility.com/"
driver.get(website_URL)
driver.maximize_window()

time.sleep(2)
login = driver.find_element(By.TAG_NAME, "INPUT")
login.send_keys("nirav.prajapati@slscorp.com")

time.sleep(2)
put_log = driver.find_element(By.XPATH, "/html/body/app-root/auth/app-login/div/div/div/div[2]/form/input[2]")
put_log.send_keys("Nirav@1307")
time.sleep(1)

driver.find_element(By.TAG_NAME, "BUTTON").click()
time.sleep(1)

# time.sleep(4)
# h = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu-title')))
menu_title_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-pages/div/app-sidebar/nav/div/div[2]/div/a/span')))
menu_title_element.click()

time.sleep(2)

sub_menu_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-pages/div/app-sidebar/nav/div/div[2]/div/li/ul/li[5]/a/span')))
sub_menu_element.click()

time.sleep(4)

filtered_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-pages/div/section/app-charging-point/p-tabview/div/div[2]/div/div/p-table/div/div[2]/table/thead/tr/th[2]/div/p-columnfilter/div/button/span")))
filtered_page.click()

time.sleep(2)
find_page = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/p-columnfilterformelement/input")
find_page.send_keys("Cube Office Test Charger")
# find_page.send_keys("System Level Solutions Office")
# find_page.send_keys("Park Plaza CBD")

time.sleep(2)

submit = driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]")
submit.click()

time.sleep(5)

selection = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-pages/div/section/app-charging-point/p-tabview/div/div[2]/div/div/p-table/div/div[2]/table/tbody/tr[1]/td[2]/a")))
selection.click()

time.sleep(2)

state_selection = driver.find_element(By.XPATH, "/html/body/app-root/app-pages/div/section/app-view-charging-point/div[2]/div[1]/div/div/div[2]/div[1]/p[1]/a")
state_selection.click()

time.sleep(3)

transaction_selection = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-pages/div/section/app-view-evse/div[3]/div/div[2]/p-dropdown/div/div[2]/span")))
transaction_selection.click()

time.sleep(2)
start_transaction = driver.find_element(By.XPATH, "/html/body/div/div/div/div/ul/p-dropdownitem[1]/li/span")
start_transaction.click()

time.sleep(2)

play = driver.find_element(By.XPATH, "/html/body/app-root/app-pages/div/section/app-view-evse/div[3]/div/div[2]/button/i")
play.click()

time.sleep(2)

Id_s = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[1]/td[2]/p-dropdown/div/span")
Id_s.click()

time.sleep(2)

Id = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[1]/td[2]/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input")))
Id.send_keys("Mayank Panchal")

time.sleep(2)
Id_sd = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[1]/td[2]/p-dropdown/div/p-overlay/div/div/div/div[2]/ul/p-dropdownitem/li/span")))
Id_sd.click()
time.sleep(2)

charging_option = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[2]/td[2]/p-selectbutton/div/div[1]/span")
charging_option.click()
time.sleep(2)

kwh = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[3]/td[2]/input")
kwh.clear()
time.sleep(2)

kwh.send_keys("1")
time.sleep(2)

reason = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[4]/td[2]/input")
reason.send_keys("Testing Purpose")

time.sleep(2)

run_button = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-start-session/div/div/form/table/tbody/tr[5]/td/div/input[1]")
run_button.click()

time.sleep(2)
