import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']
    # Для ревьювера: вы здесь написали "Объединяем поиски
    # в один единственный .css, вызываем селектор методом getall,
    # в цикле перебираем уже полученный список."
    # Но я не понял, что не так. Вроде так и сделано.

    def parse(self, response):
        all_pep_links = response.css(
            'section#index-by-category table.pep-zero-table '
            'tbody tr a[href^="pep-"]::attr(href)'
        ).getall()
        for pep_link in all_pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        pep, name = title.split(' – ')
        _, number = pep.split()
        status = response.xpath(
            '//dl[contains(@class, "rfc2822")]//abbr/text()'
        ).get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
