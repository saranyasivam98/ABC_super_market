# -- coding: UTF-8 --

""" Main file for unit conversion"""
import logging
import logging.config
import json
from datetime import datetime

from marshmallow import ValidationError
from super_market.schema_classes import ProductSchema, TransactionSchema, BranchSchema, PurchaseSchema, \
    StaffSchema, CustomerSchema
from super_market.query_functions import update_stock, get_transactions_bw_dates, most_transactions_branch, \
    staff_most_products

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger(__name__)
LOGGER_CONFIG_PATH = 'config/logging.json'


def setup_logging(default_path=LOGGER_CONFIG_PATH):
    """
    Function Description: To setup logging using the json file
    :param default_path: Path of the configuration file
    :type default_path: str
    """
    with open(default_path, 'rt') as file:
        config = json.load(file)
    logging.config.dictConfig(config)


def main():
    """Main Function"""
    setup_logging()
    with open("products.json") as file:
        products_data = json.load(file)

    with open("branch.json") as file:
        branch_data = json.load(file)

    with open("staff.json") as file:
        staff_data = json.load(file)

    with open("customers.json") as file:
        customers_data = json.load(file)

    with open("transactions.json") as file:
        transaction_data = json.load(file)

    with open("purchase.json") as file:
        purchase_data = json.load(file)

    try:
        products_data = ProductSchema(many=True).load(products_data)
    except ValidationError as err:
        LOGGER.error(err.messages)

    transaction_data = TransactionSchema(many=True).load(transaction_data)
    branch_data = BranchSchema(many=True).load(branch_data)
    purchase_data = PurchaseSchema(many=True).load(purchase_data)
    staff_data = StaffSchema(many=True).load(staff_data)
    customer_class = CustomerSchema(many=True).load(customers_data)
    LOGGER.info(type(customer_class[0]))

    # Query 1:
    update_stock(products_data, 500)

    # Query 2:
    from_date = datetime.strptime("01-03-2021", "%d-%m-%Y")
    to_date = datetime.strptime("03-03-2021", "%d-%m-%Y")

    get_transactions_bw_dates(transaction_data, from_date, to_date)

    # Query 3:
    most_transactions_branch(transaction_data, branch_data)

    # Query 4: Staff who sold the most no of products
    staff_most_products(staff_data, transaction_data, purchase_data)


if __name__ == '__main__':
    main()
