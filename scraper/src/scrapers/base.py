import requests


class Scraper:
    url = ""

    @classmethod
    def fetch_data():
        raise NotADirectoryError

    @staticmethod
    def parse_fetched_data(fetched_data):
        raise NotImplementedError

    @staticmethod
    def scrape():
        raise NotImplementedError


class ApiGetScraper(Scraper):
    params = {}
    headers = {}

    @classmethod
    def fetch_data(cls, **kwargs):
        return requests.get(cls.url, params=cls.params, headers=cls.headers, **kwargs)

# TODO: for popular we will need selenium or something strong to bypass the waf