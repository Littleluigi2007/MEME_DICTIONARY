print("merhaba")


meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BRB": "birazdan gelirim",
            "GN": "iyi geceler",
            "GM": "günaydın",
            "AFK": "bilgisayardan uzak",
            }
            

for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


    if word in meme_dict.keys():
        print("kelimenin anlamı", meme_dict[word])
    else:
     print("bilinmiyor")
