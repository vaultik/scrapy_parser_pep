BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    # Тесты на сайте ругаются на f'{results_dir}/pep_%(time)s.csv':
    # AssertionError: Убедитесь, что в ключе словаря `FEEDS`
    # перед именем файла указан путь к директории `results/`
    # Если просто results_dir = 'results', то папка создается в pep_parse
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
