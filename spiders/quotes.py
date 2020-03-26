# -*- coding: utf-8 -*-
import scrapy
from ..items import GoodquotesItem

class QuoteSpider(scrapy.Spider):
    # name of this spider
    name = 'quotes'
    page_number = 2
    
    # list of urls to scrape from
    start_urls = ["https://www.goodreads.com/quotes?page=1"]

    def parse(self, response):
        items = GoodquotesItem()
        all_div_quote = response.css(".quoteDetails")

        for q in all_div_quote:
            quote = q.css("div.quoteText::text").extract()
            author = q.css("span.authorOrTitle::text").extract()
            tag = q.css(".left a::text").extract()
            likes = q.css(".right .smallText").css("::text").extract()
            image = q.css(".leftAlignedImage img::attr(src)").extract()
            
            items['quote'] = quote
            items['author'] = author
            items['tag'] = tag
            items['likes'] = likes
            items['image'] = image
            
            yield items
        
        next_page = "https://www.goodreads.com/quotes?page=" + str(QuoteSpider.page_number)
        # next_page = response.css("li.next a::attr(href)").get()

        if QuoteSpider.page_number <= 100:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)

        # if next_page is not None:
        #     yield response.follow(next_page, callback = self.parse)


