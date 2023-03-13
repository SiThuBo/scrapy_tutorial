# scrapy_tutorial
This is a Scrapy web scraping project that extracts information and stores it in an Mysql database.

## Environment

- Docker
- Python 3.10
- Scrapy 2.8.0
- Mysql 5.7

### Installation
#### Step1 Clone this project

```
git clone https://github.com/SiThuBo/scrapy_tutorial.git
```

#### Step2 Starting the development environment using Docker

```
# to build and start your application

docker-compose up --build -d
```
### Usage
To use this web scraping example, run the following command in the terminal to start the spider:

```
docker-compose exec scrapy bash
scrapy crawl myspider -s MYSQL_HOST='localhost' -s MYSQL_USER='root' -s MYSQL_PASSWORD='root' -s MYSQL_DATABASE='scraped_data'
```
Scrapy will start running the spider and output the results to the console and insert to database.
