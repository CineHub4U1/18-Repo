#    Copyright (c) 2021 Danish_00
#    Improved By @Shirou

from decouple import config

try:
    APP_ID = config("APP_ID", "20288183")
    API_HASH = config("API_HASH", "c552d415c8c88ac267891e1d01deaa57")
    BOT_TOKEN = config("BOT_TOKEN", "5929336845:AAEot0q2AHflpowNzYBO6L1aZ2Gb_Esc_zA")
    DEV = 5211097098
    OWNER = config("OWNER", "1164918935")
    ffmpegcode = ["-preset veryfast -c:v libx265 -s 1280:-2 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By DaddyCooL' -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 128k -vbr on -c:s copy -map 0 threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/ebde50b591e0e6c19366c.png")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
