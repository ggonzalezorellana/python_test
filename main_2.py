"""
2. En base a la programación orientada a objetos deberás crear
un pequeño conector para una API,
    para ello, deberás utilizar una clase padre llamada "LastMile API"
        que contenga todos los elementos básicos para comunicarte con la API, y adicionalmente, tendrás que
    crear dos clases relacionadas,
        una que se llame Route y
        la otra que se llame Guide
que contenga los siguientes métodos de la API:

Route:

    Create Route
    Update Route
    Show Route

Dispatch:

    Create Dispatch
    Show Dispatch
"""
import requests


class LastMileAPI:
    content_type = "application/json"
    token = "api_token"
    base_url = "http://app.beetrack.com/api/external/v1"
    headers = {
        "X-AUTH-TOKEN": token,
        "Content-Type": content_type
    }


class Route:
    sf_url = "/routes"
    # post
    create = ""
    # get
    show = "/:"
    # put
    update = "/:"


class Dispatch:
    sf_url = "/dispatches"
    # post
    create = ""
    # get
    show = "/:"


def connect(obj, obj_id, obj_method):
    base_url = LastMileAPI.base_url
    headers = LastMileAPI.headers

    if obj == "Route":
        objt = Route
    else:
        objt = Dispatch

    if obj_method == "create":
        obj = objt.objects.filter()
        sf_url = obj.sf_url + obj.create
        url = base_url + sf_url
        response = requests.post(url, headers=headers)
    elif obj_method == "show":
        obj = objt.objects.filter(id=obj_id)
        sf_url = obj.sf_url + obj.show + "%s" % obj.id
        url = base_url + sf_url
        response = requests.get(url, headers=headers)
    else:
        obj = objt.objects.filter(id=obj_id)
        sf_url = obj.sf_url + obj.update + "%s" % obj.id
        url = base_url + sf_url
        response = requests.put(url, headers=headers)
