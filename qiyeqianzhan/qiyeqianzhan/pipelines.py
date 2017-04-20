# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlsxwriter
from openpyxl import load_workbook

class QiyeqianzhanPipeline(object):
    def __init__(self):
        workbook = xlsxwriter.Workbook(r'huizong.xlsx')
        worksheet = workbook.add_worksheet(r'pay_company')
        workbook.close()

    def process_item(self, item, spider):
        file = open(r'companylist.txt', mode='a',
                    encoding='utf8')
        if item['compony_name']:
            file.writelines(item['compony_name']+"\n")
        else:
            file.writelines("抓取失败")
        if item['compony_url']:
            file.writelines(item['compony_url']+"\n")
        else:
            file.writelines("抓取失败")
        file.close()

        # print(item['compony_name'].strip(), "抓取成功")
        wb = load_workbook(r'huizong.xlsx')
        ws = wb.get_sheet_by_name(r'pay_company')
        col1 = 'A' + item['id']
        col2 = 'B' + item['id']
        col3 = 'C' + item['id']
        col4 = 'D' + item['id']
        col5 = 'E' + item['id']
        col6 = 'F' + item['id']
        ws[col1] = item['compony_name']
        ws[col2] = item['gsinfo_shxydm']
        ws[col3] = item['gsinfo_zch']
        ws[col4] = item['gsinfo_jgdm']
        ws[col5] = item['gsinfo_jyzt']
        ws[col6] = item['gsinfo_ztlx']
        wb.save(r'huizong.xlsx')
        print("写入成功")

        return item
