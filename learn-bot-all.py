# find element
driver.find_element_by_name("nama");
driver.find_element_by_id("nama")
driver.find_element_by_xpath("//input[@id='nama']")
driver.find_element_by_css_selector("input#nama")

# find element and find elements
# By.ID
# By.XPATH
# BY.LINK_TEXT
# PARTIAL_LINK_TEXT
# NAME
# TAH_NAME
# CLASS_NAME
# CSS_SELECTOR

driver.find_element(By.XPATH,'//button[text()="Submit"]')
driver.find_elements(By.XPATH,'//button')

# '/html/body/form[1]'
# "//form[1]"
# "//form[@id='loginForm']"

# "//form[input/@name='username']"
# "//form[@id='logitnForm]/input[1]"
# "//input[@name='username']"