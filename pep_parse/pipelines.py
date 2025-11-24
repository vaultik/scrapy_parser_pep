import csv
from datetime import datetime as dt

from pep_parse.constants import (
    DATETIME_FORMAT, results_dir, status_summary_file
)


RESULTS_STATUS = {
    'A': 0,
    'D': 0,
    'F': 0,
    'P': 0,
    'R': 0,
    'S': 0,
    'W': 0,
    'Total': 0
}


class PepParsePipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        print("PIPELINE GOT ITEM:", item['number'], item['status'])
        RESULTS_STATUS[item['status'][0]] += 1
        RESULTS_STATUS['Total'] += 1
        return item

    def close_spider(self, spider):
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.now().strftime(DATETIME_FORMAT)

        file_name = f'{status_summary_file}_{now_formatted}.csv'
        file_path = results_dir / file_name

        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус', 'Количество'])

            for status, count in RESULTS_STATUS.items():
                writer.writerow([status, count])
