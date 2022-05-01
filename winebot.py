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
    "easter eggs",
    "fennel",
    "fried chicken",
    "fish and chips",
    "greek food",
    "green salads",
    "hamburgers",
    "hard cheeses",
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
    "aggressive",
    "alcoholic",
    "balanced",
    "baroque",
    "bitter",
    "brutal",
    "clammy",
    "clean",
    "complex",
    "conniving",
    "crisp",
    "crispy",
    "deceptive",
    "delightful",
    "dirty",
    "disheveled",
    "dry",
    "earthy",
    "feral",
    "ferocious",
    "full-bodied",
    "grape-flavoured",
    "harmonious",
    "harsh",
    "hypnotic",
    "judgmental",
    "kinky",
    "layered",
    "legit",
    "lingering",
    "lurking",
    "muddy",
    "nicely integrated",
    "ominous",
    "overrated",
    "resentful",
    "rich",
    "ripe",
    "sweaty",
    "swift",
    "tart",
    "turgid",
    "totally legal",
    "unbalanced",
    "uncivilised",
    "unstructured",
    "unjudgemental",
    "wet",
    "wine-like",
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
    "black current",
    "blackberry",
    "bleach",
    "blueberry",
    "brick",
    "butter",
    "camomile",
    "caramel",
    "cats",
    "chalk",
    "Chewits®",
    "chlorine",
    "cigars",
    "coffee",
    "cola",
    "cocaine",
    "citrus",
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
    "lutefisk",
    "lychee",
    "miso",
    "moss",
    "noodles",
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
    "rhubarb",
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
