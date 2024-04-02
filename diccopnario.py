meme_dict = {

    "CRINGE": "Algo excepcionalmente raro o embarazoso",

    "LOL": "Una respuesta común a algo gracioso",
    
    "HATER": "una persona que desprecia lo que haces",

}

 

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print({meme_dict[word]})

else:

    print("Lo siento, no tengo información sobre la palabra.")
