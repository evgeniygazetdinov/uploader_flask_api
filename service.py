import requests
import os
import sys
import json
import time
from tqdm import tqdm
import xtarfile as tarfile
import uuid
from datetime import datetime


class Service:
    def __init__(self, cur_status: str):
        self.cur_status = cur_status


class Downloader(Service):
    """
    принимает урлу отдает струнгу с путем файла
    """

    def __init__(self, url: str):
        super().__init__("download")
        self.url = url
        self.storage_place = ""

    def generate_filename(self) -> str:
        return str(uuid.uuid4())

    def download_file(self) -> str:
        """
        response = requests.get(self.url, stream=True)
        filename = self.generate_filename()

        with open(filename, "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)
        return os.path.dirname(os.path.abspath(filename)) + "/" + filename
        """

        with io.BytesIO() as f:
            start = time.clock()
            r = requests.get(url, stream=True)
            total_length = r.headers.get("content-length")
            dl = 0
            if total_length is None:  # no content length header
                f.write(r.content)
            else:
                for chunk in r.iter_content(1024):
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(30 * dl / int(total_length))
                    sys.stdout.write(
                        "\r[%s%s] %s Mbps"
                        % (
                            "=" * done,
                            " " * (30 - done),
                            dl // (time.clock() - start) / 100000,
                        )
                    )


class FilePacker(Service):
    """
    Принимает файл --> пакует--> удаляет -->отдает стрингу с местом архива архив
    """

    def __init__(self, file_name: str):
        super().__init__("packing")
        self.cur_file = file_name
        self.cur_dir = os.getcwd()

    def generate_archive_name(self) -> str:
        now = datetime.now()  # current date and time
        return now.strftime("%m%d%Y%-H%M%S") + ".tar.gz"

    def pack(self) -> str:
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
