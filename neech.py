import pyautogui
import time
import random
pyautogui.hotkey('winleft', 'q')
time.sleep(0.5)
pyautogui.typewrite("Whats")
pyautogui.press("Enter")
time.sleep(2.5)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("Neech")
pyautogui.press("tab")
time.sleep(5)  # for staying on the safer side, you can close the whatsapp windows in this time span.
pyautogui.press("Enter")
time.sleep(2)
count = 1

gaali = ["bhosad chod (ass fucker)", "chodu bhagat (fucking asshole)", "gaandu (born from an ass)", "lund choosu (cock sucker)", "chut ke dhakkan (pussy lid)", "chut mari ke (fucked up)", "gaand ka makhan (butter from the ass)", "gaand main lassan (garlic in ass)", "Bhosad (ass), Chutiya (fool)", "Bhenchod (sister-fucker)", "Randi (whore)", "Lund (penis)", "Gaand (ass)", "Choot (vagina)", "Bachchoda (bastard)", "Bhadke (arsehole)", "Chhota (small penis)", "Chudna (fucking)", "Chhut (vagina)", "Chhut ke dhakkan (pussy lid)", "Chhut ke pasine (pussy sweat)", "Chhut marani (pussy whipped)", "Chhut ke baal (vagina hair)", "Chhut ke bhoot (vaginal ghost)", "Chhut ke dhakkan mein talay huye bhajiye (snack fried in pussy sweat)", "Tere gaand mein keede paday", "Teri maa ka bhosda", "Teri gaand main kute ka lund", "Sadi hui gaand", "Rundi khana", "Najayaz paidaish", "Meri Gand Ka Khatmal", "Lund Chus", "Kutte ke poot, teri maa ki choot", "Kadak Mall", "Kali Choot Ke Safaid Jhaat", "Pote kitne bhi bade ho, lund ke niche hi rehte hai", "Bol teri gand kaise maru", "Bhonsri-Waalaa", "Abla naari tera buble bhaari", "Bhen ke takke", "Betichod", "Chullu bhar muth mein doob mar", "Chinaal ke gadde ke nipple ke baal ke joon", "Chutiya ka bheja ghas khane gaya hai", "Chut ke pasine mein talay huye bhajiye", "Chut ke gulam", "Kamina", "madar chod bhosdke esa lagta h apne hii taaate kaat ke chipka diya apni shakal dekh lodee jese shakal aur gand me h aakal", "Chhut ke dhakkan mein lassan (garlic in pussy)", "Chhut ke dhakkan mein bambu (bamboo in pussy)", "Bokachoda", "Chhut ke dhakkan mein keera (bug in pussy)", "Chhut ke dhakkan mein danda (stick in pussy)", "Chhut ke dhakkan mein hazaar lund (thousand dicks in pussy)", "Chhut ke dhakkan mein muthi (fist in pussy)", "Chhut ke dhakkan mein jhaat (pubic hair in pussy)", "Chhut ke dhakkan mein jhaat ke baal (pubic hair in pussy)", "Chhut ke dhakkan mein jhaat ke pasine (pubic hair sweat in pussy)", "Chhut ke dhakkan mein jhaat ke baal ke joon (pubic hair lice in pussy)", "Chhut ke dhakkan mein jhaat ke baal ke joon ke nipple (pubic hair lice nipple in pussy)", "Chhut ke dhakkan mein jhaat ke baal ke joon ke nipple ke baal (pubic hair lice nipple hair in pussy)", "bhos randi ke", "behen dhodhi ke", "chutpaglu", "aad", "aand", "bahenchod", "behenchod", "bhenchod", "bhenchodd", "b.c.", "bc", "bakchod", "bakchodd", "bakchodi", "bevda", "bewda", "bevdey", "bewday", "bevakoof", "bevkoof", "bevkuf", "bewakoof", "bewkoof", "bewkuf", "bhadua", "bhaduaa", "bhadva", "bhadvaa", "bhadwa", "bhadwaa", "bhosada", "bhosda", "bhosdaa", "bhosdike", "bhonsdike", "bsdk", "b.s.d.k", "bhosdiki", "bhosdiwala", "bhosdiwale", "bhosadchodal", "bhosadchod", "bhosadchodal", "bhosadchod", "babbe", "babbey", "bube", "bubey", "bur", "burr", "buurr", "buur", "charsi", "chooche", "choochi", "chuchi", "chhod", "chod", "chodd", "chudne", "chudney", "chudwa", "chudwaa", "chudwane", "chudwaane", "choot", "chut", "chute", "chutia", "chutiya", "chutiye", "chuttad", "chutad", "dalaal", "dalal", "dalle", "dalley", "fattu", "gadha", "gadhe", "gadhalund", "gaand", "gand", "gandu", "gandfat", "gandfut", "gandiya", "gandiye", "goo", "gu", "gote", "gotey", "gotte", "hag", "haggu", "hagne", "hagney", "harami", "haramjada", "haraamjaada", "haramzyada", "haraamzyaada", "haraamjaade", "haraamzaade", "haraamkhor", "haramkhor", "jhat", "jhaat", "jhaatu", "jhatu", "kutta", "kutte", "kuttey", "kutia", "kutiya", "kuttiya", "kutti", "landi", "landy", "laude", "laudey", "laura", "lora", "lauda", "ling", "loda", "lode", "lund", "launda", "lounde", "laundey", "laundi", "loundi", "laundiya", "loundiya", "lulli", "maar", "maro", "marunga", "madarchod", "madarchodd", "madarchood", "madarchoot", "madarchut", "m.c.", "mc", "mamme", "mammey", "moot", "mut", "mootne", "mutne", "mooth", "muth", "nunni", "nunnu", "paaji", "paji", "pesaab", "pesab", "peshaab", "peshab", "pilla", "pillay", "pille", "pilley", "pisaab", "pisab", "pkmkb", "porkistan", "raand", "rand", "randi", "randy", "suar", "tatte", "tatti", "tatty", "ullu"]

while count <= len(gaali):
    pyautogui.typewrite(random.choice(gaali))
    time.sleep(0.5)
    pyautogui.press("Enter")
    count += 1
