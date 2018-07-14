from iamb import tokenize, load_stresses, syllables_of_token, split_token, basic_split
from phrases import phrase_for
import sys
import re

def to_syllables(*, token, stresses):
    token = split_token(token=token, stresses=stresses)
    return [s for token in token for s in syllables_of_token(token=token, stresses=stresses)]

INFINITY = 1_000_000_000
def main(input_lines):
    if type(input_lines) == str:
        input_lines = [input_lines]
    new_input_lines = []
    for x in input_lines:
        if "#" in x:
            print(x, end='')
        else:
            new_input_lines.append(x)
    stresses = load_stresses()
    tokens = [x for line in new_input_lines for x in basic_split(line)]
    syllables = [to_syllables(token=token, stresses=stresses) for token in tokens]
    cache = {}
    line_end = 10
    def rec(index, posn_in_line):
        key = (index, posn_in_line)
        if key in cache:
            return cache[key]
        prepend = []
        while index < len(syllables) and len(syllables[index]) == 0:
            prepend.append(tokens[index])
            index += 1
        assert index <= len(syllables)
        if index == len(syllables) and posn_in_line == line_end:
            return 0, prepend
        if posn_in_line == line_end:
            prepend.append("\n")
            posn_in_line = 0
        best = INFINITY, []
        cache[key] = best
        is_first_syllable_stressed = posn_in_line % 2 == 1
        for new_posn in range(posn_in_line+1, line_end+1):
            sub_cost, sub_soln = rec(index, new_posn)
            sub_cost += new_posn - posn_in_line + 1
            if sub_cost < best[0]:
                sub_soln = [phrase_for(posn_in_line = posn_in_line,
                                       num_syllables = new_posn - posn_in_line,
                                       is_first_syllable_stressed = is_first_syllable_stressed)] + sub_soln
                best = sub_cost, sub_soln
        if index < len(syllables):
            cost_now = 0
            can_go_now = True
            for syl_index, syl in enumerate(syllables[index]):
                is_supposed_to_be_stressed = (syl_index + posn_in_line) % 2 == 1
                if syl_index + posn_in_line >= line_end:
                    can_go_now = False
                if is_supposed_to_be_stressed and syl[0] == '0':
                    cost_now += 100
                if is_supposed_to_be_stressed and syl[0] == '2':
                    cost_now += 2
                if len(syllables[index]) >= 3 and syl[0] == '1' and not is_supposed_to_be_stressed:
                    cost_now += 100
            if can_go_now:
                sub_cost, sub_soln = rec(index+1, posn_in_line + len(syllables[index]))
                sub_cost += cost_now
                if sub_cost <= best[0]:
                    sub_soln = [tokens[index]] + sub_soln
                    best = sub_cost, sub_soln
        best = best[0], prepend + best[1]
        cache[key] = best
        return best
    for i in range(len(syllables), 0, -1):
        rec(i, 0)
    cost, solution = rec(0, 0)
    if cost == INFINITY:
        raise Exception("no solution")
    return cost, solution

def test_main():
    assert main("to be or not to be")[1][:-1] == [
        "to", " ",
        "be", " ",
        "or", " ",
        "not", " ",
        "to", " ",
        "be"]

if __name__ == "__main__":
    cost, result = main(sys.stdin)
    print("cost:", cost, file=sys.stderr)
    prev = None
    for x in result:
        if type(x) != str:
            x = x[1]
        if x != prev or x != " ":
            sys.stdout.write(x)
        prev = x
    sys.stdout.write('\n')

