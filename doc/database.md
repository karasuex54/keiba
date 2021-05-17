# データについて
## レース前に得られる情報（使う）
- レース名
- レース場
- 馬場
- 距離
- 右回りか左回りか
- 天候
- 馬場
- 枠
- 馬番
- 馬名
- 血統
- 性
- 齢
- 斤量
- 騎手
- 厩舎
- 馬体重
- 増減

## レース後に得られる情報（使う）
- 着順
- タイム
- 着差
- 上がり3F
- コーナー通過順

# database

- RACES
- RESULTS

## RACES

| Column    | Type | Options     | Description       |
| ----      | ---- | ----        | ----              |
| id        | TEXT | PRIMARY KEY | race id           |
| name      | TEXT | -           | race name         |
| surface   | TEXT | -           | track surface     |
| distance  | TEXT | -           | race distance (m) |
| rotation  | TEXT | -           | race rotation     |
| weather   | TEXT | -           | weather           |
| condition | TEXT | -           | track condition   |
| place     | TEXT | -           | race place        |
| grade     | TEXT | -           | race grade        |
| other     | TEXT | -           | other infomation  |

## RESULTS

| Column        | Type | Options     | Description                  |
| ----          | ---- | ----        | ----                         |
| id            | TEXT | PRIMARY KEY | house and race id            |
| race_id       | TEXT | -           | race id                      |
| ord           | TEXT | -           | order of finish              |
| post          | TEXT | -           | post position                |
| number        | TEXT | -           | horse number in race         |
| horse_id      | TEXT | -           | house id                     |
| sex           | TEXT | -           | house sex                    |
| age           | TEXT | -           | house age                    |
| penalty       | TEXT | -           | weight on the hose           |
| jockey_id     | TEXT | -           | jockey id                    |
| finish        | TEXT | -           | finish time  (s)             |
| margin        | TEXT | -           | margin                       |
| corner        | TEXT | -           | order of passing corners     |
| g-3f          | TEXT | -           | time last three furlongs (s) |
| odds          | TEXT | -           | win odds                     |
| popular       | TEXT | -           | popular                      |
| weight        | TEXT | -           | horse weight (kg)            |
| weight_dif    | TEXT | -           | horse weight difference (kg) |
| stable        | TEXT | -           | stable id                    |

## PEDIGREES
| Column    | Type | Options     | Description             |
| ----      | ---- | ----        | ----                    |
| horse_id  | TEXT | PRIMARY KEY | horse id                |
| b_ml      | TEXT | -           | horse's father          |
| b_ml_ml   | TEXT | -           | horse's father's father |
| b_ml_fml  | TEXT | -           | horse's father's mother |
| b_fml     | TEXT | -           | horse's mother          |
| b_fml_ml  | TEXT | -           | horse's mother's father |
| b_fml_fml | TEXT | -           | horse's mother's mother |
