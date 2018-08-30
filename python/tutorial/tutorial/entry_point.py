from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'umt', '-o', 'contact_info.json'])
#execute(['scrapy', 'crawl', 'umt_scraper'])
# execute(['scrapy', 'shell', 'https://www.sheego.de/'])