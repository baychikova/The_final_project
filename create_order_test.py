import pytest 
import data
import sender_stand_request

def test_create_order_and_get_by_track():
    # Создать заказ
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201

    # Сохранить track из ответа
    track = create_response.json().get("track")
    assert track is not None

    # Получить заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200

    # Евгения Байчикова, 43-я когорта — Финальный проект. Инженер по тестированию плюс