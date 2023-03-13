import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8944770"))
    API_HASH = os.environ.get("API_HASH", "d997f78197dc92d5c9765bc2b11a8740")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5054743721:AAGiCiYZ3zuW7MCsHvLPQPfBf1chxv2Ng0U")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAVxLQq-MDK1uRyDbBe1_zKA1lv2rmnR26Ki1RpqSJd9XdhlAAQ_hdLoAAkmeTsTwt-0nkRt02jg0HOEAhO9YKgN8tj9cyfQduMS8uU3t7ztIdcZvf-zqh4cdvB9teJkxMWW-szjtMvktbKkcAFilB-aTEJwF1n1ZL5uqLe1G71HoCs3sYcbfNnnaRGG_zZy3gSWr3ZuRIipvdIO3xPfmCb5E4x98iMdTsaK9fYCEF-zuT58ohnDMBUpiSMt2VchLfq8__OnxK8TUSUfhiyz5ybCWzU7CWJh9ASjloRZfkSW2hXvvuLix6JWd3Bo08ABNGtPhegadAnUYynK_rxc1jccYW45gA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Love_Guru_Music_bot")
    SUPPORT = os.environ.get("SUPPORT", "Yarri_ka_Circle") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "attitudeLover4141") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1904589030")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
