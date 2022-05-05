from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 1. Khai báo browser
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument('--incognito')
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# 2. Mở URL
browser.get("https://www.facebook.com/groups/miaigroup/permalink/730028114435130/")
sleep(7)

# 3. Lấy link hiện comment
# showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
# showcomment_link.click()
# sleep(5)

# 4. Lấy comment
showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]/span/span")
showmore_link.click()
sleep(5)
# sleep(random.randint(5,10))

# showmore_link.click()
# sleep(5)

# 5. Tìm tất cả các comment và ghi ra màn hình (hoặc file)
# -> lấy all thẻ div có thuộc tính aria-label='Bình luận'
filetext = open("comment.txt", "w+", encoding="utf-8")
comment_list = browser.find_elements_by_xpath('//div[@role="article"]')

# Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
for comment in comment_list:
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
    poster = comment.find_element_by_class_name("_6cuy")
    # content = comment.find_element_by_class_name("ecm0bbzt e5nlhep0 a8c37x1j")
    # print("*", poster.text,":", content.text)
    print(poster.text)
    filetext.write(poster.text + "\n")
    print("--------------------")
    filetext.write("--------------------" + "\n")

sleep(5)

# 6. Đóng browser
browser.close()