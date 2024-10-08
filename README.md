# Weather Forecast Email Sender

## Descrição do Projeto

Este projeto é um script Python que extrai dados de previsão do tempo de um site e envia essas informações por email. Ele utiliza Selenium para web scraping e smtplib para envio de emails.

## Funcionalidades ⚙️

 - Extrai dados de previsão do tempo para o dia atual e os próximos três dias.
 - Gera um template HTML com os dados extraídos.
 - Envia um email com a previsão do tempo formatada em HTML.

## Configuração para Usuários 🔧
### Requisitos
- `Python 3.x`
- `Google Chrome`
- `ChromeDriver`
- `Variáveis de ambiente para credenciais de email`

## Instruções para Execução ▶️

1. Configure as variáveis de ambiente: Crie um arquivo .env no diretório raiz e adicione suas credenciais de email:


```bash
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha
```
2. Execute o script:

```bash
python app.py
```
## Configuração para Desenvolvedores 🔧
### Requisitos

- Python 3.x
- Google Chrome
- ChromeDriver

### Instalação das Dependências

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/weather-forecast-email-sender.git
cd weather-forecast-email-sender
```

2. Configure um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

3. Instale as dependências usando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Exemplo de Uso 💡
1. Configure as variáveis de ambiente conforme descrito acima.

``Obs``: EMAIL_PASSWORD -> Vá em seu e-mail, gerenciar sua conta, pesquise por `app password`, gere uma senha e essa será a senha do e-mail

2. Execute o script:
```bash
python app.py
```
3. Verifique seu email para a previsão do tempo.

## Problemas Conhecidos ⚠️
- O script depende de uma conexão estável com a internet para acessar o site de previsão do tempo.
- O ChromeDriver deve ser compatível com a versão do Google Chrome instalada no sistema.

## Licença 📝

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
