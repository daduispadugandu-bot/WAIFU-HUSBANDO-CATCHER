class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6653139548"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = 1003283703106
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "@Anime_Harem_Bot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 25962157
    api_hash = "b650e6e6766b8b24362e2bd73b9a6c14"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
