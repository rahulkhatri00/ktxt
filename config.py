import os

API_ID = API_ID = 27355149

API_HASH = os.environ.get("API_HASH", "68bcb1ab22bd80bbae9d66ccddf540c2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7350135417:AAEjnqZhUX-IeARKYIz9NF9CK_DkMTJkv0c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7068698396))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7068698396").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


