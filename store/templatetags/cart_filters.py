from django import template

register = template.Library()

#Decorator to specify this func is a filter
#set name only if want to use this fuction with different name, here it i am going with same name which is not necessary
@register.filter(name="is_in_cart")
def is_in_cart(product,cart):
    if str(product.id) in cart.keys(): # cart.keys() will have a list of keys in string format which will never match with integer product.id
        return True
    else:
        return False

# This function is returing dictionary value (quantity of a particular item) by passing key in cart dictionary 
@register.filter
def product_count_in_cart(product,cart):
    return cart[str(product.id)]

@register.filter
def total_price(product,cart):
    return product.product_price * product_count_in_cart(product,cart)

@register.filter
def total_cart_price(product,cart):
    sum = 0
    for amount in product:
        sum += total_price(amount,cart)
    return sum

@register.filter
def currency(number):
    return "₹"+str(number)