# keiba

## Task
- 「阪神10日目」から「阪神1」と間違えてる（例：https://db.netkeiba.com/race/202109021007 ）
- 「内2周3600m」から距離が「2」と間違えてる（例：https://db.netkeiba.com/race/201706050111 ）
- 「障芝」から回りが「芝」と間違えてる（例：https://db.netkeiba.com/race/201706010208 ）
- 回りが「右外-内」になってるのはどうしようか（例：https://db.netkeiba.com/race/202109021211 ）
- その他の情報が空になっている（例：https://db.netkeiba.com/race/201710010201 ）

## 問題点
- 昔（例えば2010年）のレースだと https://race.netkeiba.com/race/result.html?race_id= からはデータは取れないから https://db.netkeiba.com/race/ でとれるように（あるいは後者のほうに統一）
|レース|データベース|
| ---- | ---- |
| 騎手のリンクがミスってる | 確認中 |


- データ元のリンク先がミスってる（例：https://race.netkeiba.com/race/result.html?race_id=201701020309 のマカヴのjockeyIdがおかしい）