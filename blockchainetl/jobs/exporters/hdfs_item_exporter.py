import re
from hdfs import InsecureClient
from json import dumps
from ethereumetl.jobs.exporters.blocks_and_transactions_item_exporter import BLOCK_FIELDS_TO_EXPORT


class HDFSItemExporter:
    def __init__(self, output) -> None:
        # split output
        schema = output[:output.index("//") + 2]
        splits = output[len(schema):].split('/', 2)
        url = schema + splits[0]
        user = splits[1]
        file = '/' + splits[-1]
        self.client = InsecureClient(url, user=user)
        self.file = file
        self._join_multivalued = ','
        self.encoding = 'utf-8'
        self.client.makedirs(re.search(r"(.*\/)[^\/]+", self.file)[1])
        # self.file_exist = self.client.status(hdfs_path=self.file, strict=False)

    def open(self):
        pass

    # def export_items(self, items):
    #     content = ""
    #     for item in items:
    #         # TODO: to csv
    #         content += dumps(item)
    #     self.client.write(self.file, content, encoding='utf-8')

    def export_items(self, items):
        for item in items:
            self.export_item(item)

    # def export_item(self, item):
    #     # TODO: to csv
    #     content = dumps(item)
    #     self.client.write(self.file, content, encoding='utf-8')

    def export_item(self, item):
        # to csv
        content = self.get_content(item)
        values = self._join_multivalued.join(value for value in content)
        self.client.write(self.file, values + '\n', encoding=self.encoding, append=True)

    def close(self):
        pass

    def get_content(self, item, field_iter=BLOCK_FIELDS_TO_EXPORT):
        content = []
        for field_name in field_iter:
            if field_name in item:
                if field_name == 'transactions':
                    for tx in item[field_name]:
                        content.append(dumps(str(tx)))
                else:
                    content.append(str(item[field_name]))
        return content
