import requests
import smtplib
from email.message import EmailMessage

# --- CONFIGURAÇÕES ---
SITES_PARA_CHECAR = [
    "https://www.google.com",
    "https://github.com",
    "https://site-que-nao-existe-123.com"
]

MEU_EMAIL = "CONFIGURAR_EMAIL"
SENHA_APP = "CONFIGURAR_SENHA"

def enviar_alerta(site, erro):
    msg = EmailMessage()
    msg.set_content(f"O site {site} apresentou erro: {erro}")
    msg['Subject'] = f"🚨 ALERTA: Site Fora do Ar - {site}"
    msg['From'] = MEU_EMAIL
    msg['To'] = MEU_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MEU_EMAIL, SENHA_APP)
            smtp.send_message(msg)
        print(f"E-mail enviado para {site}")
    except Exception as e:
        print(f"Erro ao enviar: {e}")

print("Iniciando checagem...")

for site in SITES_PARA_CHECAR:
    try:
        r = requests.get(site, timeout=10)

        if r.status_code != 200:
            enviar_alerta(site, f"Status: {r.status_code}")
        else:
            print(f"✅ {site} está online!")

    except Exception as e:
        enviar_alerta(site, str(e))

print("Fim da checagem.")