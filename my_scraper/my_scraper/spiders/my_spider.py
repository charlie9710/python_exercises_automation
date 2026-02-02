import scrapy

class MySpider(scrapy.Spider):
  name = "my_spider"
  start_urls = ['https://es.wikipedia.org/wiki/Wikipedia:Portada']

  def parse(self,response):
    yield{
      'title':response.css('title::text').get(),
      'paragraphs': response.css('p::text').get()
    }
    # #Extract the title of the page
    # title = response.css('title::text').get()

    # #Extract all the paragraph text
    # paragraphs= response.css('p::text').get()

    # #Print the extracted data
    # print(f"Title: {title}")
    # print(f"Paragraphs: {paragraphs}")