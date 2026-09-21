from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/status")
def status():
    return jsonify(
        equipamento="painel de sensores",
        sensores_ativos=3,
        estado="operacao normal",
        unidade="laboratorio de manutencao",
    )
