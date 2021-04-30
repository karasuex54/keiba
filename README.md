# keiba

## Task
- [ ] レースリンクからじゃなくてデータベースからレース情報を取る
- [ ] 馬のIDを入力したら馬の親の情報を取得（情報はIDぐらいだけで）

## 問題点
- 昔（例えば2010年）のレースだと https://race.netkeiba.com/race/result.html?race_id= からはデータは取れないから https://db.netkeiba.com/race/ でとれるように（あるいは後者のほうに統一）
|レース|データベース|
| ---- | ---- |
| 騎手のリンクがミスってる | 確認中 |


- データ元のリンク先がミスってる（例：https://race.netkeiba.com/race/result.html?race_id=201701020309 のマカヴのjockeyIdがおかしい）