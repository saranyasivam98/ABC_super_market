# -- coding: UTF-8 --

"""
*****************
Schema Classes
*****************
Schema classes for validating the responses from POS database """

from marshmallow import Schema, fields, validate, post_load

__author__ = 'saranya@gyandata.com'


class Customer:
    def __init__(self, customer_id, customer_name, customer_email, customer_ph_no):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_ph_no = customer_ph_no


class StaffSchema(Schema):
    """
    To store the staff details

    :ivar staff_id: The ID of the staff
    :vartype staff_id: fields.Str

    :ivar staff_name: Name of the staff
    :vartype staff_name: fields.Str

    :ivar staff_email = Email of the staff
    :vartype staff_email: fields.Email
    """
    staff_id = fields.Str()
    staff_name = fields.Str()
    staff_email = fields.Email()


class CustomerSchema(Schema):
    """
    To store the customer details

    :ivar customer_id: The ID of the customer
    :vartype customer_id: fields.Str

    :ivar customer_name: Name of the customer
    :vartype customer_name: fields.Str

    :ivar customer_email = Email of the customer
    :vartype customer_email: fields.Email

    :ivar customer_ph_no = Phone Number of the customer
    :vartype customer_ph_no: fields.Number
    """
    # customer_id = Primary Key
    # customer_details
    customer_id = fields.Str()
    customer_name = fields.Str()
    customer_ph_no = fields.Number()
    customer_email = fields.Email()

    @post_load
    def make_staff(self, data):
        return Customer(**data)


class BranchSchema(Schema):
    """
    To store the customer details

    :ivar branch_id: The ID of the branch
    :vartype branch_id: fields.Str

    :ivar branch_address: Address of the branch
    :vartype branch_address: fields.Str
    """
    # branch_id = Foreign Key
    # branch_details
    branch_id = fields.Str()
    branch_address = fields.Str()


class TransactionSchema(Schema):
    """
    To store the transaction details

    :ivar trans_id: The ID of the transaction
    :vartype trans_id: fields.Str

    :ivar customer_details: The ID of the customer for whom the transaction was did
    :vartype customer_details: fields.Str

    :ivar trans_date: The date of the transaction
    :vartype trans_date: fields.Datetime

    :ivar staff_details: The ID of the staff who did the transaction
    :vartype customer_details: fields.Str

    :ivar branch_details: The ID of the branch where the transaction happened
    :vartype branch_details: fields.Str

    """
    trans_id = fields.Str()
    trans_date = fields.DateTime()
    customer_details = fields.Str()
    staff_details = fields.Str()
    branch_details = fields.Str()


class ProductSchema(Schema):
    """
    To store the product details
    :ivar product_id: The ID of the product
    :vartype product_id: fields.Str

    :ivar product_quantity: The quantity that is available
    :vartype product_quantity: fields.Int
    """
    # product_id = Primary Key
    # product_details
    product_id = fields.Str()
    product_quantity = fields.Int(validate=validate.Range(min=0), error_messages={"message": "Fill up the stock"})


class PurchaseSchema(Schema):
    """
    To store the purchase details

    :ivar purchase_id: The ID of the purchase
    :vartype purchase_id: fields.Str

    :ivar trans_id: The ID of the transaction
    :vartype trans_id: fields.Str

    :ivar product_id: The ID of the product
    :vartype product_id: list[fields.Str]
    """

    purchase_id = fields.Str()
    trans_details = fields.Str()
    product_details = fields.List(fields.Str)
