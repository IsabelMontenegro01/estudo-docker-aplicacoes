from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/status")
def status():
    return jsonify(
        servico="api",
        estado="disponivel",
        mensagem="A API respondeu pela rede interna do Compose.",
    )
