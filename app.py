# モジュールのインポート
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

# Flaskアプリのインスタンスを作成
app = Flask(__name__)


# Yahoo!ニュースのURL
url = 'https://news.yahoo.co.jp/topics'
# requests.getでurlにアクセス
r = requests.get(url)
# htmlからのデータ取得を可能にする
soup = BeautifulSoup(r.text, 'html.parser')

def get_articles():
    # pタグで、クラス名が"sc-hqyNC iOQlXg"となっている部分にカテゴリの情報が存在する
    categories = soup.find_all('p', class_='sc-hqyNC iOQlXg')
    # カテゴリ名を格納するリスト
    category_names = []
    # カテゴリのURLを格納するリスト
    category_links = []
    for category in categories:
        # category_listsに、カテゴリ名を追加(append)する
        category_names.append(category.get_text()) # get_text()とすることで、htmlタグの表示を削除できます
        # aタグからは/categories/{カテゴリ名}しか入手できないため、
        # 'https://news.yahoo.co.jp'と結合することで、URLを作成する
        category_link = 'https://news.yahoo.co.jp' + category.find('a').get('href')
        category_links.append(category_link)

    # liタグで、クラス名が"sc-ksYbfQ gSBRIC"となっている部分に記事情報が存在する
    li_lists = soup.find_all('li', class_="sc-ksYbfQ gSBRIC")
    # 記事の名前を格納するリスト
    article_names = []
    # 記事のURLを格納するリスト
    article_links = []
    for li_list in li_lists:
        article_name = li_list.find('a').get_text()
        article_names.append(article_name)
        article_link = li_list.find('a').get('href')
        article_links.append(article_link)

    return category_names, category_links, article_names, article_links


@app.after_request
def apply_caching(response):
     response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
     return response

# ルーティングの設定
@app.route('/')
def index():
    category_names, category_links, article_names, article_links = get_articles()
    return render_template(
        'index.html', 
        category_names=category_names, category_links=category_links,
        article_names=article_names, article_links=article_links
        )

# このコードによって、Flaskがweb上で走ります
if __name__ == '__main__':
    # debug=Trueとすることで、保存するだけで変更が適用されます
    # エラーも見やすくなります
    app.run(debug=True)