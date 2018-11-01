from gnewsclient import gnewsclient
client = gnewsclient()

parametros= client.get_config()
news= client.get_news()

#Mudar parametros

client.edition = 'Brazil'
client.topic = 'business'
client.language = 'portuguese'

print(news)

