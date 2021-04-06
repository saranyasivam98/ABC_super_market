# -- coding: UTF-8 --

"""
*****************
Schema Classes
*****************
Schema classes for validating the responses from POS database """

from marshmallow import Schema, fields, validate, post_load

__author__ = 'saranya@gyandata.com'


class Staff:
    """
    To store the staff details

    :ivar staff_id: The ID of the staff
    :vartype staff_id: :class:`marshmallow.fields.Str`

    :ivar staff_name: Name of the staff
    :vartype staff_name: :class:`marshmallow.fields.Str`

    :ivar staff_email = Email of the staff
    :vartype staff_email: :class:`marshmallow.fields.Email`
    """
    def __init__(self, staff_id, staff_name, staff_email):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_email = staff_email


class StaffSchema(Schema):
    """
    Schema class for staff details

    :ivar staff_id: The ID of the staff
    :vartype staff_id: :class:`marshmallow.fields.Str`

    :ivar staff_name: Name of the staff
    :vartype staff_name: :class:`marshmallow.fields.Str`

    :ivar staff_email = Email of the staff
    :vartype staff_email: :class:`marshmallow.fields.Email`
    """
    staff_id = fields.Str()
    staff_name = fields.Str()
    staff_email = fields.Email()

    @post_load
    def make_staff(self, data, **kwargs):
        return Staff(**data)


class Customer:
    """
    To store the customer details

    :ivar customer_id: The ID of the customer
    :vartype customer_id: :class:`marshmallow.fields.Str`

    :ivar customer_name: Name of the customer
    :vartype customer_name: :class:`marshmallow.fields.Str`

    :ivar customer_email = Email of the customer
    :vartype customer_email: :class:`marshmallow.fields.Str`

    :ivar customer_ph_no = Phone Number of the customer
    :vartype customer_ph_no: :class:`marshmallow.fields.Number`
    """
    def __init__(self, customer_id, customer_name, customer_email, customer_ph_no):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_ph_no = customer_ph_no


class CustomerSchema(Schema):
    """
    Schema class for customer details

    :ivar customer_id: The ID of the customer
    :vartype customer_id: :class:`marshmallow.fields.Str`

    :ivar customer_name: Name of the customer
    :vartype customer_name: :class:`marshmallow.fields.Str`

    :ivar customer_email = Email of the customer
    :vartype customer_email: :class:`marshmallow.fields.Email`

    :ivar customer_ph_no = Phone Number of the customer
    :vartype customer_ph_no: :class:`marshmallow.fields.Number`
    """
    # customer_id = Primary Key
    # customer_details
    customer_id = fields.Str()
    customer_name = fields.Str()
    customer_ph_no = fields.Number()
    customer_email = fields.Email()

    @post_load
    def make_customer(self, data, **kwargs):
        return Customer(**data)


class Branch:
    """
    To store the customer details

    :ivar branch_id: The ID of the branch
    :vartype branch_id: :class:`marshmallow.fields.Str`

    :ivar branch_address: Address of the branch
    :vartype branch_address: :class:`marshmallow.fields.Str`
    """
    def __init__(self, branch_id, branch_address):
        self.branch_id = branch_id
        self.branch_address = branch_address


class BranchSchema(Schema):
    """
    Schema class for customer details

    :ivar branch_id: The ID of the branch
    :vartype branch_id: :class:`marshmallow.fields.Str`

    :ivar branch_address: Address of the branch
    :vartype branch_address: :class:`marshmallow.fields.Str`
    """
    # branch_id = Foreign Key
    # branch_details
    branch_id = fields.Str()
    branch_address = fields.Str()

    @post_load
    def make_branch(self, data, **kwargs):
        return Branch(**data)


class Transaction:
    """
    To store the transaction details

    :ivar trans_id: The ID of the transaction
    :vartype trans_id: :class:`marshmallow.fields.Str`

    :ivar customer_details: The ID of the customer for whom the transaction was did
    :vartype customer_details: :class:`marshmallow.fields.Str`

    :ivar trans_date: The date of the transaction
    :vartype trans_date: :class:`marshmallow.fields.Datetime`

    :ivar staff_details: The ID of the staff who did the transaction
    :vartype customer_details: :class:`marshmallow.fields.Str`

    :ivar branch_details: The ID of the branch where the transaction happened
    :vartype branch_details: :class:`marshmallow.fields.Str`
    """
    def __init__(self, trans_id, trans_date, customer_details, staff_details, branch_details):
        self.trans_id = trans_id
        self.trans_date = trans_date
        self.customer_details = customer_details
        self.staff_details = staff_details
        self.branch_details = branch_details


class TransactionSchema(Schema):
    """
    Schema class for transaction details

    :ivar trans_id: The ID of the transaction
    :vartype trans_id: :class:`marshmallow.fields.Str`

    :ivar customer_details: The ID of the customer for whom the transaction was did
    :vartype customer_details: :class:`marshmallow.fields.Str`

    :ivar trans_date: The date of the transaction
    :vartype trans_date: :class:`marshmallow.fields.Datetime`

    :ivar staff_details: The ID of the staff who did the transaction
    :vartype customer_details: :class:`marshmallow.fields.Str`

    :ivar branch_details: The ID of the branch where the transaction happened
    :vartype branch_details: :class:`marshmallow.fields.Str`
    """
    trans_id = fields.Str()
    trans_date = fields.DateTime()
    customer_details = fields.Str()
    staff_details = fields.Str()
    branch_details = fields.Str()

    @post_load
    def make_transaction(self, data, **kwargs):
        return Transaction(**data)


class Product:
    """
    To store the product details
    :ivar product_id: The ID of the product
    :vartype product_id: :class:`marshmallow.fields.Str`

    :ivar product_quantity: The quantity that is available
    :vartype product_quantity: :class:`marshmallow.fields.Int`
    """
    def __init__(self, product_id, product_quantity):
        self.product_id = product_id
        self.product_quantity = product_quantity


class ProductSchema(Schema):
    """
    Schema class for product details

    :ivar product_id: The ID of the product
    :vartype product_id: :class:`marshmallow.fields.Str`

    :ivar product_quantity: The quantity that is available
    :vartype product_quantity: :class:`marshmallow.fields.Int`
    """
    product_id = fields.Str()
    product_quantity = fields.Int(validate=validate.Range(min=0), error_messages={"message": "Fill up the stock"})

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)


class Purchase:
    """
    To store the purchase details

    :ivar purchase_id: The ID of the purchase
    :vartype purchase_id: :class:`marshmallow.fields.Str`

    :ivar trans_id: The ID of the transaction
    :vartype trans_id: :class:`marshmallow.fields.Str`

    :ivar product_id: The ID of the product
    :vartype product_id: list[:class:`marshmallow.fields.Str`]
    """
    def __init__(self, purchase_id, trans_details, product_details):
        self.purchase_id = purchase_id
        self.trans_details = trans_details
        self.product_details = product_details


class PurchaseSchema(Schema):
    """
    Schema class for purchase details

    :ivar purchase_id: The ID of the purchase
    :vartype purchase_id: :class:`marshmallow.fields.Str`

    :ivar trans_id: The ID of the transaction
    :vartype trans_id: :class:`marshmallow.fields.Str`

    :ivar product_id: The ID of the product
    :vartype product_id: list[:class:`marshmallow.fields.Str`]
    """

    purchase_id = fields.Str()
    trans_details = fields.Str()
    product_details = fields.List(fields.Str)

    @post_load
    def make_purchase(self, data, **kwargs):
        return Purchase(**data)
