from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe");

driver.get("http://localhost/selenium/index.php")

print("Start")

# mencari attribute name="nama"
elem = driver.find_element_by_name("nama");
# menghapus isi
elem.clear();
# mengisi dengan Testing
elem.send_keys('Testing');

# mencari attribute name="password"
elem = driver.find_element_by_name("password");
# menghapus isi
elem.clear();
# mengisi dengan 12345678
elem.send_keys("12345678")

# mencari attribute name="gender" di tag select
select = Select(driver.find_element_by_name('gender'))
# menselect nilai
select.select_by_value('female');

# mecari attribute input[type=checkbox] dan value Sleep
checkboxSleep = driver.find_element_by_xpath("//input[@type='checkbox'][@value='Sleep']")
checkboxSleep.click()


# submit
elem.send_keys(Keys.ENTER);


# NAMA
elementNama = WebDriverWait(driver,10).until(
	EC.presence_of_element_located((By.ID,"nama"))
) 

print("Nama Text : " + elementNama.text)
print("Nama Value : " + elementNama.get_attribute('value'))

driver.execute_script('arguments[0].innerText = "Hello"',elementNama)
driver.execute_script('arguments[0].setAttribute("value","Hello-Value")',elementNama)


# HOBBY
elementHobby = WebDriverWait(driver,10).until(
	EC.presence_of_element_located((By.ID,"hobby"))
)
elementHobbyChild = elementHobby.find_elements_by_tag_name("li");

for item in elementHobbyChild:
	print("Hobby Child : "+item.text)

print("Done");