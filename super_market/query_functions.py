# -- coding: UTF-8 --

"""
*****************
Query Functions
*****************
Functions for querying from the POS database responses
Query 1: To get the products which are lesser than the user-defined value
Query 2: To get the transactions between a particular dates
Query 3: Branch with most no of transactions and print its details
Query 4: Staff who sold most no of products
"""

import logging
from collections import Counter

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger(__name__)


def update_stock(products, lower_value):
    """
    To check for the products with stock value lesser than the user input and print that the item has to stocked

    :param products: List of all the product details that contains products id and product quantity
    :type products: list

    :param lower_value: The least permissible value of stock
    :type lower_value: int

    :return: None
    """
    for product in products:
        if product["product_quantity"] < lower_value:  # user input from arg_parse
            LOGGER.info("%s to be stocked", product["product_id"])


def get_transactions_bw_dates(transactions, from_date, to_date):
    """
    To get the transactions from a particular to another particular date

    :param transactions: list of all transactions
    :type transactions: list

    :param from_date: Starting date
    :type from_date: datetime.datetime

    :param to_date: Ending date
    :type to_date: datetime.datetime

    :return: None
    """
    for transaction in transactions:
        if from_date.date() <= transaction["trans_date"].date() <= to_date.date():
            LOGGER.info(transaction)


def most_transactions_branch(transaction_data, branch_data):
    """
    To print the details of the branch with most no of transactions

    :param transaction_data: list of all transactions
    :type transaction_data: list

    :param branch_data: Branch code and branch address
    :type branch_data: list

    :return: None
    """
    trans_branches = []
    for transaction in transaction_data:
        trans_branches.append(transaction["branch_details"])

    most_trans_branch = Counter(trans_branches).most_common(1)
    for branch in branch_data:
        if branch["branch_id"] == most_trans_branch[0][0]:
            LOGGER.info(" %s has the most no of transactions and the address is %s ", most_trans_branch[0][0],
                        branch["branch_address"])


def staff_most_products(staff_data, transaction_data, purchase_data):
    """
    To find which staff sold the most no of products

    :param staff_data: list of all staff details
    :type staff_data: list

    :param transaction_data: list of all transactions
    :type transaction_data: list

    :param purchase_data: list of all purchase details
    :type purchase_data: list

    :return: None
    """
    no_of_prods_transactions = []
    for purchase in purchase_data:
        no_of_products = len(purchase["product_details"])
        no_of_prods_transactions.append(dict(trans_id=purchase["trans_details"], no_of_products=no_of_products))

    most_products_staff = []
    for transaction in transaction_data:
        for data in no_of_prods_transactions:
            if transaction["trans_id"] == data["trans_id"]:
                most_products_staff.append(dict(no_of_products=data["no_of_products"],
                                                staff_id=transaction["staff_details"]))

    staff_ids = [staff["staff_id"] for staff in staff_data]
    final_dict = {}
    for staff_id in staff_ids:
        final_dict[staff_id] = 0

    for data in most_products_staff:
        for staff in staff_ids:
            if data["staff_id"] == staff:
                final_dict[data["staff_id"]] += data["no_of_products"]
    keymax = max(final_dict, key=final_dict.get)
    LOGGER.info("%s has sold the maximum no of products", keymax)
