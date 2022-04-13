from django.db import models


class Transaction(models.Model):
    txd_id = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)


class Customer(models.Model):
    pass


class Conversation(models.Model):
    pass


class BankAccount(models.Model):
    pass


class Bank(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class BankBranch(models.Model):
    name = models.CharField(max_length=50)
    ifse_code = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    bank_name = models.ForeignKey("Bank", verbose_name="name", on_delete=models.CASCADE)
