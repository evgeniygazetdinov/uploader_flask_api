from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/archive", methods=['DELETE'])
def remove_from_storage():
    """
    удалить архив
    :return:
    """
    return jsonify({'message':'deleted'})


@app.route("/archive", methods=['POST'])
def set_archive_on_start():
    """
    поставить архив на загрузку
    :return:
    """
    archive_id = request.args.get('id')
    print(request.get_json())
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route("/")
def check_archive_state():
    """
    проверка состояния скачки
    :return:
    """
    archive_id = request.args.get('id')
    return jsonify({'message':'checked'})