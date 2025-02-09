"""
Module to implement main features for dish
"""

from common_configuration_for_all_customer import (
    get_configuration_based_on_customer_id,
    get_discount_percentage_based_on_deal_type,
)


def get_total_amount(no_of_items: int):
    """

    :param no_of_items:
    """
    total_amount = no_of_items * 100
    return total_amount


def calculate_discount_amount(cust_id: int, total_amount: int):
    """

    :param cust_id:
    :param total_amount:
    :return:
    """
    cust_config = get_configuration_based_on_customer_id(cust_id)
    percentage = get_discount_percentage_based_on_deal_type(
        cust_config["deal_type"]
    )
    discount_amount = total_amount - ((percentage / 100) * total_amount)
    return discount_amount


def calculate_total_cart_amount(cust_id: int, no_of_items: int):
    """
    :param cust_id:
    :param no_of_items:
    :return:

    """
    total = get_total_amount(no_of_items)
    dicount_amount = calculate_discount_amount(cust_id, total)
    final_cart_val = total - dicount_amount
    return final_cart_val
