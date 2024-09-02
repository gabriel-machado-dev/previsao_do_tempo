

````
- Entender o que você quer fazer de forma geral
- Você consegue explicar para outra pessoa?
- Descrever em grandes detalhes como você faz esse processo de forma manual hoje
- Quebre cada passo da sua descrição numa tarefa ou modulo, caso seja um projeto maior
- Você consegue quebrar esses passos manuais numa sequência de passos?
- Transforme cada passo em codigo
- Faça isso a cada um dos passos e ao finaizar terá o ‘bot’ pronto


    # Metodo 5q's

    1. Quais dados necessários de entrada ?
    2. O que fazer com eles ?
    3. Restrições do problema ?
    4. Resultado esperado ?
    5. sequência de passos para o resultado

````

##  Oque irá desenvolver?

 Crie um web scraper que roda 100% no terminal em Python que acesse um site de previsão do
 tempo, colete dados meteorológicos e envie um e-mail diário com as informações
 coletadas(não precisa de interface gráfica)

 ### Funcionalidades que o projeto deve possuir:

 1. Navegação Automática:
    ○ Abrir um navegador e acessar um site de previsão do tempo(você pode escolhe o site)
 2. Coleta de Dados Meteorológicos:
    ○ Extrair a temperatura atual.
    ○ Extrair a condição do tempo atual (ex. ensolarado, nublado, etc.).
    ○ Extrair a previsão para os próximos 3 dias (temperatura e condição do tempo).
 3. Tratamento e Formatação de Dados:
    ○ Organizar os dados extraídos em um formato legível.
 4. Envio de E-mail:
    ○ Configurar o envio de e-mails.
    ○ Criar o conteúdo do e-mail com os dados meteorológicos coletados.
    ○ Enviar o e-mail para um destinatário específico.(pode enviar para você mesmo
 como teste)
 5. Automatização do Envio Diário:
    ○ Agendar aexecução do script para rodar diariamente em um horário específico


## Passo a passo


# Bot para extrair dados previsao do tempo do dia atual e dos proximos 3 dias

# entrar no site
# extrair os dados do dia arual: temperatura, condicao do tempo
# extrair a previsao dos proximos 3 dias
# enviar um email com os dados
# agendar a automacao
