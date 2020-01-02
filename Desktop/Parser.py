import re

class Parser(object):
    @staticmethod
    def DeleteNonAlph(text):
        return re.sub("[^ \w]", "", text)

    @staticmethod
    def Tokenize(text):
        out = text.split()
        idx = 0
        while idx < len(out):
            if out[idx] == "":
                del out[idx]
            else:
                idx += 1
        return out

    @staticmethod
    def Lower(parsed_text):
        for i in range(len(parsed_text)):
            parsed_text[i] = parsed_text[i].lower()
        return parsed_text