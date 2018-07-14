from iamb import tokenize
from phrases import phrase_for

def main(input_lines):
    tokens = [token for line in input_lines for token in tokenize(line)]
    syllables = [s for token in tokens for s in syllables_of_token(stresses=stresses, token=token)]
    cache = {}
    line_end = 10
    def rec(index, posn_in_line):
        if index == len(syllables) and posn_in_line == line_end:
            return 0, []
        if posn_in_line == line_end:
            posn_in_line = 0
        key = (index, posn_in_line)
        if key in cache:
            return cache[key]
        # TODO

if __name__ == "__main__":
    main(sys.stdin)
