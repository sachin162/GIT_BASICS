"""
Common Configuration Files
"""

from customer_details import customer_details


def get_configuration_based_on_customer_id(cust_id: int):
    """

    :param cust_id:
    :param key:
    :return:
    """
    return customer_details[cust_id]


def get_discount_percentage_based_on_deal_type(deal_type: str):
    """

    :param deal_type:
    :return:
    """
    if deal_type == "short":
        discount_precentage = 20
    else:
        discount_precentage = 35

    return discount_precentage
