🖥️ Python Website Monitor

Projeto em Python para monitoramento de disponibilidade de sites, com envio automático de alertas por e-mail em caso de falhas.

🎯 Objetivo do Projeto

Este projeto demonstra habilidades práticas em:

Monitoramento de disponibilidade de websites

Detecção e tratamento de falhas de conexão

Automação de envio de alertas por e-mail

Uso de bibliotecas Python para requisições HTTP

Estruturação e documentação de projeto para portfólio profissional

Aplicabilidade real:

Este sistema simula monitoramento utilizado em ambientes corporativos, como:

Infraestrutura de TI

DevOps

Monitoramento de sistemas críticos

Cybersecurity / SOC (Security Operations Center)

Ele pode ser expandido para integrações com dashboards, alertas em tempo real via Slack ou Telegram e análises de disponibilidade de serviços essenciais.

Observação: Este é a primeira fase do projeto (MVP). A segunda fase incluirá funcionalidades adicionais e integração com o organizador ponto Pi.

⚙️ Tecnologias Utilizadas

Python 3

Biblioteca requests

SMTP para envio de e-mails

Automação de scripts Python

Ambiente virtual Python (venv)

📁 Estrutura do Projeto

python-site-monitor/
│
├── alerta_sites.py          # Script principal de monitoramento
├── README.md                # Documentação do projeto
├── .gitignore               # Arquivos a ignorar no GitHub
├── images/                  # Imagens de demonstração
│   ├── script-success.png
│   ├── email-success.png
│   ├── script-error.png
│   └── email-alert-error.png
└── venv/                    # Ambiente virtual (não subir para o GitHub)

Dica: Verifique se a pasta venv/ e qualquer arquivo com credenciais, como config.py, estão incluídos no .gitignore antes de subir para o GitHub.

🧪 Como Executar o Projeto
1️⃣ Criar ambiente virtual
python3 -m venv venv
2️⃣ Ativar o ambiente virtual

Linux / WSL:

source venv/bin/activate

Windows:

venv\Scripts\activate
3️⃣ Instalar dependências
pip install requests
4️⃣ Configurar credenciais de e-mail

No código, utilize um placeholder para a senha antes de subir ao GitHub:

MEU_EMAIL = "seu_email@gmail.com"
SENHA_APP = "CONFIGURAR_SENHA"

⚠️ Nunca publique sua senha real.

5️⃣ Executar o script
python3 alerta_sites.py

O script iniciará a verificação dos sites configurados.

🚀 Funcionamento do Sistema

O script realiza os seguintes passos:

Carrega a lista de sites configurados

Envia uma requisição HTTP para cada site

Verifica se o site respondeu corretamente

Caso ocorra erro de conexão ou status inválido:

Um alerta automático é enviado por e-mail

O erro é registrado no terminal

🖥️ Demonstração do Script
Sites online

Exemplo de saída:

Iniciando checagem...

✅ https://www.google.com está online!
✅ https://github.com está online!

Fim da checagem.
Sites com erro

Exemplo de erro detectado:

NameResolutionError
Max retries exceeded
Failed to resolve host
📧 Envio de Alerta por E-mail

Quando um site apresenta falha, o sistema envia automaticamente um alerta:

Assunto do e-mail:

🚨 ALERTA: Site Fora do Ar

Mensagem:

O site apresentou erro de conexão.
🔐 Como Gerar a Senha de Aplicativo do Gmail (16 dígitos)

Para enviar e-mails via Python, é necessário criar uma senha de aplicativo.

Passo 1 — Ativar verificação em duas etapas

Acesse a segurança da conta Google:
https://myaccount.google.com/security

Ative Verificação em duas etapas.

Passo 2 — Gerar senha de aplicativo

Acesse:
https://myaccount.google.com/apppasswords

Escolha:

Aplicativo → Mail

Dispositivo → Outro

Nome → python-monitor

Clique em Gerar e copie a senha de 16 dígitos.

Passo 3 — Inserir senha no código

Use sem espaços:

SENHA_APP = "abcdefghijklmnop"

⚠️ Lembre-se: no GitHub, substitua por CONFIGURAR_SENHA.

🔒 Segurança

Nunca publique credenciais reais no repositório.

Arquivos de configuração com senha (config.py) devem estar no .gitignore.

A senha deve ser configurada manualmente no ambiente local antes da execução.

👩‍💻 Autora

Priscila Ferreira de Gouvêia Tenório
Formação em Desenvolvimento Back-End
Pós-graduação em Cybersecurity e Cybercrime

Projeto desenvolvido como prática de automação, monitoramento de sistemas e construção de portfólio em tecnologia.