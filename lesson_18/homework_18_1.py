import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

search_response = requests.get(search_url, params=search_params)
items = search_response.json()["collection"]["items"]

nasa_ids = [item["data"][0]["nasa_id"] for item in items[:2]]
print("Знайдені nasa_id:", nasa_ids)

for number, nasa_id in enumerate(nasa_ids, start=1):

    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_items = requests.get(asset_url).json()["collection"]["items"]

    jpg_url = next(item["href"] for item in asset_items if item["href"].endswith(".jpg"))
    print(f"{nasa_id} -> {jpg_url}")

    image_response = requests.get(jpg_url)
    file_name = f"mars_photo{number}.jpg"

    with open(file_name, "wb") as file:
        file.write(image_response.content)
    print(f"Збережено: {file_name}")