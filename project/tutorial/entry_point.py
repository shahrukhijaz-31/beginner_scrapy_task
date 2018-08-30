import scrapy


from scrapy.cmdline import execute

#execute(['scrapy', 'crawl', 'webScrap', '-o', 'file.json'])
execute(['scrapy', 'shell', 'https://www.sheego.de/adidas-performance-laufschuh-duramo-8-w-_126898.html?color=00919'])
