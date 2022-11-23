import pickle
import os
import fugashi

from . import errors

"""
parse text

returns (sentence_structures, word_pool)
  sentence_structures: list of (feat, surface)
  pool: dict of {feat: set of (surface, raw_features)}

    feat: (elements[0]: 品詞, elements[1]: 詳しい品詞, elements[5]: 活用形)
    raw_features: str
    elements: raw_features.split(',')
"""
def parse(text, split_with_kuten=False):
    res_sentences = []
    parsing_sentence = []
    word_pool = {}

    tagger = fugashi.Tagger()

    for word in tagger(text):
        elements = word.feature_raw.split(",")
        feat = (elements[0], elements[1], elements[5])
        parsing_sentence.append((feat, word.surface))
        word_pool[feat] = word_pool.get(feat, set())
        word_pool[feat].add((word.surface, word.feature_raw))

        if split_with_kuten and elements[0] == '補助記号' and elements[1] == '句点':
            res_sentences.append(parsing_sentence)
            parsing_sentence = []

    if len(parsing_sentence) > 1:
        res_sentences.append(parsing_sentence)

    return(res_sentences, word_pool)

"""
make binary dump from text
"""
def parse_text_and_dump_data(input_path, pool_path, sentences_path, force=False):
    sentences = []
    word_pool = {}

    if os.path.isfile(pool_path) and not force:
        raise errors.FileAlreadyExistsException("%s already exists. If you want to overwrite, give -f or --force to command" % pool_path)

    if os.path.isfile(sentences_path) and not force:
        raise errors.FileAlreadyExistsException("%s already exists. If you want to overwrite, give -f or --force to command" % sentences_path)

    with open(input_path) as input_fp, open(pool_path, 'wb') as pool_fp, open(sentences_path, 'wb') as sentences_fp:
        for line in input_fp:
            (new_sentences, new_pool) = parse(line)
            sentences.extend(new_sentences)
            for k, v in new_pool.items():
                word_pool[k] = word_pool.get(k, set()) | v

        pickle.dump(word_pool, pool_fp)
        pickle.dump(sentences, sentences_fp)
