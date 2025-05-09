# -*- coding: utf-8 -*-
"""
pip install selenium webdriver_manager
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import pandas as pd
        
#%% 靜宜大學公告總覽
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
    options=options
)

# 啟動瀏覽器 & 最大化視窗
driver.get("https://www.pu.edu.tw/p/422-1000-1011.php?Lang=zh-tw")
driver.maximize_window()

# 模擬滾動頁面 2 次，以載入更多公告內容
for _ in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) # 等待 2 秒

# 存放所有資料的列表
data_list = []


# 選取所有公告標題的 a 元素
titles = driver.find_elements(By.CSS_SELECTOR, ".mtitle a")

for t in titles:
    title = t.text
    link = t.get_attribute("href")
    data_list.append({"公告": title, "網址": link})
    print(title) # 顯示公告標題
    print(link) # 顯示該公告的網址
    
driver.quit()

#%%
# 轉為 DataFrame 並輸出成 CSV
df = pd.DataFrame(data_list)
df.to_csv(r"PU.csv", index=False, encoding="utf-8-sig")






