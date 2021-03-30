def tap_code_translation(text):
    new_dict={"a":". .", "b":". ..", "c":". ...", "k":". ...", "d":". ....", "e":". .....",
             "f":".. .", "g":".. ..", "h":".. ...", "i":".. ....", "j":".. .....",
             "l":"... .", "m":"... ..", "n":"... ...", "o":"... ....", "p":"... .....",
             "q":".... .", "r":".... ..", "s":".... ...", "t":".... ....", "u":".... .....",
             "v":"..... .", "w":"..... ..", "x":"..... ...", "y":"..... ....", "z":"..... ....."}
#     return list(text)
#     a = list(text)
#     b = str(a)
    c = []
    for i in range(0, len(text)):
        for key, value in new_dict.items():
            if text[i] in key:
                c.append(value)
    return ' '.join(c)