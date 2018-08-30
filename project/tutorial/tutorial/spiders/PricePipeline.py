from scrapy.exceptions import DropItem
class PricePipeline(object):
   vat = 2.25

   def process_item(self, item, spider):
      if item['price']:
         if item['excludes_vat']:
            item['price'] = item['price'] * self.vat
            return item
         else:
            raise DropItem("Missing price in %s" % item)