import play_scraper
from multiprocessing import Pool

number_of_cores_to_use = 4
number_of_pages_per_category = 25  # Change as you like, runtime will go up significantly

COLLECTIONS = {
    'NEW_FREE': 'topselling_new_free',
    'NEW_PAID': 'topselling_new_paid',
    'TOP_FREE': 'topselling_free',
    'TOP_PAID': 'topselling_paid',
    'TOP_GROSSING': 'topgrossing',
    'TRENDING': 'movers_shakers',
}

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


def list_of_details_of_collection(category, number_of_pages_per_category):
    f = open('data/' + category + '.txt', 'w')
    print('Finding results for' + category)
    for collection in COLLECTIONS:
        for page in range(0, number_of_pages_per_category):
            try:
                scraper = play_scraper.collection(
                    collection=collection,
                    category=category,
                    results=120,
                    page=page
                )
            except:
                break
            list_of_ids = []
            list_of_details = []
            for item in scraper:
                list_of_ids.append(item['app_id'])

            for id in list_of_ids:
                a = play_scraper.details(id)
                b = {a['app_id']: [a['title'], a['developer_id'], a['installs'], a['developer_url'],
                                   a['developer_email']]}
                list_of_details.append(b)
                try:
                    f.write(str(b) + '\n')
                except:
                    break
    print(category + ' Done\n')


if __name__ == "__main__":
    p = Pool(number_of_cores_to_use)
    p.map(list_of_details_of_collection, (CATEGORIES, number_of_pages_per_category))
