import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.constants import (
    DATETIME_FORMAT, results_dir, status_summary_file
)


class PepParsePipeline:

    def __init__(self):
        self.statuses = defaultdict(int)
        results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.now().strftime(DATETIME_FORMAT)
        file_name = f'{status_summary_file}_{now_formatted}.csv'
        file_path = results_dir / file_name

        results_data = (
            ['Статус', 'Количество'],
            *([[status, count] for status, count in self.statuses.items()]),
            ['Total', sum(self.statuses.values())]
        )

        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results_data)
