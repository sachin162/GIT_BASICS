"""
Module for Dish Feature 2 implementation
"""


def get_recommendations_based_on_customer_profile(customer_profile: str):
    """

    :param customer_profile:
    :return:
    """
    recommendation = None
    if customer_profile == "Tech":
        recommendation = "Tech Recommendation"
    elif customer_profile == "Gas":
        recommendation = "Oil Industry Recommendation"
    elif customer_profile == "Telco":
        recommendation = "5G Recommendation"
    return recommendation
