import re
from responses import get_custom_response, unknown
RULES = [
    {
        "keywords": ["hello", "hi", "hey", "salut"],
        "response": "Hello! 😊",
        "single_response": True
    },
    {
        "keywords": ["how", "are", "you", "doing"],
        "required": ["you"],
        "response": "I'm doing fine, and you?"
    },
    {
        "keywords": ["what", "is", "your", "name"],
        "required": ["name"],
        "response": "I'm CodePal, your friendly chatbot 🤖"
    },
    {
        "keywords": ["i", "love", "code", "palace"],
        "required": ["code"],
        "response": "Thank you! ❤️"
    },
    {
        "keywords": ["what", "you", "eat", "like"],
        "required": ["eat"],
        "response": get_custom_response("eat")
    },
    {
        "keywords": ["bye", "goodbye", "see"],
        "response": "Goodbye! 👋",
        "single_response": True
    },
    {
        "keywords": ["help", "assist", "support"],
        "response": "How can I assist you today?",
        "single_response": True
    },
    {
        "keywords": ["joke", "funny"],
        "response": "Why don't programmers like nature? It has too many bugs! 😂",
        "single_response": True
    },
    {
        "keywords": ["weather", "forecast"],
        "response": "I can't check the weather, but I hope it's nice where you are! ☀️",
        "single_response": True
    },
    {
        "keywords": [],
        "response": unknown(),
        "single_response": True
    }
]

def message_probability(user_message, keywords, single_response=False, required=[]):

    # Calculează probabilitatea mesajului message_certainty
    message_certainty = 0
    for word in user_message:
        if word in keywords:
            message_certainty += 1
    #pt fiecare cuvant din mesaj care apare in recognised_words
    #message_certainty este incrementat

    #Calculăm match_ratio ca raportul dintre message_certainty și numărul de cuvinte din keywords
    #dacă keywords este gol, setăm match_ratio la 0
    if len(keywords) == 0:
        match_ratio = 0
    else:
        match_ratio = message_certainty / len(keywords)

    if required:
        if not all(word in user_message for word in required):
            return 0
    match_ratio = match_ratio
    if single_response:
        return 1 if match_ratio > 0 else 0
    return int(match_ratio * 100) if match_ratio > 0 else 0

def check_all_messages(message):
    highest_prob = 0
    best_response = None

    for rule in RULES:
        #None
        
        # Calculează probabilitatea mesajului pentru fiecare regulă
        #folosind funcția message_probability definită mai sus
        prob = message_probability(message, rule['keywords'], rule.get('single_response', False), rule.get('required', []))
        #dacă prob este mai mare decât highest_prob,
        # actualizează best_response și highest_prob
        if prob > highest_prob:
            highest_prob = prob
            best_response = rule['response']
    # returneaza raspunsul, fie cel de eroare, fie cel gasit 
    return best_response if best_response else unknown()

def get_response(user_input):
    #str1 = "Ana"
    #return str1
    # Verifică dacă user_input este gol sau conține doar spații
    if not user_input or user_input.strip() == "":
        return "Please say something!"
    # apeleaza functia split pentru a împărți mesajul în cuvinte 
    clean_message = re.split(r'\s+|[,;?.-]\s*', user_input.lower())
    # apoi returneaza rezultatul obtinut folosind check_all_messages pentru a verifica mesajul
    return check_all_messages(clean_message)

# Ce inseamna \s+|[,;?.-]\s*?
# \s+ înseamnă unul sau mai multe spații albe (inclusiv tab-uri și linii noi)
# | este operatorul "sau" în expresiile regulate
# [,;?.-] înseamnă oricare dintre caracterele specificate (
# virgulă, punct și virgulă, punct, semn de întrebare sau cratimă)
# \s* înseamnă zero sau mai multe spații albe după aceste caractere
# deci, expresia întreagă împarte mesajul în cuvinte folosind spațiile albe și semnele de punctuație specificate
# de exemplu, "Hello, world! How are you?" va fi împărțit în
# ["hello", "world", "how", "are", "you"]