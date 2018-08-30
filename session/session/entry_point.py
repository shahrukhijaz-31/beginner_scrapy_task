from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'session_spider', '-o', 'session_spider.json'])
