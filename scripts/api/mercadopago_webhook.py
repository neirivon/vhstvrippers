from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import json
import os
from datetime import datetime

app = FastAPI()

# Caminho onde os logs dos webhooks serão armazenados
WEBHOOK_LOG_PATH = "data/pagamentos/webhook_log.json"

# Garante que a pasta 'data/pagamentos' exista
os.makedirs(os.path.dirname(WEBHOOK_LOG_PATH), exist_ok=True)

@app.post("/api/mercadopago/webhook")
async def receber_webhook(request: Request):
    try:
        # Recebe e carrega o JSON enviado pelo MercadoPago
        payload = await request.json()
        print("📡 Webhook recebido:", payload)

        # Adiciona timestamp para registro
        payload["_timestamp"] = datetime.now().isoformat()

        # Lê histórico atual, se existir
        if os.path.exists(WEBHOOK_LOG_PATH):
            with open(WEBHOOK_LOG_PATH, "r", encoding="utf-8") as f:
                historico = json.load(f)
        else:
            historico = []

        # Adiciona o novo evento ao histórico
        historico.append(payload)

        # Salva de volta no arquivo
        with open(WEBHOOK_LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=2, ensure_ascii=False)

        return JSONResponse(status_code=200, content={"status": "ok", "message": "Webhook processado com sucesso"})

    except Exception as e:
        print("❌ Erro ao processar webhook:", e)
        return JSONResponse(status_code=500, content={"status": "erro", "detalhe": str(e)})

# ✅ Rodando com segurança sem precisar nome de módulo
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

