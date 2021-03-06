import datetime
import pytz

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


from .models import Client, Order
from products.services import parse_cart_cookie


def create_valid_number(number: str):
    """This function is create valid view of client's number"""
    num = "".join(filter(str.isdigit, number))
    if len(num) < 10 or len(num) > 11 or num[-10] != '9':
        print(num)
        exit()
    phone = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*num[-9:])
    return phone


def validate_and_add_client(data: dict) -> dict:
    client_full_adress = data["full_adress"]
    clients_email = data["email"]
    valid_client_first_name = data["first_name"].capitalize()
    valid_client_last_name = data["last_name"].capitalize()
    valid_client_city = data["city"].capitalize()
    valid_client_number = create_valid_number(data["phone"])
    new_client = Client(first_name=valid_client_first_name,
                        last_name=valid_client_last_name,
                        city=valid_client_city, email=clients_email,
                        full_adress=client_full_adress, phone=valid_client_number
                        )
    new_client.save()
    return new_client


def create_order(request, data):
    """This function for create order"""
    client = validate_and_add_client(data)
    cart_products_from_function, cart_products_qty = parse_cart_cookie(request)
    cart_products = cart_products_from_function
    order_list = ""
    for i in range(len(cart_products)):
        order_list += str(cart_products_from_function[i].name) + \
            ": " + str(cart_products_qty[i]) + "\n"

    final_price = int(sum([cart_products_from_function[i].price * cart_products_qty[i]
                      for i in range(len(cart_products))]))
    comment = data["comment"]
    delivery = bool(data["delivery"])
    time = datetime.datetime.now().replace(
        tzinfo=pytz.timezone("UTC")).astimezone(tz=pytz.timezone("Europe/Moscow"))
    adress = data["full_adress"]
    new_order = Order(client=client,
                      order_list=order_list, final_price=final_price,
                      comment=comment, delivery=delivery,
                      time=time, adress=adress)
    new_order.save()
    new_order.products.set(cart_products)
    return new_order


@receiver(post_save, sender=Order)
def post_emails(sender, instance, **kwargs):
    """This signal is work when order is save"""
    context = {
        "message": instance.order_list,
        "name": instance.client.first_name
    }
    html_body = render_to_string("mail_templates/order.html", context)
    msg = EmailMultiAlternatives(subject="?????????? ?? ?????????????????????? ??????-??????????????????", to=[
                                 f'{instance.client.email}', "iglin1488@gmail.com"])
    msg.attach_alternative(html_body, "text/html")
    msg.send()
    print(f"{instance.client.email}")
