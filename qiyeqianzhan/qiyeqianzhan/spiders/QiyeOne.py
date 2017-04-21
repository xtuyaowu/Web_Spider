# -*- coding: utf-8 -*-
import scrapy
from ..items import QiyeqianzhanItem
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Request
import time
class QiyeoneSpider(CrawlSpider):
    name = "QiyeOne"
    allowed_domains = ["qiye.qianzhan.com"]
    start_urls = ['http://qiye.qianzhan.com/search/all/支付']
    parent_url='http://qiye.qianzhan.com'
    i = 1
    # cookies = { 'Cookie': 'qznewsite.uid=toiuig450mrlasa5l4m45dfz; ASP.NET_SessionId=p3xviyxbeytnuy3zhcswzglf; Hm_lvt_048cbb2d27bb635e2aeb64403a58e3a3=1492592694,1492592884,1492594667; Hm_lpvt_048cbb2d27bb635e2aeb64403a58e3a3=1492676564; qz.newsite=455BF9B7F710709223ED59F2C526EE851B3FBC96DEF2474B5AE03F72A0341842B16CC08303E5B61BBDCC4AFFAFEEAEF92F6DF7DA5A2017C182EBE88023DB44CC3DE9D35A3BC04932990BD43EAC1528794ABF26E80F6C7F3EA924C112B1C6B0A80E6669E3267F65A8C2906379B1A06B5C4564C094B645CDDD67CB04739333BE4AF4BC3257E49806C3AC586E9B57D71B27DEB33A2613E487E2B1A5F74614479149CF29049D'}
    cookies = {'qznewsite.uid': 'toiuig450mrlasa5l4m45dfz',
                   'ASP.NET_SessionId': 'p3xviyxbeytnuy3zhcswzglf',
                   'Hm_lvt_048cbb2d27bb635e2aeb64403a58e3a3': ['1492592694', '1492592884', '1492594667'],
                   'Hm_lpvt_048cbb2d27bb635e2aeb64403a58e3a3': ['1492676564'],
                   'qz.newsite': '455BF9B7F710709223ED59F2C526EE851B3FBC96DEF2474B5AE03F72A0341842B16CC08303E5B61BBDCC4AFFAFEEAEF92F6DF7DA5A2017C182EBE88023DB44CC3DE9D35A3BC04932990BD43EAC1528794ABF26E80F6C7F3EA924C112B1C6B0A80E6669E3267F65A8C2906379B1A06B5C4564C094B645CDDD67CB04739333BE4AF4BC3257E49806C3AC586E9B57D71B27DEB33A2613E487E2B1A5F74614479149CF29049D'}
    cookies2={'qznewsite.uid':'toiuig450mrlasa5l4m45dfz',
 'qz.newsite':'0AA0F7F64C35F3C59972E8937E3493F1103584B195E21858D7F257FB8C133F897CDBF4B75E005DEE1238A239A31B7E92A61A8B07DEFE43C72C41257FB2C3623719D5DFBAC2219363DE322E40E3CAA6F906EBCCD531CBA751FDEEE1DF660C6BD6F72D00C6F73C6F22AFAFEC5A2FF591608FEE96E40579288F3AAA8B8893CEB86EBD441AAE1A420FDEB7B7DD9F610ACDECB220F9EF43BD942C27FA794F1D0C72622A977126',
 'Hm_lvt_048cbb2d27bb635e2aeb64403a58e3a3':['1492592694','1492592884','1492594667','1492681298'],
 'Hm_lpvt_048cbb2d27bb635e2aeb64403a58e3a3':'1492681336'}

    cookies3={'qznewsite.uid':'toiuig450mrlasa5l4m45dfz',
'qz.newsite':'0AA0F7F64C35F3C59972E8937E3493F1103584B195E21858D7F257FB8C133F897CDBF4B75E005DEE1238A239A31B7E92A61A8B07DEFE43C72C41257FB2C3623719D5DFBAC2219363DE322E40E3CAA6F906EBCCD531CBA751FDEEE1DF660C6BD6F72D00C6F73C6F22AFAFEC5A2FF591608FEE96E40579288F3AAA8B8893CEB86EBD441AAE1A420FDEB7B7DD9F610ACDECB220F9EF43BD942C27FA794F1D0C72622A977126',
'Hm_lvt_048cbb2d27bb635e2aeb64403a58e3a3':['1492741808','1492741873','1492741883','1492742610'],
'Hm_lpvt_048cbb2d27bb635e2aeb64403a58e3a3':'1492742633'}



    def start_requests(self):
        return [Request("http://qiye.qianzhan.com/search/all/支付", cookies=self.cookies, callback=self.parse)]

    def parse(self, response):
        company_selector = Selector(response)
        company_iterator=company_selector.xpath(r'//ul[@class="list-search"]/li')
        for eachcompany in company_iterator:
            companyitem=QiyeqianzhanItem()
            compony_name_1 = eachcompany.xpath(r'div[@class="tit"]/a/text()[1]').extract()
            compony_name_2=eachcompany.xpath(r'div[@class="tit"]/a/em/text()').extract()
            compony_name_3=eachcompany.xpath(r'div[@class="tit"]/a/text()[2]').extract()
            compony_url = eachcompany.xpath(r'div[@class="tit"]/a/@href').extract()
            if compony_name_1:
                if compony_name_2:
                    if compony_name_3:
                        companyitem['compony_name'] = compony_name_1[0].strip()+compony_name_2[0].strip()+compony_name_3[0].strip()
                    else:
                        companyitem['compony_name'] = compony_name_1[0].strip() + compony_name_2[0].strip()
                else:
                    companyitem['compony_name'] = compony_name_1[0].strip()
            else:
                if compony_name_2:
                    if compony_name_3:
                        companyitem['compony_name'] = compony_name_2[0].strip()+compony_name_3[0].strip()
                    else:
                        companyitem['compony_name'] = compony_name_2[0].strip()

            if compony_url:
                companyitem['compony_url'] = self.parent_url + compony_url[0].strip()
            companyitem["id"]=str(self.i)
            self.i+=1
            # yield companyitem
            #测试内容网址
            print(self.parent_url + compony_url[0].strip())
            time.sleep(2)
            yield Request(self.parent_url + compony_url[0].strip(), meta={"item": companyitem},
                          callback=self.parse_article_content,cookies=self.cookies2)


        #nextlink = response.xpath(r'//div[@class="page-list"]/a[contains(text(),"下一页")]/@href').extract()
        nextlink = response.xpath(r'//div[@class="page-list"]/a[@class="next"]/@href').extract()

        if nextlink:
            Nextlink = nextlink[0].strip()
            request = Request(self.parent_url + Nextlink, callback=self.parse,cookies=self.cookies)
            time.sleep(2)
            yield request
        else:
            print('下一页链接为空')

    def parse_article_content(self, response):
        companyitem = response.meta['item']

        gsinfo_shxydm = response.xpath(r'//ul[@class="art-basic"]/li[1]/span[2]/text()').extract()
        if gsinfo_shxydm:
            companyitem['gsinfo_shxydm'] = gsinfo_shxydm[0].strip()
        else:
            companyitem['gsinfo_shxydm']='NaN'

        gsinfo_zch = response.xpath(r'//ul[@class="art-basic"]/li[2]/span[2]/text()').extract()
        if gsinfo_zch:
            companyitem['gsinfo_zch'] = gsinfo_zch[0].strip()
        else:
            companyitem['gsinfo_zch']='NaN'

        gsinfo_jgdm = response.xpath(r'//ul[@class="art-basic"]/li[4]/span[2]/text()').extract()
        if gsinfo_jgdm:
            companyitem['gsinfo_jgdm'] = gsinfo_jgdm[0].strip()
        else:
            companyitem['gsinfo_jgdm']='NaN'

        gsinfo_jyzt = response.xpath(r'//ul[@class="art-basic"]/li[5]/span[2]/text()').extract()
        if gsinfo_jyzt:
            companyitem['gsinfo_jyzt'] = gsinfo_jyzt[0].strip()
        else:
            companyitem['gsinfo_jyzt']='NaN'

        gsinfo_ztlx = response.xpath(r'//ul[@class="art-basic"]/li[6]/span[2]/text()').extract()
        if gsinfo_ztlx:
            companyitem['gsinfo_ztlx'] = gsinfo_ztlx[0].strip()
        else:
            companyitem['gsinfo_ztlx']='NaN'

        gsinfo_jglx = response.xpath(r'//ul[@class="art-basic"]/li[7]/span[2]/text()').extract()
        if gsinfo_jglx:
            companyitem['gsinfo_jglx'] = gsinfo_jglx[0].strip()
        else:
            companyitem['gsinfo_jglx'] = 'NaN'

        gsinfo_djrq = response.xpath(r'//ul[@class="art-basic"]/li[8]/span[2]/text()').extract()
        if gsinfo_djrq:
            companyitem['gsinfo_djrq'] = gsinfo_djrq[0].strip()
        else:
            companyitem['gsinfo_djrq']='NaN'

        gsinfo_frdb = response.xpath(r'//ul[@class="art-basic"]/li[9]/span[2]/text()').extract()
        if gsinfo_frdb:
            companyitem['gsinfo_frdb'] = gsinfo_frdb[0].strip()
        else:
            companyitem['gsinfo_frdb']='NaN'

        gsinfo_zczb = response.xpath(r'//ul[@class="art-basic"]/li[10]/span[2]/text()').extract()
        if gsinfo_zczb:
            companyitem['gsinfo_zczb'] = gsinfo_zczb[0].strip()
        else:
            companyitem['gsinfo_zczb']='NaN'

        gsinfo_jyxq = response.xpath(r'//ul[@class="art-basic"]/li[11]/span[2]/text()').extract()
        if gsinfo_jyxq:
            companyitem['gsinfo_jyxq'] = gsinfo_jyxq[0].strip()
        else:
            companyitem['gsinfo_jyxq']='NaN'

        gsinfo_djjg = response.xpath(r'//ul[@class="art-basic"]/li[12]/span[2]/text()').extract()
        if gsinfo_djjg:
            companyitem['gsinfo_djjg'] = gsinfo_djjg[0].strip()
        else:
            companyitem['gsinfo_djjg']='NaN'

        gsinfo_ssdq = response.xpath(r'//ul[@class="art-basic"]/li[13]/span[2]/text()').extract()
        if gsinfo_ssdq:
            companyitem['gsinfo_ssdq'] = gsinfo_ssdq[0].strip()
        else:
            companyitem['gsinfo_ssdq']='NaN'

        gsinfo_zsyxq = response.xpath(r'//ul[@class="art-basic"]/li[14]/span[2]/text()').extract()
        if gsinfo_zsyxq:
            companyitem['gsinfo_zsyxq'] = gsinfo_zsyxq[0].strip()
        else:
            companyitem['gsinfo_zsyxq']='NaN'

        gsinfo_fzrq = response.xpath(r'//ul[@class="art-basic"]/li[15]/span[2]/text()').extract()
        if gsinfo_fzrq:
            companyitem['gsinfo_fzrq'] = gsinfo_fzrq[0].strip()
        else:
            companyitem['gsinfo_fzrq']='NaN'

        gsinfo_qzbq = response.xpath(r'//ul[@class="art-basic"]/li[16]/span[2]/a/text()').extract()
        if gsinfo_qzbq:
            companyitem['gsinfo_qzbq'] = ":".join(gsinfo_qzbq)
        else:
            companyitem['gsinfo_qzbq']='NaN'

        gsinfo_zhbq = response.xpath(r'//ul[@class="art-basic"]/li[17]/span[2]/a/text()').extract()
        if gsinfo_zhbq:
            companyitem['gsinfo_zhbq'] = ":".join(gsinfo_zhbq)
        else:
            companyitem['gsinfo_zhbq']='NaN'

        gsinfo_sshy = response.xpath(r'//ul[@class="art-basic"]/li[18]/span[2]/a/text()').extract()
        if gsinfo_sshy:
            companyitem['gsinfo_sshy'] = ":".join(gsinfo_sshy)
        else:
            companyitem['gsinfo_sshy']='NaN'


        compony_adress = response.xpath(r'//ul[@class="art-basic"]/li[19]/span[2]/text()').extract()
        if compony_adress:
            companyitem['compony_adress'] = compony_adress[0].strip()
        else:
            companyitem['compony_adress']='NaN'

        gsinfo_jyfw = response.xpath(r'//ul[@class="art-basic"]/li[20]/span[2]/text()').extract()
        if gsinfo_jyfw:
            companyitem['gsinfo_jyfw'] = gsinfo_jyfw[0].strip()
        else:
            companyitem['gsinfo_jyfw']='NaN'

        #爬取测试
        htmlname = response.xpath(r'//html/head/title').extract()
        print(response,htmlname)
        return companyitem
