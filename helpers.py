def mixedletters(quant):
    for i in range(len(quant)):
        if quant[i].isalpha():
            return True
    return False