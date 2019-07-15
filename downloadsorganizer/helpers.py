def pretty_print(text):
    box = "+" + "-" * (len(text)) + "+" + "\n"
    box += "|" + text + "|" + "\n"
    box += "+" + "-" * (len(text)) + "+" + "\n"
    print(box)

