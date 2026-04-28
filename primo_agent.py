#pip install -r requirements.txt
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def genera_battuta(domanda, configurazione):

    # Generazione risposta del modello
    risposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=domanda,
        config=configurazione
    )

    print("\nRISPOSTA DELL'AGENTE:")
    print(risposta.text)
    print(f"\n{'*'*30}\n")



# --- 1. CARICAMENTO DEL FILE .ENV ---
cartella_attuale = os.path.dirname(os.path.abspath(__file__))
percorso_env = os.path.join(cartella_attuale, '.env')
load_dotenv(dotenv_path=percorso_env, override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print(f"ERRORE: Non trovo la chiave. Ho cercato esattamente in: {percorso_env}")
    exit()

print("✅ Chiave trovata! Avvio dell'agente Gemini in corso...\n")


# --- 2. INIZIALIZZAZIONE DEL CLIENT ---
client = genai.Client(api_key=api_key)


# --- 3. CREAZIONE DELL'AGENTE E DELLE ISTRUZIONI ---
istruzioni_comico = '''
Sei un comico brillante, sarcastico e maestro delle freddure.
Rispondi sempre con battute fulminanti o giochi di parole inaspettati.
'''

# Configuriamo le istruzioni di sistema
configurazione = types.GenerateContentConfig(
    system_instruction=istruzioni_comico,
)

while True:
    domanda = input("\nSu cosa vuoi che generi una battuta? (Scrivi 'basta' per uscire): ")

    # Se l'utente scrive 'basta', il comando 'break' interrompe il ciclo while
    if domanda.lower().startswith("basta") or domanda.lower().endswith("basta"):
        print("Chiusura del programma... Alla prossima!")
        break

    try:
        genera_battuta(domanda, configurazione)

    except Exception as errore:
        print("\n❌ OPS! Si è verificato un errore di comunicazione con Gemini:")
        print(errore)