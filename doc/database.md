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
| hold_date | TEXT | -           | hold at date      |

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
