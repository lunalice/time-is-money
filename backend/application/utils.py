from datetime import datetime, timedelta
import pandas
import urllib
from IPython import embed

public_holiday_csv_url="https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv"
file_name = public_holiday_csv_url.split("/")[-1]

# 対象年度
target_year = datetime(datetime.now().year, datetime.now().month, datetime.now().day) 

# 会社特有の休日
company_holiday = [] # '2019-01-01'

def get_holiday_flg(date):
    # 通常の土日
    if (date.weekday() >= 5):
        return True

    # 祝日
    holidays_df = pandas.read_table(file_name, delimiter=',', encoding="SHIFT-JIS")
    if date.strftime("%Y-%m-%d") in holidays_df['国民の祝日・休日月日'].tolist():
        return True

    #　会社の休日
    if date.strftime("%Y-%m-%d") in company_holiday:
        return True

    return False

def holiday():
    # 内閣府から祝日データを取得、更新したいときにTrue
    if False:
        urllib.request.urlretrieve(public_holiday_csv_url, file_name)

    result = 0
    date = datetime(target_year.year, 1, 1, 0, 0)

    while date != target_year:
        if get_holiday_flg(date):
            result += 1
        date += timedelta(days=1)
    
    return result