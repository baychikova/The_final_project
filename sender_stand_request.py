import requests
import configuration
import data 

def create_order(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )
    return response

def get_order_by_track(track_number):
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track_number}
    )
    return response