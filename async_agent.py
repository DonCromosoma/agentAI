#pip install -r requirements.txt
import os
import asyncio
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Carica le variabili dal file .env (dove c'est GEMINI_API_KEY)
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    print(f"ERRORE: Non trovo la chiave. Ho cercato esattamente in: {percorso_env}")
    exit()

print("✅ Chiave trovata! Avvio dell'agente Gemini in corso...\n")
client = genai.Client(api_key=api_key)

# 2. Configurazione dell'Agente
configurazione = types.GenerateContentConfig(
    system_instruction="Sei un comico molto spiritoso che inventa solo barzellette sugli animali"
)

# 3. Funzione asincrona che sostituisce Runner.run()
async def esegui_agente(domanda):
    risposta = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=domanda,
        config=configurazione
    )
    return risposta.text

# 4. Il blocco principale del tuo tutorial
async def main():
    print("Avvio della richiesta all'agente")

    # Avvia la richiesta a Gemini in background
    task_agente = asyncio.create_task(esegui_agente("Dimmi una barzelletta con un cane e un gatto"))

    # Esegue il conteggio mentre Gemini elabora la risposta
    for i in range(1, 10):
        print(f"Elaboro operazioni...{i}")
        await asyncio.sleep(0.8)

    print("Terminate le attività del main")

    # Attende e recupera il risultato
    result = await task_agente

    print("Risposta dell'agente:")
    print(result)

# Avvio del programma
if __name__ == "__main__":
    asyncio.run(main())