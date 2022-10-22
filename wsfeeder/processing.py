import random
import pickle

def process(pool, sentence):
    res = ""
    for (feat, raw) in sentence:
        if feat[0] in ('助詞', '助動詞'):
            res += raw
        else:
            res += random.choice(list(pool[feat]))[0]
    return res

def process_sentences_from_dump(pool_path, sentences_path, number=0, randomize_sentences_order=True):
    with open(pool_path, 'rb') as pool_fp, open(sentences_path, 'rb') as sentences_fp:
        pool = pickle.load(pool_fp)
        sentences = pickle.load(sentences_fp)

    res_sentences = []

    if randomize_sentences_order:
        random.shuffle(sentences)

    if n == 0:
        n = len(sentences)
    n = min(n, len(sentences))

    for i in range(n):
        sentence = sentences[i]
        res_sentences.append(process(pool, sentence))

    return res_sentences
