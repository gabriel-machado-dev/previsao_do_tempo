from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
import logging as lg
import re

load_dotenv()
lg.basicConfig(level=lg.ERROR, format='%(asctime)s - %(message)s')

# inicializar o driver do selenium
def run_driver(site_url):
    try:
        chorme_options = Options()

        arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--disable-notifications', '--incognito', '--block-new-web-contentes', '--no-default-browser-check', 'window-position=36,68', '--headless']
        for argument in arguments:
            chorme_options.add_argument(argument)

        # desabilitar pop-up de navegador controlado por automacao
        chorme_options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])

        # Using experimental settings
        chorme_options.add_experimental_option('prefs', {
            # Alterar o local padrão de ‘download’ de arquivos
            'download.default_directory': 'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\projetos '
                                          'pyautogui\\selenium_dev_aprender',
            # notificar o Google chrome sobre essa alteração
            'download.directory_upgrade': True,
            # Desabilitar a confirmação de ‘download’
            'download.prompt_for_download': False,
            # Desabilitar notificações
            'profile.default_content_setting_values.notifications': 2,
            # Permitir multiplos downloads
            'profile.default_content_setting_values.automatic_downloads': 1,

        })

        driver = webdriver.Chrome(options=chorme_options)
        driver.get(site_url)

        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
                TimeoutException
            ]
        )

        return driver, wait
    except Exception as e:
        lg.error(f'Error occurred while initializng driver: {type(e).__name__} - {e}')
        return None

# extrair os dados do clima
def extract_weather_data():
  # entrar no site
  driver, wait = run_driver('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/297/duquedecaxias-rj')

  # extrair os xpath
  div = wait.until(EC.presence_of_all_elements_located(('xpath', '//section[@class="accordion-card -daily-infos _border-bl-light-1"]')))

  # extrair os dados do dia atual e dos proximos dias: temperatura, condicao do tempo
  # ['03', 'ter', '18°', '29°', '1%', 'Dia de sol com algumas nuvens e névoa ao amanhecer. Noite com poucas nuvens.']
  dia_atual = []
  previsao_proximos_dias = []
  for i, d in enumerate(div[:4]):
      day_data = d.text.split('\n')[0]
      day = d.text.split('\n')[1]
      temp_max = d.text.split('\n')[3]
      temp_min = d.text.split('\n')[2]
      porcentagem_chuva = d.text.split('\n')[4]
      cond = d.text.split('\n')[5]

      # extrair os dados do dia atual
      if i == 0:
          dia_atual.append({
              'day_data': day_data,
              'day': day,
              'temp_max': temp_max,
              'temp_min': temp_min,
              'porcentagem_chuva': porcentagem_chuva,
              'cond': cond
          })
      # extrair a previsao dos proximos 3 dias
      else:
          previsao_proximos_dias.append({
              'day_data': day_data,
              'day': day,
              'temp_max': temp_max,
              'temp_min': temp_min,
              'porcentagem_chuva': porcentagem_chuva,
              'cond': cond
          })


  return dia_atual, previsao_proximos_dias

# gerar um template html com os dados
def generate_weather_template(dia_atual, previsao_proximos_dias):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .weather-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .day {{
                border: 1px solid #ccc;
                padding: 10px;
                margin: 10px;
                width: 300px;
                text-align: center;
            }}
            .day h2 {{
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <div class="weather-container">
            <div class="day">
                <h2>Dia Atual</h2>
                <p>Data: {dia_atual[0]['day_data']}</p>
                <p>Dia: {dia_atual[0]['day']}</p>
                <p>Temp Máx: {dia_atual[0]['temp_max']}</p>
                <p>Temp Mín: {dia_atual[0]['temp_min']}</p>
                <p>Probabilidade de Chuva: {dia_atual[0]['porcentagem_chuva']}</p>
                <p>Condição: {dia_atual[0]['cond']}</p>
            </div>
            {"".join([f'''
            <div class="day">
                <h2>Dia {dia['day_data']}, {dia['day']}</h2>
                <p>Data: {dia['day_data']}</p>
                <p>Dia: {dia['day']}</p>
                <p>Temp Máx: {dia['temp_max']}</p>
                <p>Temp Mín: {dia['temp_min']}</p>
                <p>Probabilidade de Chuva: {dia['porcentagem_chuva']}</p>
                <p>Condição: {dia['cond']}</p>
            </div>
            ''' for i, dia in enumerate(previsao_proximos_dias)])}
        </div>
    </body>
    </html>
    """
    return html_content

# enviar um email com os dados
def send_email(recipient_email):
    dia_atual, previsao_proximos_dias = extract_weather_data()

    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    if not EMAIL_USER or not EMAIL_PASSWORD:
        lg.error('Email credentials not found')
        raise EnvironmentError('Email credentials not found')


    msg = EmailMessage()
    msg['Subject'] = 'Previsão do Tempo'
    msg['From'] = EMAIL_USER
    msg['To'] = recipient_email
    msg.add_header('Content-Type', 'text/html')

    html_content = generate_weather_template(dia_atual, previsao_proximos_dias)
    msg.set_content(html_content, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)

def validate_email(email):
    while True:
        if re.findall(r'@.{1,8}\.com', email):
            return email
        else:
            email = input('Email inválido, digite novamente: ')


if __name__ == '__main__':
    recipient_email = input('Digite o email do destinatário: ')
    recipient_email = validate_email(recipient_email)
    send_email(recipient_email)
    print('Email enviado com sucesso!')
