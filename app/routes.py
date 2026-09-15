import json
import os

from flask import Blueprint, abort, render_template


main = Blueprint("main", __name__)


def cargar_productos():
    ruta = os.path.join(os.path.dirname(__file__), "data", "productos.json")

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def buscar_producto_por_sku(sku):
    productos = cargar_productos()

    for producto in productos:
        if producto["sku"] == sku:
            return producto

    return None


@main.route("/")
def index():
    productos = cargar_productos()
    return render_template("index.html", productos=productos)


@main.route("/producto/<sku>")
def detalle(sku):
    producto = buscar_producto_por_sku(sku)

    if producto is None:
        abort(404)

    return render_template("detalle.html", producto=producto)
