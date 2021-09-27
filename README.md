# flask-articles

# 1. 仮想環境の設定
Anacondaの場合
```terminal
# 仮想環境を作ります
$ conda create --name flaskenv

# 作れたら、仮想環境を適用します
$ conda activate flaskenv

# Flask, wtforms, requests, BeautifulSoupをインストールします
(flaskenv)$ pip install flask wtforms requests beautifulsoup4
```
virtualenvの場合
```terminal
# ↓まだvirtualenvをインストールしていければ
$ pip install virtualenv

# 仮想環境を作ります
$ virtualenv flaskenv

# 仮想環境を適用します
$ source flaskenv/bin/activate

# Flask, wtforms, requests, BeautifulSoupをインストールします
(flaskenv)$ pip install flask wtforms requests beautifulsoup4
```

# 2. Runさせる方法
```terminal
$ python app.py
```
アクセス👉http://127.0.0.1:5000/
