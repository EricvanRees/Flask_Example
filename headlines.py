import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'ad': 'https://www.ad.nl/home/rss.xml',
             'vk':  'https://www.volkskrant.nl/nieuws-achtergrond/rss.xml',
             'tr': 'https://www.trouw.nl/voorpagina/rss.xml',
             'nu': 'https://www.nu.nl/rss'}


@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "vk"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template("index.html",
                           articles=feed['entries'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
