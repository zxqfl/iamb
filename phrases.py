import random

# Phrases that end the line
end_phrases = {
    1: [
        "made",
        "found",
        "caught",
        "seen",
        "torn",
        "hark!",
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
        "noble Feridun",
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
        "where is the lamb sauce"
    ],
    6: [
        "as boundless as the sea",
        "the darling buds of May",
        "eternal light prevails",
        "thou art a fishmonger",
    ],
    7: [
        "through the mist and fog light shines",
        "soaring through the sky a soul",
        "dancing o'er an empty lake",
    ],
    8: [
        "forever and forever still",
        "nor reason can my passion hide",
        "of gods and men this tale unfolds",
        "by mountains set aflame by morn",
    ],
    9: [
        "- words as sweet as honey seems to bees"
    ],
    10: [
        "Mysterious as the dark side of the moon",
        "Love is a spirit all compact of fire",
        "If music be the food of love, play on",
        "A song that lulls the heart ignites truth love",
    ]
}

def pick_random(array):
    return array[random.randint(0, len(array) - 1)]

def phrase_for(*, posn_in_line, num_syllables, is_first_syllable_stressed):
    return " /* " + pick_random(end_phrases[num_syllables]) + " */ "
