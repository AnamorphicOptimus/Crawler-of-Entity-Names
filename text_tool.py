# -*- coding: utf-8 -*-

import json

def get_page_num(page_info):
    """return page number of each list item"""
    if page_info == '':
        return 1
    return int((page_info.split('..')[1]).split('下一页')[0])


def get_page_url(index_url, page_index):
    """return each page url of a list item"""
    return index_url+'p'+str(page_index)


def get_li_detail(text):
    """return expected name and address"""
    spli_list = text.split('\n')
    name = spli_list[0]
    address = ''
    for spli in spli_list:
        if "地址:" in spli:
            address = spli.split("地址: ")[1].strip()
    return name, address


def crawl_to_file(crawl_data):
    """to save data in case of err"""
    with open(r'.\shanghaiPlacetest.json', 'w', encoding='utf-8') as file_obj:
        json.dump(crawl_data, file_obj, indent=4, ensure_ascii=False)
