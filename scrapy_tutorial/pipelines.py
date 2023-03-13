# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class ScrapyTutorialPipeline:

    def __init__(self, mysql_host, mysql_port, mysql_user, mysql_password, mysql_database):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_password=crawler.settings.get('MYSQL_PASSWORD'),
            mysql_database=crawler.settings.get('MYSQL_DATABASE')
        )

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
			host=self.mysql_host,
			port=self.mysql_port,
			user=self.mysql_user,
			password=self.mysql_password,
		)

        self.curr = self.conn.cursor()

        # Create the database if it doesn't exist
        self.curr.execute(f"CREATE DATABASE IF NOT EXISTS {self.mysql_database}")
        self.conn.commit()

        # Select the database
        self.curr.execute(f"USE {self.mysql_database}")

        # Create the table if it doesn't exist
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS portfolio (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                details_link VARCHAR(255),
                image VARCHAR(255)
            )
        """)
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        cursor.execute(
        """insert into portfolio (title, details_link, image) values (%s, %s, %s)""",
        (
            item['title'],
            item['details_link'],
            item['image']
        ))
        self.conn.commit()
        cursor.close()
