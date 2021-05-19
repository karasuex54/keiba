# keiba

`main.py`でnetkeiba.comからデータを取ってきます。

`data_to_csv.py`で取得してきたデータからcsvファイルにして出力してくれます。

## check
- 2021-2017

## Task
- 回りが「右外-内」になってるのはどうしようか（例：https://db.netkeiba.com/race/202109021211 ）

## 問題点
- 昔（例えば2010年）のレースだと https://race.netkeiba.com/race/result.html?race_id= からはデータは取れないから https://db.netkeiba.com/race/ でとれるように（あるいは後者のほうに統一）
- データ元のリンク先がミスってる（例：https://race.netkeiba.com/race/result.html?race_id=201701020309 のマカヴのjockeyIdがおかしい）