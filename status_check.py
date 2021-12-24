import os
import json
import shutil
from datetime import datetime
import time

DOWNLOAD_PLACE = "/download_session/"
FORMAT = '.json'
DATE_NOW = datetime.now().strftime("%Y-%m-%d %H:%M")
# TODO ADD typing

class Session(object):
    """
    первичная реализация записи о загрузках
    """
    def __init__(self, url):
        self.id = username
        self.url = url
        self.file = chat
        self.status_of_file = message_id
        self.downloaded_file_path = (
            os.getcwd()
            + DOWNLOAD_PLACE
            + str(self.id)
            + "/"
            + str(self.file)
            + ".json"
        )
        if os.path.exists(self.user_file_path):
            self.user_folder = os.getcwd() + DOWNLOAD_PLACE + str(self.username)
            self.user_info = self.get_session_details()
            self.save_user_info()
        else:
            self.user_info = {
                "id": id,
                "url": url,
                "file": file
                "state": {'file_status':status_of_file,
                          'download_progress': False,
                          'pack_progress': False
                          }
                "path_of_download": downloaded_file_path,
                "last_action": DATE_NOW
            }
            self.user_folder = self.create_user_folder()
            self.save_user_info()

    def get_session_details(self):
        user_session_path = self.user_folder + ("/{}" + FORMAT).format(self.username)
        with open(user_session_path) as json_file:
            data = json.load(json_file)
            return data

    def update_user_info(self, value, condition):
        self.user_info[value] = condition
        self.save_user_info()

    def update_last_action(self):
        self.user_info["last_action"] = DATE_NOW

    def update_state_user(self, state, value, password=False):
        self.update_last_action()
        self.user_info["state"][state] = value
        self.save_user_info()

    def get_user_info_value(self, value):
        self.update_last_action()
        return self.user_info[value]

    def save_user_info(self):
        self.update_last_action()
        with open(
            self.user_folder + ("/{}" + FORMAT).format(self.username), "w", encoding="utf-8"
        ) as f:
            json.dump(self.user_info, f, ensure_ascii=False, indent=4)

    def create_user_folder(self):
        os.makedirs(os.getcwd() + DOWNLOAD_PLACE + str(self.id), exist_ok=True)
        return str(os.getcwd() + DOWNLOAD_PLACE + str(self.id))

    def clean_session(self):
        shutil.rmtree(self.user_folder, ignore_errors=True)

    def get_cur_download_id(self):
        cur_ids = next(os.walk(DOWNLOAD_PLACE))[1]
        if len(cur_ids) == 0:
            return 1
        return max(cur_ids)

    def create_info_file

import sys
import os
import sqlite3

class ArchiveDB:
    def __init__(self):
        self.name_db = "archive.sqlite"
        self.base_path = os.getcwd() + "/" + self.name_db
        self.query_creation =
            """CREATE TABLE [downloads] ( [id] integer,
                [url] text, [file] text, [status_of_file] text,
                [download_path] text );"""

        if not os.path.exists(self.base_path):
            self.db = self.create_db()
            self.connection = sqlite3.connect(self.name)
            for query in self.query_creation:
                self.edit(query)
        else:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

    def create_db(self):

        sqlite3.connect(self.name)
        return name

    def insert(self, query):
        query_res = self.cursor.execute(query)
        res = query_res.fetchall()
        self.connection.commit()
        return res

    def edit(self, query):
        db = self.connection
        cursor = db.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def select(self, query):
        if self.db.open():
            res = []
            sql_query = QSqlQuery()
            sql_query.exec_(query)
            while sql_query.next():
                res.append(sql_query.value(0))
            self.db.close()
            return res

    def close(self):
        self.connection.close()

    def get_tables_from_mdb_dump(self, mdb_db):
        tables = []
        for tbl in mdb.list_tables(mdb_db):
            tables.append(tbl)
        return tables

    def exists(self, table_name):
        query = "SELECT * FROM sqlite_master WHERE type='table' AND  name='{}'".format(
            table_name
        )
        res = self.insert(query)
        if len(res) > 0:
            return True
        return False

if __name__ == "__main__":
    db = Bicycle_db()

