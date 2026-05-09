# PEP Parser (Scrapy)
 
A Scrapy spider that crawls python.org and collects PEP data into CSV reports.
 
## Features
 
- Crawls all PEP pages and exports: number, title, status → `pep_TIMESTAMP.csv`
- Aggregates PEP count by status + total count → `status_summary_TIMESTAMP.csv`

## Tech Stack

- **Python 3.12+**
- **Scrapy 2.5.1**
- **lxml 5.2.1**
- **pytest 6.2.5**

Full list of dependencies: `requirements.txt`
 
## How to Run
 
```bash
# Clone the repository
git clone https://github.com/vaultik/scrapy_parser_pep
cd scrapy_parser_pep
 
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
 
# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
 
# Run the spider
scrapy crawl pep
```
 
Output CSV files are saved to the `data/` directory.
 
## Author
 
[github.com/vaultik](https://github.com/vaultik)
 
