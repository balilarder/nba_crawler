# NBA crawler

## Usage
- 進入專案nba_crawler

`cd nba_crawler`

- 創建virtual environment and activate

`python3 -m venv venv`

`source venv/bin/activate`

- 確保之後執行的django server與scrapy爬蟲皆在(venv中)
![](https://i.imgur.com/XXVTrZg.png)

- 安裝所需套件

`pip install django scrapy scrapyd python-scrapyd-api scrapy-djangoitem`

- 進入firstdjango, 執行migration準備資料庫

`cd firstdjango`

`python manage.py makemigrations`

`python manage.py migrate`

![](https://i.imgur.com/Db3GJCu.png)

- 啟動server

`python manage.py runserver`

- 在broser中輸入http://127.0.0.1:8000/ , 進入首頁。

- 目前資料庫為空，因為尚未執行scrapy爬蟲，首頁目前沒有資料

![](https://i.imgur.com/BNCEvbH.png)

- 開啟另一個執行環境(也要先source venv/bin/activate)進入

`/nba_crawler/firstdjango/scrapy_app/scrapy_app`

- 執行一次爬蟲`python main.py`, 此會在網頁中擷取焦點新聞，一次擷取三篇，並用scrapy的pipeline配合Django的model存入DB

- 重新整理首頁，將會多了三筆資料

![](https://i.imgur.com/FUzTYUX.png)

- 每執行一次爬蟲就會多三筆資料



