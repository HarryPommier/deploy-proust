import os
import io
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json


class Model:
    def __init__(self, model_path: str=None, tokenizer_path:str=None):
        self._model = None
        self._tokenizer = None
        self._model_path = model_path
        self._tokenizer_path = tokenizer_path
        self.load_model()
        self.load_tokenizer()

    def load_model(self):
        try:
            self._model = load_model(self._model_path)
        except Exception as e:
            print("Model.load_model() failed. Error: {}".format(e))
            self._model = None
        return self

    def load_tokenizer(self):
        try:
            with io.open(tokenizer_path) as f:
                json_string = json.load(f)
                self._tokenizer = tokenizer_from_json(json_string)
        except Exception as e:
            print("Model.load_tokenizer() failed. Error: {}".format(e))
        return self

    def generate_text(self, seed_text: str=None):
        try:
            output_word = ""
            while output_word != ".":
                token_list = self._tokenizer.texts_to_sequences([seed_text])[0]
                token_list = pad_sequences([token_list], maxlen=49, padding='pre')
                predicted = self._model.predict_classes(token_list, verbose=0)
                output_word = ""
                for word, index in self._tokenizer.word_index.items():
                    if index == predicted:
                        output_word = word
                        break
                if output_word != ".":
                    seed_text += " " + output_word
                else:
                    seed_text += output_word
        except Exception as e:
            print(e)
        return seed_text

model_path = os.path.join("saved_model", "model_proust_generator")
tokenizer_path = os.path.join("saved_model", "tokenizer","tokenizer.json")
model = Model(model_path, tokenizer_path)
