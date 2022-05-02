import os

class Config:

    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = '11fc10d8188549cfad1539f1ad053fce'
    SECRET_KEY='vivioonana'

class ProdConfig(Config):
    pass


class DevConfig(Config):
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}