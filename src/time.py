import os
import logging
import requests
from fastapi import UploadFile

from src.config import settigns


client_id = settigns.CLIENT_ID


async def download_image_user(file: UploadFile) -> str:
    # Убедимся, что это изображение
    if not file.content_type.startswith("image/"):
        raise ValueError("Файл должен быть изображением!")

    image_path = f"src/photo/{file.filename}"
    logging.warning(f"Сохраняем изображение во временный файл: {image_path}")

    # Сохраняем файл на диск
    with open(image_path, "wb") as out_file:
        content = await file.read()
        out_file.write(content)

    try:
        # Загружаем в Imgur
        with open(image_path, 'rb') as img:
            headers = {
                'Authorization': f'Client-ID {client_id}'
            }
            files = {
                'image': img
            }

            url = 'https://api.imgur.com/3/upload'
            response = requests.post(url, headers=headers, files=files)

        # Обрабатываем ответ
        if response.status_code == 200:
            uploaded_image_url = response.json()['data']['link']
            return uploaded_image_url
        else:
            logging.error(f"Ошибка при загрузке: {response.status_code}")
            logging.error(response.json())
            raise RuntimeError("Ошибка при загрузке на Imgur")

    finally:
        # Удаляем файл после загрузки
        if os.path.exists(image_path):
            os.remove(image_path)
