from tamil import utf8


data_dict ={

# English Letters
    "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g",
    "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n",
    "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u",
    "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",

# NUMBERS
    "1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
    "6": "6", "7": "7", "8": "8", "9": "9", "0": "0",

# Tamil letters
"அ": "a", "ஆ": "aa", "இ": "i", "ஈ": "ii", "உ": "u", "ஊ": "uu", "எ": "e", "ஏ": "ee", "ஐ": "ai", "ஒ": "o", "ஓ": "oo", "ஔ": "au",

"க்": "k", "ங்": "n", "ச்": "c", "ஞ்": "n", "ட்": "t", "ண்": "n", "த்": "p", "ம்": "m", "ய்": "y",
"ர்": "r", "ல்": "l", "வ்": "v", "ழ்": "l", "ள்": "l", "ற்": "r", "ன்": "n",

"க": "ka", "கா": "kaa", "கி": "ki", "கீ": "kii", "கு": "ku", "கூ": "kuu", "கெ": "ke", "கே": "kee", "கை": "kai", "கொ": "ko", "கோ": "koo", "கௌ": "kau",
"ங": "na", "ஙா": "naa", "ஙி": "ni", "ஙீ": "nii", "ஙு": "nu", "ஙூ": "nuu", "ஙெ": "ne", "ஙே": "nee", "ஙை": "nai", "ஙொ": "no", "ஙோ": "noo", "ஙௌ": "nau",
"ச": "ca", "சா": "caa", "சி": "ci", "சீ": "cii", "சு": "cu", "சூ": "cuu", "செ": "ce", "சே": "cee", "சை": "cai", "சொ": "co", "சோ": "coo", "சௌ": "cau",
"ஞ": "na", "ஞா": "naa", "ஞி": "ni", "ஞீ": "nii", "ஞு": "nu", "ஞூ": "nuu", "ஞெ": "ne", "ஞே": "nee", "ஞை": "nai", "ஞொ": "no", "ஞோ": "noo", "ஞௌ": "nau",
"ட": "ta", "டா": "taa", "டி": "ti", "டீ": "tii", "டு": "tu", "டூ": "tuu", "டெ": "te", "டே": "tee", "டை": "tai", "டொ": "to", "டோ": "too", "டௌ": "tau",
"ண": "na", "ணா": "naa", "ணி": "ni", "ணீ": "nii", "ணு": "nu", "ணூ": "nuu", "ணெ": "ne", "ணே": "nee", "ணை": "nai", "ணொ": "no", "ணோ": "noo", "ணௌ": "nau",
"த": "tha", "தா": "tha", "தி": "thi", "தீ": "thii", "து": "thu", "தூ": "thuu", "தெ": "the", "தே": "thee", "தை": "thai", "தொ": "tho", "தோ": "thoo", "தௌ": "thau",
"ந": "na", "நா": "na", "நி": "ni", "நீ": "nii", "நு": "nu", "நூ": "nuu", "நெ": "ne", "நே": "nee", "நை": "nai", "நொ": "no", "நோ": "noo", "நௌ": "nau",
"ப": "pa", "பா": "paa", "பி": "pi", "பீ": "pii", "பு": "pu", "பூ": "puu", "பெ": "pe", "பே": "pee", "பை": "pai", "பொ": "po", "போ": "poo", "பௌ": "pau",
"ம": "ma", "மா": "maa", "மி": "mi", "மீ": "mii", "மு": "mu", "மூ": "muu", "மெ": "me", "மே": "mee", "மை": "mai", "மொ": "mo", "மோ": "moo", "மௌ": "mau",
"ய": "ya", "யா": "yaa", "யி": "yi", "யீ": "yii", "யு": "yu", "யூ": "yuu", "யெ": "ye", "யே": "yee", "யை": "yai", "யொ": "yo", "யோ": "yoo", "யௌ": "yau",
"ர": "ra", "ரா": "raa", "ரி": "ri", "ரீ": "rii", "ரு": "ru", "ரூ": "ruu", "ரெ": "re", "ரே": "ree", "ரை": "rai", "ரொ": "ro", "ரோ": "roo", "ரௌ": "rau",
"ல": "la", "லா": "laa", "லி": "li", "லீ": "lii", "லு": "lu", "லூ": "luu", "லெ": "le", "லே": "lee", "லை": "lai", "லொ": "lo", "லோ": "loo", "லௌ": "lai",
"வ": "va", "வா": "vaa", "வி": "vi", "வீ": "vii", "வு": "vu", "வூ": "vuu", "வெ": "ve", "வே": "vee", "வை": "vai", "வொ": "vo", "வோ": "voo", "வௌ": "vau",
"ழ": "la", "ழா": "laa", "ழி": "li", "ழீ": "lii", "ழு": "lu", "ழூ": "luu", "ழெ": "le", "ழே": "lee", "ழை": "lai", "ழொ": "lo", "ழோ": "loo", "ழௌ": "lau",
"ள": "la", "ளா": "laa", "ளி": "li", "ளீ": "lii", "ளு": "lu", "ளூ": "luu", "ளெ": "le", "ளே": "lee", "ளை": "lai", "ளொ": "lo", "ளோ": "loo", "ளௌ": "lau",
"ற": "ra", "றா": "raa", "றி": "ri", "றீ": "rii", "று": "ru", "றூ": "ruu", "றெ": "re", "றே": "ree", "றை": "rai", "றொ": "ro", "றோ": "roo", "றௌ": "rau",
"ன": "na", "னா": "naa", "னி": "ni", "னீ": "nii", "னு": "nu", "னூ": "nuu", "னெ": "ne", "னே": "nee", "னை": "nai", "னொ": "noo", "னோ": "noo", "னௌ": "nau",
}


def translate(text):
    result = ""
    if text:
        text = text.lower()
        letters = utf8.get_letters(text)
        result = "".join([data_dict.get(letter, letter) for letter in letters])

    return result.title()