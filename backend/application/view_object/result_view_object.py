from IPython import embed
import application.utils as Utils
import urllib

class ResultViewObject:
    def __init__(self, age, annual_income, working_hours, overtime, commuting_time, rent, holiday=None):
        self.age = int(age)
        self.annual_income = int(annual_income)
        self.working_hours = int(working_hours)
        self.overtime = int(overtime)
        self.commuting_time = int(commuting_time)
        self.rent = int(rent)
        self.holiday = int(holiday or Utils.holiday())

    def output(self):
        return {
            'age': self.age,
            'working_hours': self.working_hours,
            'overtime': self.overtime,
            'commuting_time': self.commuting_time,
            'rent': self.rent,
            'holiday': self.holiday,
            'annual_rent': self.rent * 12,
            'hourly_wage': self.hourly_wage(),
            'daily_wage': self.daily_wage(),
            'operating_time': self.operating_time(),
            'annual_commuting_time': self.annual_commuting_time(), # 年間通勤時間
            'consumption': self.consumption(), # 消費金額
            'annual_income': self.annual_income,
            'income': (self.annual_income - self.consumption()), # 年収
            'overtime_pay': self.overtime_pay(), # 残業代
            'working_days': self.working_days(),
            'twitter_intent_url': self.twitter_intent_url()
        }

    def daily_wage(self): # 年収 * 10000 / 労働日数 = 日収
        return round((self.annual_income) / self.working_days())

    def hourly_wage(self): # 日給 / 実労働時間 = 時給
        return round(self.daily_wage() / self.operating_time())

    def operating_time(self): # 労働時間 + 平均残業時間 * 12ヶ月 / 労働日 = 実稼働時間
        return round(self.working_hours + self.overtime * 12 / self.working_days())

    def working_days(self): # 365 - 休日 = 年間労働日
        return round(Utils.NUMBER_OF_DAYS_PER_YEAR - self.holiday)
    
    def consumption(self): # 時給 * 年間通勤時間 = 消費金額
        return round(self.hourly_wage() * self.annual_commuting_time())

    def annual_commuting_time(self): # 通勤時間（片道分）* 2 / 60(時間変換) * 労働日数 = 年間通勤時間
        return round(((self.commuting_time * 2) / 60) * self.working_days())

    def overtime_pay(self): # 平均残業時間 * 12ヶ月 * 時給
        return round(self.overtime * 12 * self.hourly_wage())

    def twitter_intent_url(self):
        text = f'{self.age}才さんのコスパは...\n時給：{self.hourly_wage()}円\n日給：{self.daily_wage()}円\n通勤時間（年）：{self.annual_commuting_time()}時間\n年間消費金額：{self.age}円\n実収入：{self.age}円\n'
        url = 'http://localhost:5000/'
        hashtags = 'コスパシミュ'
        params = {
          'text': text,
          'url': url,
          'hashtags': hashtags,
        }
        d_qs = urllib.parse.urlencode(params)
        print(d_qs)
        return 'https://twitter.com/intent/tweet' + '?' + d_qs