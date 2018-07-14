import re
import sys
import pytest

def strip_non_stress(pronunciation):
    return [c for c in pronunciation if c in "012"]

def load_stresses():
    result = {}
    for line in open("cmudict-0.7b", encoding="latin1"):
        if line.startswith(";;;"):
            continue
        word, stresses = line.split("  ")
        stresses = strip_non_stress(stresses)
        result[word] = stresses
    return result

def split_token(token):
    result = token.split("_")
    result = [x.upper() for x in result]
    result = [x for x in result if len(x) >= 1]
    return result

def test_split_token():
    assert split_token("foo_bar") == ["FOO", "BAR"]
    assert split_token("FOO_BAR") == ["FOO", "BAR"]

def tokenize(line):
    result = re.findall("""[A-Za-z_]+|[^\s]""", line)
    result = [part for token in result for part in split_token(token)]
    return result

def test_tokenize():
    assert tokenize("int main_fun() {") == ["INT", "MAIN", "FUN", '(', ')', '{']

def syllables_of_token(*, token, stresses):
    if token in stresses:
        return stresses[token]
    if len(token) == 1 and not token.isalpha():
        return []
    raise Exception("unrecognized token: " + token)

def main(input_lines):
    stresses = load_stresses()
    for index, line in enumerate(input_lines):
        def err(msg):
            msg = "on line {}: {}\nthe line is: {}".format(index+1, msg, line)
            raise Exception(msg)
        tokens = tokenize(line)
        syllables = [s for token in tokens for s in syllables_of_token(stresses=stresses, token=token)]
        if syllables == []:
            continue
        expected_syllables = 10
        if len(syllables) != expected_syllables:
            err("expected {} syllables, found {}".format(expected_syllables, len(syllables)))

def test_main():
    main([])
    main(["{}"])
    main(["But, soft! what light through yonder window breaks?"])
    main(["But, soft! what light through yonder windo0w breaks, bro?"])

if __name__ == "__main__":
    main(sys.stdin)
