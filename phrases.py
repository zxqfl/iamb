import random

# Phrases that end the line
end_phrases = {
    1: [
        "made",
        "found",
        "caught",
        "seen",
        "torn",
        "proved"
        "loved",
        "pure",
        "white",
    ],
    2: [
        "golden",
        "still dark",
        "bloodstained",
        "sun soaked",
        "afoot",
        "of gods",
        "primrose",
        "bedazzled",
    ],
    3: [
        "sick at heart",
        "seemeth pure",
        "rose distill'd",
        "heart assured",
        "noble Feridun"
        "beauteous geese",
    ],
    4: [
        "surmounted high",
        "noble and valiant",
        ", a sorry sight",
        "of naked truth",
        "in one fell swoop",
        "from jaws of death",
        "beauty untrimm'd",
    ],
    5: [
        "with surcease success",
        "love as swift as thought",
        "o're the castle flew",
    ],
    6: [
        "as boundless as the sea",
        "thy eternal summer",
        "the darling buds of May",
    ],
    7: [
        "nor reason can my passion hide",
    ]
}

def pick_random(array):
    return array[random.randint(0, len(array) - 1)]

def phrase_for(*, posn_in_line, num_syllables, is_first_syllable_stressed):
    return pick_random(end_phrases[num_syllables])
