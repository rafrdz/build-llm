import re


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        # int_to_str is an inverse vocab that maps token IDs back to the original text tokens
        self.int_to_str = {i: s for s, i in vocab.items()}

    # Processes input text into token IDs
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int else "<|unk|>" for item in preprocessed
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    # Converts token IDs back into text
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!"()\'])', r"\1", text)
        return text
