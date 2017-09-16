# -*- coding: utf-8 -*-
import scrapy
import re

class PaginasamarillasGeriatricosSpider(scrapy.Spider):
    name = "paginasamarillas_geriatricos"
    allowed_domains = ["www.paginasamarillas.com.ar"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
    }

    def start_requests(self):
        urls = [
            'http://www.paginasamarillas.com.ar/b/geriatricos/cordoba/'
        ]

        for url in urls:
            yield scrapy.Request(
                url=url,
                headers=self.headers
            )

    def parse(self, response):
        self.logger.info('- Parsing %s', response.url)
        FICHAS_SELECTOR = 'ul.businesses li'
        SOURCE_TYPE = 'PAGINAS_AMARILLAS'

        for ficha in response.css(FICHAS_SELECTOR):
            ficha = {
                'source' : {
                    'id'  : ficha.xpath('.//@data-bid').extract_first(),
                    'url' : ficha.xpath('.//@data-href').extract_first(),
                    'type': SOURCE_TYPE
                },
                'nombre'     : ficha.css('.business-name ::text').extract_first(),
                'descripcion': ficha.xpath('.//div[@itemprop="description"]/text()').extract_first(),
                'email'      : ficha.xpath('.//input[contains(@class, "questionData")]/@value').extract_first(),
                'url'        : ficha.css('.business-web::attr(href)').extract_first(),
                'imagen_url' : ficha.css('.logoad::attr(src)').extract_first(),
                'telefonos': {
                    'destacado'   : ficha.xpath('.//div[@data-toggle="freecall"]/@data-freecall').extract_first(),
                    'alternativos': [
                        ''.join(re.findall('\d+', telefono)) for telefono in ficha.xpath('.//a[@itemprop="telephone"]/@href').extract()
                    ]
                },
                'direccion': {
                    'streetAddress': ''.join(str(ficha.css('.business-address').xpath('.//span[@itemprop="streetAddress"]/text()').extract_first()).split()),
                    'addressLocality': ''.join(str(ficha.css('.business-address').xpath('.//span[@itemprop="addressLocality"]/text()').extract_first()).split()),
                    'geo': {
                        'latitude': ficha.xpath('.//span[@itemprop="geo"]/meta[@itemprop="latitude"]/@content').extract_first(),
                        'longitude': ficha.xpath('.//span[@itemprop="geo"]/meta[@itemprop="longitude"]/@content').extract_first(),
                    }
                }
            }

            if ficha['source']['id'] is not None:
                yield ficha

            next_page_url = response.css('.m-results-pagination li.last a::attr(href)').extract_first()
            if next_page_url is not None:
                yield scrapy.Request(
                    response.urljoin(next_page_url),
                    headers=self.headers
                )