from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
#menghapus isi
elem.clear();
#mengisi dengan 12345678
elem.send_keys("12345678")

# submit
elem.send_keys(Keys.ENTER);

print("Done");