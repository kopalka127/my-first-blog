import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from django.shortcuts import render

def news_view(request):
    url = "https://yk.kz/"
    response = requests.get(url)

    articles_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("li", attrs={"data-news-item": True})

        for article in articles:
            title_tag = article.find("div", class_="name")
            title_text = title_tag.text.strip() if title_tag else "Без названия"

            link_tag = article.find("a")
            link_href = link_tag["href"] if link_tag and link_tag.has_attr("href") else "#"
            link_href = urljoin(url, link_href)

            articles_data.append({"title": title_text, "link": link_href})

    else:
        print(f"Ошибка загрузки страницы: {response.status_code}")

    return render(request, "blog/news.html", {"articles": articles_data})
