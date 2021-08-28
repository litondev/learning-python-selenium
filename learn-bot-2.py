from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe");

driver.get("http://localhost/selenium/index.php")

print("Start")

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# famre_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# stateness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

try:
	element = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.ID,"testing-id"))
	) 

	# do something with element
	
	print("Done")
except TimeoutException as err:
	print("Element tidak ditemukan")
except Expception as err:
	print("Something Wrong")