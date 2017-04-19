from scrapy import cmdline
cmdline.execute("scrapy startproject qiyeqianzhan".split())
cmdline.execute("cd qiyeqianzhan".split())
cmdline.execute("scrapy genspider QiyeOne qiye.qianzhan.com/".split())
