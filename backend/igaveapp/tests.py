from django.test import TestCase
from django.contrib.auth.models import User
from igaveapp.models import Receipt
from datetime import date


class BasicTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)


class UserTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password'))


class ReceiptTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='receiptuser', password='password')

    def test_receipt_creation(self):
        receipt = Receipt.objects.create(
            user=self.user,
            store_name="Test Store",
            date=date.today(),
            total_amount=100.50
        )
        self.assertEqual(receipt.store_name, "Test Store")
        self.assertEqual(receipt.total_amount, 100.50)
        self.assertEqual(receipt.user, self.user)
