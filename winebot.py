import random


def rand(options):
    return random.choice(options)


pairs_withs = [
    "allspice",
    "anise",
    "bananas",
    "bank holidays",
    "barbecue",
    "birthday cake",
    "black pepper",
    "brown salads",
    "cake",
    "cheap pasties",
    "cheese",
    "chicken",
    "chickens",
    "chili pepper",
    "cinnamon",
    "coq au vin",
    "crab & lobster",
    "cream pasta with chicken",
    "cream sauce",
    "cumin",
    "danger",
    "dispair",
    "dried fruit",
    "a duck",
    "duck",
    "easter eggs",
    "eggs",
    "fennel",
    "fried chicken",
    "fresh fruit",
    "fish and chips",
    "greek food",
    "green salads",
    "hamburgers",
    "hard cheeses",
    "a hearty casserole",
    "hearty vegetable soups",
    "ice cream",
    "indian cuisine",
    "ketchup",
    "KFC",
    "lasagna",
    "lebanese cuisine",
    "lilac salads",
    "McDonalds",
    "Mexican foods",
    "Monster Munch",
    "more wine",
    "mushroom risotto",
    "orange salads",
    "pesto",
    "pink salads",
    "pizza",
    "pungent cheeses",
    "Red Bull",
    "red meat",
    "roast pork",
    "roasted vegetables",
    "rosemary",
    "sausage rolls",
    "savory mushroom dishes",
    "smoked meats",
    "soft cheeses",
    "storm clouds",
    "sushi",
    "T-bone steaks",
    "tarragon chicken",
    "thai food",
    "turkish food",
    "vodka",
]

pairs_withs_1 = pairs_withs[:len(pairs_withs)//2]
pairs_withs_2 = pairs_withs[len(pairs_withs)//2:]

def pairs_with():
    return rand(pairs_with)

def pairs_with_1():
    return rand(pairs_withs_1)

def pairs_with_2():
    return rand(pairs_withs_2)


styles = [
    "achievable",
    "acidic",
    "adorable",
    "adventurous",
    "aggressive",
    "aggressive",
    "agreeable",
    "alcoholic",
    "alert",
    "alive",
    "amused",
    "angry",
    "annoyed",
    "annoying",
    "anxious",
    "approachable",
    "arrogant",
    "ashamed",
    "attractive",
    "average",
    "awful",
    "bad",
    "balanced",
    "baroque",
    "beautiful",
    "beautiful",
    "better",
    "bewildered",
    "big",
    "bitter",
    "black",
    "bloody",
    "blue-eyed",
    "blue",
    "blushing",
    "bold",
    "bored",
    "brainy",
    "brambly",
    "brave",
    "breakable",
    "bright",
    "brutal",
    "busy",
    "calm",
    "careful",
    "cautious",
    "charming",
    "cheerful",
    "clammy",
    "clean",
    "clean",
    "clear",
    "clever",
    "cloudy",
    "clumsy",
    "colorful",
    "combative",
    "comfortable",
    "comforting",
    "complex",
    "concerned",
    "condemned",
    "confused",
    "conniving",
    "cooperative",
    "courageous",
    "crazy",
    "creepy",
    "crisp",
    "crispy",
    "crowded",
    "cruel",
    "curious",
    "cute",
    "dangerous",
    "dark",
    "dead",
    "deceptive",
    "deep-rooted",
    "defeated",
    "defiant",
    "delightful",
    "delightful",
    "dependable",
    "depressed",
    "determined",
    "different",
    "difficult",
    "dirty",
    "disastrous",
    "disgusted",
    "disheveled",
    "distinct",
    "disturbed",
    "dizzy",
    "doubtful",
    "drab",
    "drinkable",
    "dry",
    "dull",
    "eager",
    "earthy",
    "easy-drinking",
    "easy",
    "elated",
    "elegant",
    "embarrassed",
    "enchanting",
    "encouraging",
    "energetic",
    "enthusiastic",
    "envious",
    "evil",
    "excited",
    "expensive",
    "exuberant",
    "fabulous",
    "fair",
    "faithful",
    "famous",
    "fancy",
    "fantastic",
    "feral",
    "ferocious",
    "fierce",
    "filthy",
    "fine",
    "foolish",
    "fragile",
    "frail",
    "frantic",
    "fresh",
    "friendly",
    "frightened",
    "full-bodied",
    "full-flavoured",
    "funny",
    "gentle",
    "gifted",
    "glamorous",
    "gleaming",
    "glorious",
    "good",
    "gorgeous",
    "graceful",
    "grape-flavoured",
    "great value",
    "grieving",
    "grotesque",
    "grumpy",
    "handsome",
    "happy",
    "harmful",
    "harmonious",
    "harsh",
    "healthy",
    "helpful",
    "helpless",
    "high-end",
    "hilarious",
    "homeless",
    "homely",
    "horrible",
    "hot",
    "hungry",
    "hurt",
    "hypnotic",
    "ill",
    "important",
    "impossible",
    "incredible",
    "inexpensive",
    "inky",
    "innocent",
    "inquisitive",
    "intense",
    "interesting",
    "itchy",
    "jammy",
    "jealous",
    "jittery",
    "jolly",
    "joyous",
    "judgmental",
    "kind",
    "kinky",
    "layered",
    "lazy",
    "legit",
    "light-bodied",
    "light",
    "lingering",
    "liquor-ish",
    "lively",
    "lonely",
    "long",
    "lovely",
    "lucky",
    "lurking",
    "magnificent",
    "majestic",
    "misty",
    "modern",
    "modern",
    "moreish",
    "motionless",
    "muddy",
    "muddy",
    "mushy",
    "mysterious",
    "nasty",
    "naughty",
    "nervous",
    "nice",
    "nicely integrated",
    "nutty",
    "obedient",
    "obnoxious",
    "odd",
    "old-fashioned",
    "ominous",
    "open",
    "outrageous",
    "outstanding",
    "overrated",
    "panicky",
    "perfect",
    "plain",
    "pleasant",
    "plush",
    "poised",
    "poor",
    "powerful",
    "precious",
    "present",
    "prickly",
    "proud",
    "putrid",
    "puzzled",
    "quaint",
    "real",
    "relieved",
    "repulsive",
    "resentful",
    "rich",
    "rich",
    "ripe",
    "ritualistic",
    "savoury",
    "scary",
    "selfish",
    "shiny",
    "shy",
    "silly",
    "sleepy",
    "slightly out of the ordinary",
    "smiling",
    "smoggy",
    "snappy",
    "soft",
    "sore",
    "sparkling",
    "spiritual",
    "splendid",
    "spotless",
    "stormy",
    "strange",
    "stupid",
    "successful",
    "super",
    "supple",
    "sweaty",
    "swift",
    "talented",
    "tame",
    "tart",
    "tasty",
    "tender",
    "tense",
    "terrible",
    "textbook",
    "thankful",
    "thoughtful",
    "thoughtless",
    "tired",
    "totally legal",
    "tough",
    "troubled",
    "turgid",
    "ugliest",
    "ugly",
    "unbalanced",
    "uncivilised",
    "undrinkable",
    "uninterested",
    "unjudgemental",
    "unsightly",
    "unstructured",
    "unusual",
    "upset",
    "uptight",
    "vast",
    "victorious",
    "vivacious",
    "wandering",
    "warm",
    "weary",
    "wet",
    "wicked",
    "wide-eyed",
    "wild",
    "wine-like",
    "witty",
    "worried",
    "worrisome",
    "wrong",
    "zany",
    "zealous",
]

styles_1 = styles[:len(styles)//2]
styles_2 = styles[len(styles)//2:]

def style():
    return rand(style)

def style_1():
    return rand(styles_1)

def style_2():
    return rand(styles_2)


def wine_type():
    return rand([
        "Cabernet Sauvignon",
        "Chardonnay",
        "Malbec",
        "Merlot",
        "Monastrell",
        "Petit Sirah",
        "Pinot Grigio",
        "Pinot Gris",
        "Pinot Noir",
        "Pinotage",
        "Riesling",
        "Rosé",
        "Sauvignon Blanc",
        "Schiava",
        "Sémillon",
        "Shiraz",
        "Syrah",
        "Viognier",
        "Zinfandel",
    ])


hints = [
    "a whiff",
    "bits",
    "evidence",
    "hints",
    "implications",
    "inklings",
    "memories",
    "mentions",
    "notes",
    "signs",
    "suggestions",
    "suspicions",
    "tinges",
    "traces",
    "whispers",
]

hints_1 = hints[:len(hints)//2]
hints_2 = hints[len(hints)//2:]

def hint():
    return rand(hints)

def hint_1():
    return rand(hints_1)

def hint_2():
    return rand(hints_2)

notes = [
    "apple",
    "ash",
    "bacon",
    "baked potatoes",
    "banana",
    "beans",
    "black cherry",
    "black current",
    "blackberry",
    "bleach",
    "blueberry",
    "brick",
    "butter",
    "camomile",
    "caramel",
    "cats",
    "cedar spice",
    "chalk",
    "cherry",
    "Chewits®",
    "chlorine",
    "chocolate",
    "cigars",
    "cigar box",
    "coffee",
    "cola",
    "cocaine",
    "coconut",
    "citrus",
    "cranberry",
    "durian",
    "denim",
    "drains",
    "elderflower",
    "fags",
    "fennel",
    "fireworks",
    "floral aromatics",
    "Freddos",
    "gunpowder",
    "hibiscus",
    "hobnobs",
    "hot cross buns",
    "lavendar",
    "Listerine",
    "liquorice",
    "lutefisk",
    "lychee",
    "miso",
    "moss",
    "noodles",
    "oak barrels",
    "olive",
    "onion",
    "orange",
    "ozone",
    "passion fruit",
    "peach",
    "peat",
    "plum",
    "poptarts",
    "pub floor",
    "raspberry",
    "red fruit",
    "rhubarb",
    "roast mushrooms",
    "sadness",
    "sashimi",
    "slate",
    "soy sauce",
    "spices",
    "summer fruits",
    "surströmming",
    "swede",
    "Tizer",
    "toast",
    "tobacco",
    "tofu",
    "toothpaste",
    "turnip",
    "vanilla",
    "velvet",
    "war crimes",
    "wellies",
    "wet dogs",
    "wood",
    "woody herbs",
]

notes_1 = notes[:len(notes)//2]
notes_2 = notes[len(notes)//2:]

def note():
    return rand(note)

def note_1():
    return rand(notes_1)

def note_2():
    return rand(notes_2)


def smell():
    return rand([
        "a both good and bad",
        "a bewildering",
        "a darkly humerous",
        "a dense, almost foggy",
        "a frankly misleading",
        "a gloomily tainted",
        "a mischievous",
        "a mysterious",
        "a sickeningly sweet",
        "a somehow smug",
        "a somewhat sickening",
        "a strangely pompous",
        "a subtly vinegary",
        "a surprisingly erotic",
        "a surruptitious",
        "a thick, secretive",
        "a thoroughly unpleasant",
        "a throat-tickling",
        "a tough",
        "a turbulent",
        "a twisted",
        "an exagerated",
        "an exaustingly energetic",
        "an exuberant",
        "an honestly quite unnerving",
        "an optimistically old-fashioned",
        "an overbearing",
        "an uninviting",
        "an underhanded",
        "an unethical",
    ])


def sentence():
    return " ".join([
        "This",
        style_1(),
        "and",
        style_2(),
        wine_type(),
        "has",
        hint(),
        "of",
        note_1(),
        "and",
        note_2() + ",",
        "with",
        smell(),
        rand([
            "aroma",
            "smell",
            "texture",
            "appearance",
        ]) + ".",
        "Pairs well with",
        pairs_with_1(),
        "or",
        pairs_with_2(),
    ]) + "."
