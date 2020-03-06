from scrapy.spiders import CrawlSpider
from scrapy_app.items import ScrapyAppItem


class MzSpider(CrawlSpider):
    name = 'spider'
    # start_urls = ['http://www.lolmz.com/hot.php']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        # news = response.xpath('//div[@class="chroma-gallery mygallery"]//img')
        # /html/body/div[1]/div[1]
        news = response.xpath('//*[@id="news_body"]')
        print(news)
        for n in news:
            print(n)
            print("ggg")
        # for img in news:
        #     title = img.xpath('@alt').extract_first()
        #     img_url = img.xpath('@src').extract_first()
        #     item = ScrapyAppItem()
        #     item['title'] = title
        #     item['image_url'] = img_url
        #     yield item


        # for n in news:
        #     title = n.xpath('@h3').extract_first()
        #     link = n.xpath('@href').extract_first()
        #     item = ScrapyAppItem()
        #     item['title'] = title
        #     item['link_url'] = link
        #     print("gggggggg")
        #     print(title)
        #     print(link)
        #     print('\n')
        #     yield item

