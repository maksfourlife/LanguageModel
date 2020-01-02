import random as rn
import pickle as pc
from Parser import Parser

class Model(object):
    word_pairs = {}

    def save(self, filepath_n_name):
        with open((filepath_n_name + ".tmodel") if len(filepath_n_name.split(".")) == 1 else filepath_n_name, "wb") as f:
            pc.dump(self.word_pairs, f, pc.HIGHEST_PROTOCOL)

    def load(self, filepath_n_name):
        try:
            with open((filepath_n_name + ".tmodel") if len(filepath_n_name.split(".")) == 1 else filepath_n_name, "rb") as f:
                self.word_pairs = pc.load(f)
        except Exception:
            print("Не удалось найти файл")

    def fit(self, text: str):
        parsed_text = Parser.Lower(Parser.Tokenize(Parser.DeleteNonAlph(text)))
        for i in range(len(parsed_text) - 1):
            if not parsed_text[i] in self.word_pairs:
                self.word_pairs[parsed_text[i]] = [parsed_text[i + 1]]
            else:
                self.word_pairs[parsed_text[i]].append(parsed_text[i + 1])

    def generate(self, state: str, length: int):
        if not self.word_pairs or not state in self.word_pairs:
            return print("Данного слова нет в списке")
        out = state
        i = 1
        while i < length:
            choice = rn.choice(self.word_pairs[state])
            out += " {}".format(choice)
            state = choice
            i += 1
        return out

    def __del__(self):
        self.save("last.tmodel")

    def words(self):
        return self.word_pairs.keys()