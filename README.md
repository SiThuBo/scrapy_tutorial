# scrapy_tutorial
This is a Scrapy web scraping project that extracts information and stores it in an Mysql database.

## Environment
- Python 3.10
- Scrapy 2.8.0
- Mysql 5.7

## Installation
The steps to install Python 3.10 on a Windows computer:

1. Go to the official Python website (https://www.python.org/downloads/windows/) and download the latest release of Python 3.10 for Windows.
2. Run the downloaded installer file and follow the installation wizard.
3. On the first screen of the installation wizard, make sure to check the box "Add Python 3.10 to PATH" to ensure that you can use Python from the command prompt or PowerShell.
4. Customize the installation as necessary by selecting or deselecting optional features.
5. Click "Install" to start the installation process.
6. Once the installation is complete, you can verify that Python 3.10 is installed by opening a command prompt or PowerShell window and typing python --version.


Clone this project
```
git clone https://github.com/SiThuBo/scrapy_tutorial.git
```

To install the packages listed in a requirements.txt

1. Open a command prompt or terminal window.
2. Navigate to the directory where the requirements.txt file is located using the cd command.
3. Run the following command to install the packages listed in the requirements.txt file:
```
pip install -r requirements.txt
```
4. pip will download and install all the required packages and their dependencies.

## Usage

To run a Scrapy spider, follow these steps:

1. Open a command prompt or terminal window.

2. Navigate to the directory where your Scrapy project is located using the cd command.

3. Run the following command to start the spider:
```
scrapy crawl myspider -s MYSQL_HOST='localhost' -s MYSQL_USER='root' -s MYSQL_PASSWORD='root' -s MYSQL_DATABASE='scraped_data'
```
4. Scrapy will start running the spider and output the results to the console and insert to database.
