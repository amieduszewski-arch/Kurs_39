from flask import Flask, render_template, request, session, redirect, url_for
import json
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__, static_folder="static")

# koszyl klucz
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")

# email

EMAIL_ADDRESS = "a.mieduszewski@gmail.com"            # adres wysyłający
EMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")      # hasło aplikacji Gmail
RESTAURANT_EMAIL = "a.mieduszewski@gmail.com"         # adres restauracji


# Baza menu

MENU = [

    # SOUVLAKI PITA

    {
        "name": "Pita z kurczakiem",
        "price": 34,
        "category": "Souvlaki pita",
        "description": "kurczak, pita, tzatziki, sałata, pomidor, ogórek małosolny",
        "image": "dishes/Pita_z_kurczakiem.jpg",
    },
    {
        "name": "Pita z wieprzowiną",
        "price": 36,
        "category": "Souvlaki pita",
        "description": "wieprzowina, pita, tzatziki, sałata, pomidor, ogórek małosolny",
        "image": "dishes/Pita_z_wieprzowina.jpg",
    },
    {
        "name": "Pita wege",
        "price": 36,
        "category": "Souvlaki pita",
        "description": "halloumi, pita, tzatziki, sałata, pomidor",
        "image": "dishes/Pita_wege.jpg",
    },

    # SOUVLAKI NA TALERZU

    {
        "name": "Talerz z kurczakiem",
        "price": 36,
        "category": "Souvlaki na talerzu",
        "description": "kurczak, pita, tzatziki, sałata, pomidor, frytki",
        "image": "dishes/Talerz_z_kurczakiem.jpg",
    },
    {
        "name": "Talerz z wieprzowiną",
        "price": 38,
        "category": "Souvlaki na talerzu",
        "description": "wieprzowina, pita, tzatziki, sałata, pomidor, frytki",
        "image": "dishes/Talerz_z_wieprzowina.jpg",
    },
    {
        "name": "Talerz z rybą panierowaną",
        "price": 40,
        "category": "Souvlaki na talerzu",
        "description": "mintaj, pita, tzatziki, sałata, pomidor, frytki",
        "image": "dishes/Talerz_z_ryba_panierowana.jpg",
    },
    {
        "name": "Talerz wege",
        "price": 38,
        "category": "Souvlaki na talerzu",
        "description": "halloumi, pita, tzatziki, sałata, pomidor, frytki",
        "image": "dishes/Talerz_wege.jpg",
    },

    # DODATKI

    {
        "name": "Frytki małe 150g",
        "price": 11,
        "category": "Dodatki",
        "description": "podawane z parmezanem i tymiankiem",
        "image": "dishes/Frytki_male_150g.jpg",
    },
    {
        "name": "Frytki duże 210g",
        "price": 17,
        "category": "Dodatki",
        "description": "podawane z parmezanem i tymiankiem",
        "image": "dishes/Frytki_duze_210g.jpg",
    },
    {
        "name": "Ser halloumi",
        "price": 11,
        "category": "Dodatki",
        "description": "grillowany ser halloumi",
        "image": "dishes/Ser_halloumi.jpg",
    },
    {
        "name": "Ser feta",
        "price": 8,
        "category": "Dodatki",
        "description": "tradycyjna grecka feta",
        "image": "dishes/Ser_feta.jpg",
    },
    {
        "name": "Oliwki kalamata",
        "price": 8,
        "category": "Dodatki",
        "description": "oliwki greckie",
        "image": "dishes/Oliwki_kalamata.jpg",
    },
    {
        "name": "Sos tzatziki",
        "price": 6,
        "category": "Dodatki",
        "description": "sos jogurtowo-czosnkowy",
        "image": "dishes/Sos_tzatziki.jpg",
    },
    {
        "name": "Coca-Cola 0,33l",
        "price": 7,
        "category": "Napoje bezalkoholowe",
        "image": "dishes/Coca_Cola.jpg",
    },
    {
        "name": "Ayran 250ml",
        "price": 6,
        "category": "Napoje bezalkoholowe",
        "image": "dishes/Ayran_250ml.jpg"
    }
]

# strona glowna

@app.route("/")
def home():
    return render_template("index.html")

# strona menu

@app.route("/menu")
def menu():

    categories = {}

    for dish in MENU:
        cat = dish["category"]

        if cat not in categories:
            categories[cat] = []

        categories[cat].append(dish)

    return render_template("menu.html", categories=categories)

# dodawanie do koszyka

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():

    product_name = request.form.get("product")

    if not product_name:
        return {"status": "error"}

    if "cart" not in session:
        session["cart"] = []

    for dish in MENU:
        if dish["name"] == product_name:
            session["cart"].append(dish)
            break

    session.modified = True

    return {"status": "ok"}

# srona koszyk

@app.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    total_price = sum(item["price"] for item in cart_items)
    discount = round(total_price * 0.10, 2)
    final_price = round(total_price - discount, 2)

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total_price=total_price,
        discount=discount,
        final_price=final_price
    )

# usuwanie z koszyka

@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():

    index = request.form.get("index")

    if index is not None and "cart" in session:

        index = int(index)

        if 0 <= index < len(session["cart"]):
            session["cart"].pop(index)
            session.modified = True

    return redirect(url_for("cart"))

@app.route("/remove-from-cart-ajax", methods=["POST"])
def remove_from_cart_ajax():

    index = request.form.get("index")

    if index is not None and "cart" in session:

        index = int(index)

        if 0 <= index < len(session["cart"]):
            session["cart"].pop(index)
            session.modified = True

    return {"status": "ok"}

# API dla koszyka js


@app.route("/cart-data")
def cart_data():

    cart_items = session.get("cart", [])

    total = sum(item["price"] for item in cart_items)
    discount = round(total * 0.10, 2)
    final_price = round(total - discount, 2)

    return {
        "items": cart_items,
        "total": total,
        "discount": discount,
        "final_price": final_price
    }


# koniec zamowniea

@app.route("/order", methods=["GET", "POST"])
def order():

    cart_items = session.get("cart", [])

    total_price = sum(item["price"] for item in cart_items)
    discount = round(total_price * 0.10, 2)
    final_price = round(total_price - discount, 2)

    payment_status = None

    # zloz zamowienie
    if request.method == "POST" and cart_items:

        order_data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dishes": cart_items,
            "total_price": final_price,
            "discount": discount,
            "status": "PAID (SIMULATION)"
        }

        try:
            with open("orders.json", "r", encoding="utf-8") as file:
                orders = json.load(file)
        except FileNotFoundError:
            orders = []

        orders.append(order_data)

        with open("orders.json", "w", encoding="utf-8") as file:
            json.dump(orders, file, ensure_ascii=False, indent=4)

        send_order_email(order_data)

        session.pop("cart", None)

        payment_status = "Zamówienie przyjęte i wysłane do restauracji"

    return render_template(
        "order.html",
        cart_items=cart_items,
        total_price=total_price,
        discount=discount,
        final_price=final_price,
        payment_status=payment_status
    )


# statystyka

@app.route("/stats")
def stats():

    try:
        with open("orders.json", "r", encoding="utf-8") as file:
            orders = json.load(file)
    except FileNotFoundError:
        orders = []

    dish_counter = {}

    for order in orders:
        for dish in order["dishes"]:
            name = dish["name"]
            dish_counter[name] = dish_counter.get(name, 0) + 1

    return render_template(
        "stats.html",
        labels=list(dish_counter.keys()),
        values=list(dish_counter.values())
    )


# wysylanie zamowienia

def send_order_email(order):

    if not EMAIL_PASSWORD:
        print("Brak hasła Gmail ENV")
        return

    msg = EmailMessage()

    msg["Subject"] = "Nowe zamówienie – Greek Street Food"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RESTAURANT_EMAIL

    dishes_text = "\n".join(
        f"- {d['name']} ({d['price']} zł)" for d in order["dishes"]
    )

    msg.set_content(
f"""Nowe zamówienie!

Data: {order['date']}

Zamówione dania:
{dishes_text}

Suma: {order['total_price'] + order['discount']} zł
Rabat odbiór osobisty (-10%): -{order['discount']} zł
Do zapłaty: {order['total_price']} zł

Status: {order['status']}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


if __name__ == "__main__":
    app.run(debug=True)
