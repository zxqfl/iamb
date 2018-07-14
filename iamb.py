import re
import sys
import pytest

def strip_non_stress(pronunciation):
    return [c for c in pronunciation if c in "012"]

cached_stresses = None
def load_stresses():
    global cached_stresses # hack for fast tests
    if cached_stresses is not None:
        return cached_stresses
    result = {}
    for line in open("cmudict-0.7b", encoding="latin1"):
        if line.startswith(";;;"):
            continue
        word, stresses = line.split("  ")
        stresses = strip_non_stress(stresses)
        result[word] = stresses
    cached_stresses = result
    return result

def sound_out(*, stresses, token):
    if token in stresses or token.isdigit():
        return [token]
    else:
        return [c for c in token]

def split_token(*, stresses, token):
    result = token.split("_")
    result = [x.upper() for x in result]
    result = [x for x in result if len(x) >= 1]
    result = [part for token in result for part in sound_out(token=token, stresses=stresses)]
    return result

def test_split_token():
    stresses = load_stresses()
    assert split_token(token="foo_bar", stresses=stresses) == ["FOO", "BAR"]
    assert split_token(token="FOO_BAR", stresses=stresses) == ["FOO", "BAR"]
    assert split_token(token="QXPAZ", stresses=stresses) == ['Q', 'X', 'P', 'A', 'Z']
    assert split_token(token="11", stresses=stresses) == ["11"]

def basic_split(line):
    return re.findall("""[A-Za-z_0-9']+|[^\s]| """, line)

def tokenize(*, stresses, line):
    result = basic_split(line)
    result = [part for token in result for part in split_token(token=token, stresses=stresses)]
    return result

def test_tokenize():
    stresses = load_stresses()
    assert tokenize(line="int main_fun() {", stresses=stresses) == ["INT", " ", "MAIN", "FUN", '(', ')', ' ', '{']

def syllables_of_token(*, token, stresses):
    if token == "=":
        token = "EQUALS"
    if token == "-":
        token = "MINUS"
    if token == "+":
        token = "PLUS"
    if token == '"':
        token = "QUOTE"
    if token == '%':
        token = "PERCENT"
    if token == '33':
        return (syllables_of_token(token="THIRTY", stresses=stresses) +
                syllables_of_token(token="THREE", stresses=stresses))
    if len(token) == 1 and not token.isalpha():
        return []
    if token in stresses:
        return [(s, token) for s in stresses[token]]
    raise Exception("unrecognized token: " + token)

def is_valid_iamb(syllables):
    if syllables[-1][0] == '0': # this means unstressed in CMU dictionary
        return False
    syllables_ok = len(syllables) == 2
    if len(syllables) == 3 and syllables[-2][1] == "THE":
        syllables_ok = True
    if len(syllables) == 3 and syllables[0] == syllables[1] and syllables[0][0] == '0':
        syllables_ok = True
    return syllables_ok

def main(input_lines):
    stresses = load_stresses()
    for index, line in enumerate(input_lines):
        iambs = []
        def err(msg):
            msg = "on line {}: {}\niambs: {}\nthe line is: {}".format(index+1, msg, iambs, line)
            raise Exception(msg)
        tokens = tokenize(line=line, stresses=stresses)
        syllables = [s for token in tokens for s in syllables_of_token(stresses=stresses, token=token)]
        while syllables != []:
            ok = False
            for index in range(len(syllables), 0, -1):
                prefix = syllables[:index]
                suffix = syllables[index:]
                if is_valid_iamb(prefix):
                    iambs.append(prefix)
                    syllables = suffix
                    ok = True
                    break
            if not ok:
                base_tokens = [s[1] for s in syllables]
                tokens = []
                for t in base_tokens:
                    if tokens == [] or tokens[-1] != t:
                        tokens.append(t)
                err("no prefix of {} is an iamb".format(syllables))
        expected_iambs = 5
        if len(iambs) != expected_iambs and len(iambs) != 0:
            err("expected {} iambs, found {}".format(expected_iambs, len(iambs)))

def test_main():
    main([])
    main(["{}"])
    main(["But, soft! what light through yonder window breaks?"])
    with pytest.raises(Exception):
        main(["But, soft! what light through yonder window breaks, bro?"])
    with pytest.raises(Exception):
        main(open("test2.cpp"))
    main(open("test1.cpp"))

if __name__ == "__main__":
    main(sys.stdin)
