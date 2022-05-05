from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 1. Khai báo biến browser
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument('--incognito')
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

# 2. Mở một trang web
browser.get("https://www.facebook.com/")

# 2.1 Điền thông tin tài khoản vào ô tên đăng nhập
username = browser.find_element_by_id("email")
username.send_keys("sharicelong4932@gmail.com")

password = browser.find_element_by_id("pass")
password.send_keys("taukhongnho397")

# 2.2 Click vào nút đăng nhập
# password.submit()
password.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5s
sleep(20)

# 4. Đóng trình duyệt
browser.close()
