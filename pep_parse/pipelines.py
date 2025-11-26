import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.constants import (
    BASE_DIR, DATETIME_FORMAT, RESULTS_DIR, STATUS_SUMMARY_FILE
)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.now().strftime(DATETIME_FORMAT)
        file_name = f'{STATUS_SUMMARY_FILE}_{now_formatted}.csv'
        file_path = self.results_dir / file_name

        results_data = (
            ('Статус', 'Количество'),
            *self.statuses.items(),
            ('Total', sum(self.statuses.values()))
        )

        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results_data)
