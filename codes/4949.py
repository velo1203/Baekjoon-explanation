


txts = []
while True:
    txt = input()
    if txt == ".":
        break

    txts.append(txt)


for t in txts:
    sentence= []

    for w in t:
        if w == "(" or w == ")" or w == "[" or w == "]":
            sentence.append(w)

    sen = []
    for idx,s in enumerate(sentence):
        if s == "(" or s == "[":
            sen.append(s)
        elif len(sen)!= 0 and (sen == ")" or "]"):
            if s == ")" and  sen[-1] == "(":
                sen.pop()
            elif s == "]" and sen[-1] == "[":
                sen.pop()
            else:
                break
        else:
            sen.append(s)
    if len(sen) == 0:
        print("yes")
    else:
        print('no')