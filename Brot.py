# coding=utf-8
import os

from flask import Flask, request
from Schaufel import report_fnde

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def began():
    if request.method == 'GET':
        report_fnde()
        return "Projeto ! - Fim do Relatório"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)