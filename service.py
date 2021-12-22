import requests
import os
import sys
import json
from tqdm import tqdm
import xtarfile as tarfile

class Service:
    def __init__(self, cur_status):
        self.cur_status = cur_status


class Downloader(Service):
    """
    принимает урлу отдает струнгу с путем файла
    """
    def __init__(self, url):
        super().__init__('download')
        self.url = url
        self.storage_place = ''

    def generate_filename(self):
        template = "Output_{YYYYMMDD}_{HHMMSS}.txt"
        return template.format(YYYYMMDD="20190606", HHMMSS="130612")

    def download_file(self):
        response = requests.get(self.url, stream=True)
        filename = self.generate_filename()

        with open(filename, "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)
        return os.path.dirname(os.path.abspath(filename))+ '/' +filename


class FilePacker(Service):
    """
    Принимает файл --> пакует--> удаляет -->отдает стрингу с местом архива архив
    """
    def __init__(self, file_name):
        super().__init__('packing')
        self.cur_file = file_name

    def pack(self):
        with tarfile.open('some-archive.tar.gz', 'w:zstd') as archive:
            archive.add(self.cur_file)