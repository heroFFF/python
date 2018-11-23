from datetime import datetime
birthday=datetime.now()
birthday.strftime("%Y-%m-%d")
print("生日是{0:%Y}年{0:%m}月{0:%d}日".format(birthday))
