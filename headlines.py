import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'ad': 'https://www.ad.nl/home/rss.xml',
             'vk':  'https://www.volkskrant.nl/nieuws-achtergrond/rss.xml',
             'tr': 'https://www.trouw.nl/voorpagina/rss.xml',
             'nu': 'https://www.nu.nl/rss'}


@app.route("/")
@app.route("/vk")
def vk():
    return get_news('vk')


@app.route("/ad")
def ad():
    return get_news('ad')


def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>Headlines </h1>
            <b>{0}</b>
            <i>{1}</i>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("link"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
