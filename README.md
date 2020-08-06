# TimeIsMoney

## TL;DR
- 昔作成した簡単な時給計算シミュレーターをwebアプリ移植
- データ入力だけで自分のコストパフォーマンス計測出来る！
- DB連携して入力してきた方々の平均値をビビっと出すくらいまでやるかな？

## config
- vue-cli
- python3
- pipenv

## debug
```
cd frontend
npm run build
npm run serve

cd backend
pipenv run start
http://localhost:5000

# pipenv in
pipenv shell
deactivate
exit
```

```heroku
heroku run python
from ~ import db
db.create_all()
```

## 残り
PWA  
herokuが落ちないような定期タスク追加  

## 後回し🥺
design  
average  
db migrate  
refactor
