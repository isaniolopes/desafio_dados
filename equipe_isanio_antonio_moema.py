#abrir o CSV 

desafio_dados = open('project_twitter_data.csv')   

lista_tweets = [] 

  

#para cada linha dentro do arquivo 

for row in desafio_dados:   

    # nao adiciona as linhas em branco 

    if row[0] != '\n':  

      #remove as quebras de linhas, coloca nas posicoes e coloca em minusculas 

      linha = row.replace('\n','').split(',') 

      lista_tweets.append([linha[0].lower(),linha[1],linha[2]])  

  

#remove cabeçalho 

del(lista_tweets[0]) 

  

arq_positivo = open('positive_words.txt') 

  

positive_words = [] 

#criar a lista de palavras positivas 

for row in arq_positivo: 

    #considerar linhas em branco e nem as que começa com ';' que são comentários do arquivo 

    if row[0] != ';' and row[0] != '\n':    

      positive_words.append(row.replace('\n','')) 

  

  

arq_negativo = open('negative_words.txt') 

  

negative_words = [] 

#criar a lista de palavras negativas 

for row in arq_negativo: 

    #considerar linhas em branco e nem as que começa com ';' que são comentários do arquivo 

    if row[0] != ';' and row[0] != '\n':    

      negative_words.append(row.replace('\n','')) 

  

  

  

resultado = [] 

  

for t in lista_tweets: 

  qtd_positivo = 0 

  qtd_negativo = 0 

  

  tweet_words = t[0].split() #separa lista de palavras a partir de cada tweet 

  retweets = t[1] 

  replies = t[2] 

  

  #conta as palavras positivas no tweet 

  for p in positive_words: 

    if p in tweet_words: 

      qtd_positivo = qtd_positivo + 1 

  

  #conta as palavras negativas no tweet 

  for n in negative_words: 

    if n in tweet_words: 

      qtd_negativo = qtd_negativo + 1 

  

  

  #Number of Retweets, Number of Replies, Positive Score, Negative Score e Net Score  

  resultado.append([retweets, replies, qtd_positivo, qtd_negativo, (qtd_positivo - qtd_negativo)])    

  

#escrever no arquivo 

arq_saida = open("resulting_data.csv","w") 

  

arq_saida.write("Number of Retweets;Number of Replies;Positive Score;Negative Score;Net Score") 

arq_saida.write("\n") 

  

#pega cada linha do resultado 

for r in resultado:

    for i in range(len(r)): 
        arq_saida.write(str(r[i])+';')    
    arq_saida.write("\n")  


   

 #fecha o arquivo 

arq_saida.close() 
