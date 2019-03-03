# cmudict.dict: big dictionary of pronunciatinos
# cmudict.phones # phoneme classification
# cmudict.symbols # uselsss set of phonemes
# cmudict.vp

# p2c = phoneme to classification
# c2pl = classification to phoneme-list

from collections import defaultdict
nested_dict = lambda: defaultdict(nested_dict)

import re
non_letters_re = re.compile(r"[^A-Z]+")

DEFAULT_DICT = "cmudict.dict"
DEFAULT_CLASSIFICATION = "cmudict.phones"

class CanEndHereClass(object):
    def __repr__(self):
        return "END"
CanEndHere = CanEndHereClass()

def clean_phoneme(phoneme):
    return non_letters_re.sub("", phoneme).strip()

def load_classifications(fname):
    p2c = {}
    c2pl = defaultdict(list)
    with open(fname) as f:
        for line in f:
            if '\t' in line:
                line = line.rstrip()
                phoneme, classification = line.split('\t', 1)
                p2c[phoneme] = classification
                c2pl[classification].append(phoneme)
    return p2c, c2pl

def load_dict(fname, p2c):
    forward = defaultdict(list)
    backward = nested_dict()
    with open(fname) as f:
        for line in f:
            word, pronunciation = line.split(None, 1)
            if "." in word or not word[:1].isalpha():
                # avoid punctuation and contractions
                continue
            # altarnate pronuciations have "(n)" after
            word, _, _ = word.partition('(')
            word = word.strip().upper()
            pronunciation, _, _ = pronunciation.partition("#")
            pronunciation = tuple(
                clean_phoneme(phoneme)
                for phoneme
                in pronunciation.strip().split()
                )
            forward[word].append(pronunciation)
            cur = backward
            for phoneme in pronunciation:
                cur = cur[phoneme]
            if CanEndHere in cur:
                cur[CanEndHere].append(word)
            else:
                cur[CanEndHere] = [word]
    return forward, backward

def phoneme_iter(
        forward,
        words,
        ):
    if words:
        remaining_words = list(words)
        word = remaining_words.pop(0)
        for pronunciation in forward[word]:
            for rest in phoneme_iter(forward, remaining_words):
                yield pronunciation + rest
    else:
        yield tuple()

def find_puns(
        original_backward,
        backward,
        p2c, # pronunciation-to-classification dict
        c2pl, # classification-to-pronunciatino-list
        stream,
        so_far=None,
        fudge=False,
        fudged=False,
        ):
    if so_far is None:
        so_far = []
    if stream:
        first = stream[0]
        candidate_phonemes = [first]
        if fudge and not fudged:
            candidate_phonemes.extend(c2pl[p2c[first]])
            fudged = True
        candidate_phonemes.sort()
        for phoneme_to_check in candidate_phonemes:
            if phoneme_to_check in backward:
                new_backward = backward[phoneme_to_check]
                if CanEndHere in new_backward:
                    candidates = "{%s}" % (",".join(new_backward[CanEndHere]))
                    for result in find_puns(
                            original_backward,
                            original_backward,
                            p2c,
                            c2pl,
                            stream[1:],
                            so_far + [candidates],
                            fudge=fudge,
                            fudged=fudged or phoneme_to_check != first,
                            ):
                        yield result
                for result in find_puns(
                        original_backward,
                        backward[phoneme_to_check],
                        p2c,
                        c2pl,
                        stream[1:],
                        so_far,
                        fudge=fudge,
                        fudged=fudged or phoneme_to_check != first,
                        ):
                    yield result
    elif CanEndHere in backward:
        candidates = "{%s}" % (",".join(backward[CanEndHere]))
        yield so_far + [candidates]

if __name__ == "__main__":
    from pprint import pprint
    import argparse
    import sys
    import logging
    log = logging.getLogger(__file__)
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(
        description="Find phonetic word-plays based on input phrases",
        )
    parser.add_argument("-f", "--fudge",
        action="store_true",
        help="Fudge the sounds phonetically",
        )
    parser.add_argument("-d", "--dictionary",
        metavar="FILE",
        action="store",
        help="CMU-format dictionary file (default=%s)" % DEFAULT_DICT,
        default=DEFAULT_DICT,
        )
    parser.add_argument("-c", "--classifications",
        metavar="FILE",
        action="store",
        help="CMU-format phoneme-classification file (default=%s)" %
            DEFAULT_CLASSIFICATION,
        default=DEFAULT_CLASSIFICATION,
        )
    parser.add_argument("phrases",
        metavar="WORDS",
        type=str,
        nargs="+",
        help="Phrases to riff on",
        )
    args = parser.parse_args()
    if args.fudge:
        log.debug("Fudging")
        # don't need to bother loading these
        # unless we're fudging the sounds
        log.info("Loading classifications from %s", args.classifications)
        p2c, c2pl = load_classifications(args.classifications)
    else:
        p2c = c2pl = {}
    log.info("Loading dictionary from %s", args.dictionary)
    forward, backward = load_dict(args.dictionary, p2c)
    log.info("Loaded %i words", len(forward))
    output_set = set()
    for phrase in args.phrases:
        phrase = phrase.upper()
        for stream in phoneme_iter(forward, phrase.split()):
            for pun in find_puns(
                    backward,
                    backward,
                    p2c,
                    c2pl,
                    stream,
                    fudge=args.fudge,
                    ):
                output = " ".join(w.lower() for w in pun)
                if output not in output_set:
                    output_set.add(output)
                    print(output)
