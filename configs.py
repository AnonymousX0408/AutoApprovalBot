# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23257540"))
    API_HASH = getenv("API_HASH", "39ec865c872592512e5c61da6da0e7e9")
    BOT_TOKEN = getenv("BOT_TOKEN", "6558469088:AAE8E1pglkqxQh6rjsmYwuVDfgobpIyx7To")
    FSUB = getenv("FSUB", "Privates_RoBot")
    CHID = int(getenv("CHID", "-1001938360542"))
    SUDO = list(map(int, getenv("SUDO", "6417243582").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
