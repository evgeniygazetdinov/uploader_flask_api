import requests
import os
import sys
import json
from tqdm import tqdm
import xtarfile as tarfile
import uuid
from datetime import datetime




class Service:
    def __init__(self, cur_status):
        self.cur_status = cur_status


class Downloader(Service):
    """
    принимает урлу отдает струнгу с путем файла
    """

    def __init__(self, url):
        super().__init__("download")
        self.url = url
        self.storage_place = ""

    def generate_filename(self):
        return str(uuid.uuid4())

    def download_file(self):
        response = requests.get(self.url, stream=True)
        filename = self.generate_filename()

        with open(filename, "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)
        return os.path.dirname(os.path.abspath(filename)) + "/" + filename


class FilePacker(Service):
    """
    Принимает файл --> пакует--> удаляет -->отдает стрингу с местом архива архив
    """

    def __init__(self, file_name):
        super().__init__("packing")
        self.cur_file = file_name
        self.cur_dir = os.getcwd()

    def generate_archive_name(self):
        now = datetime.now()  # current date and time
        return now.strftime("%m-%d-%Y%H-%M-%S") + '.tar.gz'

    def pack(self):
        def make_tarfile(
            output_filename=self.generate_archive_name(), source_dir=self.cur_file
        ):
            with tarfile.open(output_filename, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
            return source_dir + "/" + output_filename

        def remove_dir_file_after_packing(self):
            os.remove(self.cur_file)

        archive_name = make_tarfile()
        remove_dir_file_after_packing(self)
        return archive_name
