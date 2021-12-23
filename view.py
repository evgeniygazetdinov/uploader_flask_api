from flask import Flask, jsonify, request
from service import Downloader, FilePacker
import json


app = Flask(__name__)


@app.route("/archive", methods=["DELETE"])
def remove_from_storage():
    """
    удалить архив
    :return:
    """
    return jsonify({"message": "deleted"})


@app.route("/archive", methods=["GET"])
def set_archive_on_start():
    """
    поставить архив на загрузку
    :return:
    """
    archive_id = request.args.get("id")
    uploader = Downloader(
        "https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48"
    )
    upload_result = uploader.download_file()
    packing = FilePacker(upload_result)

    return (
        json.dumps({"success": packing.pack()}),
        200,
        {"ContentType": "application/json"},
    )


@app.route("/")
def check_archive_state():
    """
    проверка состояния скачки
    :return:
    """
    archive_id = request.args.get("id")
    return jsonify({"message": "checked"})
