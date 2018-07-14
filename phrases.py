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
        "words as sweet as honey seems to bees",
        "winds of summer air bring boundless love"
        "hath taught me thus to ruminate",
        "though mine own love’s strength seems to decay",
        "love a spirit all compact of fire",
    ],
    10: [
        "Mysterious as the dark side of the moon",
        "Love is a spirit all compact of fire",
        "If music be the food of love, play on",
        "A song that lulls the heart ignites truth love",
        "Against the stormy gusts of winter’s day",
    ]
}

start_phrases = {
    1: [
        "The",
        "First",
        "Find",
        "See"
    ],
    2: [
        "Behold",
        "See the",
        "Regard",
        "Destroy",
        "Toward",
        "Abound",
    ],
    3: [
        "Now hear me:",
        "To find a",
        "Searching for",
        "For seeking",
        "Forsooth my",
        "Regaling for",
    ],
    4: [
        "To say the least",
        "Love is my sin",
        "O, know, sweet love",
        "To thee I say",
        "Upon my word",
    ],
    5: [
        "The beauty of this",
        "My love is for the",
        "My heart yearns for the",
        "For fantasy begs",
        "From heaven sent a",
        "And yet, by heaven",
    ],
    6: [
        "To be or not to be",
        "Whilst I, my sovereign, watch",
        "And buds of marjoram had",
        "I have seen roses damask’d",
    ],
    7: [
        "Yet so they mourn becoming",
        "And fortify yourself with",
        "Without accusing you of",
        "Love’s eye is not so true as",
    ],
    8: [
        "I never saw a goddess say",
        "Such civil war is in my heart",
        "If Time have any wrinkle then"
    ],
    9: [
        "Without all ornament, itself and",
        "Such civil war is in my heart and",
        "To let base clouds o’ertake me in my",
        "And yet, by heaven, I think my love as",
    ]
}

mono_syllabic_words = ["the", "of", "to", "from", "sees"]

inner_phrases = {
    "stressed": {
        1: mono_syllabic_words,
        2: [
            "final",
            "seeking",
            "finding",
            "loving",
            "hating",
            "seeing",
            "broken",
            "shattered",
            "struck down",
            "cast down",
            "vanquished"
        ],
        3: [
            "treason then",
            "misfortune",
            "fortunate",
            "loving smile",
            "sinful smile",
            "lavendar",
            "summer sound",
            "honey sweet",
        ],
        4: [
            "king and country",
            "roads to heaven",
            "seething anger",
            "painful message",
        ],
        5: [
            "such profound abysm",
            "that which still doth grow",
            "to myself I'll vow",
            "without words' despair",
        ],
        6: [
            "moan the expense of many",
            "producing dust therein",
            "counter to creation",
            "loving the abation",
            "harmony in music"
        ],
        7: [
            "old to dress his beauty new",
            "part of which I cannot know",
            "those under the dreaded sea",
            "cannot fathom summer's draw"
        ],
    },
    "unstressed": {
        1: mono_syllabic_words,
        2: [
            "behold",
            "succeed",
            "destroy",
            "abound",
            "amock",
            "proves real",
            "makes good",
            "perplexed",
        ],
        3: [
            "to see a",
            "a mix of",
            "unbounded",
            "created",
            "destroyed",
            "contrited",
        ],
        4: [
            "escaping death"
            "a flurry of",
            "the gears of war",
            "with love as rare",
            "like raven black",
            "with gentle gait",
            "dear virtue hate",
        ],
        5: [
            "You note a message",
            "In deep abysm",
            "In deadly waters",
            "To give full growth to",
            "What means the world to"
        ],
        6: [
            "Without all ornament",
            "Thus policy in love",
        ],
        7: [
            "O let me, true in love, write",
        ],
        8: [
            "For thee against myself I'll fight"
        ],
    }
}


def pick_random(array):
    return array[random.randint(0, len(array) - 1)]

def phrase_for(*, posn_in_line, num_syllables, is_first_syllable_stressed):
    if num_syllables >= 10 - posn_in_line + 1:
        # We need the rest of the line
        return pick_random(end_phrases[num_syllables])
    elif posn_in_line == 0:
        return pick_random(start_phrases[num_syllables])
    return pick_random(inner_phrases["stressed" if is_first_syllable_stressed else "unstressed"][num_syllables])
