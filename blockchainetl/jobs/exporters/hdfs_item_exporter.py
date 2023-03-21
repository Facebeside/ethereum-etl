import re
from hdfs import InsecureClient
from json import dumps


class HDFSItemExporter:
    def __init__(self, output) -> None:
        # TODO: split output
        self.client = InsecureClient('http://192.168.1.103:9870', user="zebra")
        self.file = "/test/data.csv"
        self.client.makedirs(re.search(r"(.*\/)[^\/]+", self.file)[1])

    def open(self):
        pass

    def export_items(self, items):
        content = ""
        for item in items:
            # TODO: to csv
            content += dumps(item)
        self.client.write(self.file, content, encoding='utf-8')

    def export_item(self, item):
        # TODO: to csv
        content = dumps(item)
        self.client.write(self.file, content, encoding='utf-8')

    def close(self):
        pass
