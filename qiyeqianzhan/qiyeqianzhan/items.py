# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from scrapy import Item

class QiyeqianzhanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    compony_name=Field()
    compony_url=Field()
    compony_info=Field()
    id = Field()
    gsinfo_shxydm=Field()
    gsinfo_zch=Field()
    gsinfo_jgdm=Field()
    gsinfo_jyzt=Field()
    gsinfo_ztlx=Field()


