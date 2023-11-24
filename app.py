# from flask import Flask, render_template, request
# import requests

# app=Flask(__name__)

# NEWS_API_KEY = 'AgZaN18JE4QP7XEjTcXYHvfI5O2e6Hilc5RpnZwc'

# @app.route('/')
# def index():
#     # Example: fetching top headlines
#     url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
#     response = requests.get(url)
#     news_data = response.json()

#     headlines = news_data['articles']

#     return render_template('index.html', headlines=headlines)

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask
# import requests

# app = Flask(__name__)

# # Replace 'YOUR_API_KEY' with your actual News API key
# NEWS_API_KEY = 'AgZaN18JE4QP7XEjTcXYHvfI5O2e6Hilc5RpnZwc'

# @app.route('/')
# def index():
#     # Example: fetching top headlines
#     url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
#     response = requests.get(url)
#     news_data = response.json()

#     headlines = news_data['articles']

#     output = "\n".join([f"{article['title']}\n{article['description']}\n" for article in headlines])

#     return output

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)



@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])



    mylist = zip(news, desc, img)


    return render_template('index.html', context = mylist)



@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="YOUR-API-KEY")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('bbc.html', context=mylist)



if __name__ == "__main__":
    app.run(debug=True)



