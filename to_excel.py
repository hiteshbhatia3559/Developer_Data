import ast
import xlwt
import csv

CATEGORIES = {
    "ANDROID_WEAR": "ANDROID_WEAR",
    "ART_AND_DESIGN": "ART_AND_DESIGN",
    "AUTO_AND_VEHICLES": "AUTO_AND_VEHICLES",
    "BEAUTY": "BEAUTY",
    "BOOKS_AND_REFERENCE": "BOOKS_AND_REFERENCE",
    "BUSINESS": "BUSINESS",
    "COMICS": "COMICS",
    "COMMUNICATION": "COMMUNICATION",
    "DATING": "DATING",
    "EDUCATION": "EDUCATION",
    "ENTERTAINMENT": "ENTERTAINMENT",
    "EVENTS": "EVENTS",
    "FAMILY": "FAMILY",
    "FAMILY_ACTION": "FAMILY_ACTION",
    "FAMILY_BRAINGAMES": "FAMILY_BRAINGAMES",
    "FAMILY_CREATE": "FAMILY_CREATE",
    "FAMILY_EDUCATION": "FAMILY_EDUCATION",
    "FAMILY_MUSICVIDEO": "FAMILY_MUSICVIDEO",
    "FAMILY_PRETEND": "FAMILY_PRETEND",
    "FINANCE": "FINANCE",
    "FOOD_AND_DRINK": "FOOD_AND_DRINK",
    "GAME": "GAME",
    "GAME_ACTION": "GAME_ACTION",
    "GAME_ADVENTURE": "GAME_ADVENTURE",
    "GAME_ARCADE": "GAME_ARCADE",
    "GAME_BOARD": "GAME_BOARD",
    "GAME_CARD": "GAME_CARD",
    "GAME_CASINO": "GAME_CASINO",
    "GAME_CASUAL": "GAME_CASUAL",
    "GAME_EDUCATIONAL": "GAME_EDUCATIONAL",
    "GAME_MUSIC": "GAME_MUSIC",
    "GAME_PUZZLE": "GAME_PUZZLE",
    "GAME_RACING": "GAME_RACING",
    "GAME_ROLE_PLAYING": "GAME_ROLE_PLAYING",
    "GAME_SIMULATION": "GAME_SIMULATION",
    "GAME_SPORTS": "GAME_SPORTS",
    "GAME_STRATEGY": "GAME_STRATEGY",
    "GAME_TRIVIA": "GAME_TRIVIA",
    "GAME_WORD": "GAME_WORD",
    "HEALTH_AND_FITNESS": "HEALTH_AND_FITNESS",
    "HOUSE_AND_HOME": "HOUSE_AND_HOME",
    "LIBRARIES_AND_DEMO": "LIBRARIES_AND_DEMO",
    "LIFESTYLE": "LIFESTYLE",
    "MAPS_AND_NAVIGATION": "MAPS_AND_NAVIGATION",
    "MEDICAL": "MEDICAL",
    "MUSIC_AND_AUDIO": "MUSIC_AND_AUDIO",
    "NEWS_AND_MAGAZINES": "NEWS_AND_MAGAZINES",
    "PARENTING": "PARENTING",
    "PERSONALIZATION": "PERSONALIZATION",
    "PHOTOGRAPHY": "PHOTOGRAPHY",
    "PRODUCTIVITY": "PRODUCTIVITY",
    "SHOPPING": "SHOPPING",
    "SOCIAL": "SOCIAL",
    "SPORTS": "SPORTS",
    "TOOLS": "TOOLS",
    "TRAVEL_AND_LOCAL": "TRAVEL_AND_LOCAL",
    "VIDEO_PLAYERS": "VIDEO_PLAYERS",
    "WEATHER": "WEATHER",
}

list_of_categories = list(CATEGORIES.values())

for category in list_of_categories:
    f = open('data/{}.txt'.format(category),'r',encoding='cp1252',errors='ignore').readlines()

    list_of_f = []

    for item in f:
        list_of_f.append(ast.literal_eval(item))

    multilist = []
    a = []
    for item in list_of_f:
        a = [list(item.keys())[0]]
        for item in list(item.values()):
            for item1 in item:
                a.append(item1)
        multilist.append(a)

    multilist = [['app_id','title','dev_id','installs','dev_url','dev_email']] + multilist
    with open('data/{}.csv'.format(category),'w',newline='') as writefile:
        writer = csv.writer(writefile)
        try:
            writer.writerows(multilist)
        except:
            print('problem with '+category)