
from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from lxml import etree
import traceback
from text_tool import *


"""webdriver config"""
options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument('--proxy-server={0}'.format(proxy.proxy))
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
browser = webdriver.Chrome(chrome_options=options, executable_path=r'.\chromedriver.exe')

"""crawl list"""
url = 'http://life.city8090.com/shanghai/'
page_xpath = '//div[@class="page"]'
elements_xpath = '//div[@class="content_list01"]//ul//li[@class="width01"]'
crawl_list_en = ["dujiacun", "wenhuaguan", "yezonghui", "guangchang", "shangchang", "dianqishangchang", "gouwu",
                 "xiaoqu", "bieshu", "bangongdasha", "daoluming", "quxian", "shangquan", "xiangzhen"]
crawl_list_ch = ["度假村/度假区", "文化馆/活动中心", "夜总会/娱乐中心", "休闲广场", "购物中心", "电器商场", "超市", "小区", "别墅",
                 "办公大厦", "道路名称", "区县", "商圈", "乡镇"]
crawl_list_len = len(crawl_list_en)

"""crawl data"""
crawl_data = {}
err_data = {"index_page_num": [], "index_page": []}
try:
    for index in range(crawl_list_len):
        # dic init...
        index_url = url+crawl_list_en[index]+'/'
        crawl_dic = {crawl_list_ch[index]: []}

        # web refreshing...
        try:
            browser.get(index_url)
            WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, page_xpath)))
        except Exception as ex:
            print("### err in ", index, "log:", ex)
            err_data["index_page_num"].append(index)
            continue

        # get page number
        page_num_info = browser.find_element_by_xpath(page_xpath).text
        page_num = get_page_num(page_num_info)

        # pages in loop
        for page_index in range(1, page_num+1):
            page_url = get_page_url(index_url, page_index)

            # web refreshing...
            try:
                browser.get(page_url)
                WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, elements_xpath)))
            except Exception as ex:
                print("### err in ", index, "### err in page", page_index, "log:", ex)
                err_data["index_page"].append('-'.join((str(index), str(page_index))))
                continue

            # elements data collect
            elements = browser.find_elements_by_xpath(elements_xpath)
            for li in elements:
                detail = get_li_detail(li.text)
                li_detail = dict(name=detail[0], address=detail[1])
                crawl_dic[crawl_list_ch[index]].append(li_detail)
            print("--- finish in ", index, "--- finish in page", page_index)

        time.sleep(2)
        # finish one of the items
        crawl_data.update(crawl_dic)
except Exception as ex:
    crawl_to_file(crawl_data)
    print("log:", ex)
    traceback.print_exc()

"""save data with json"""
crawl_to_file(crawl_data)












