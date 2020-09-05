import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.new_account = Account("Anna","Adhiambo","0758579812","annaadhiambo01@gmail.com","AnnaAdhiambo","12345")
    def test_init(self):
        self.assertEqual(self.new_account.first_name,"Anna")
        self.assertEqual(self.new_account.last_name,"Adhiambo")
        self.assertEqual(self.new_account.phone_number,"0758579812")
        self.assertEqual(self.new_account.email,"annaadhiambo01@gmail.com")
        self.assertEqual(self.new_account.username,"AnnaAdhiambo")
        self.assertEqual(self.new_account.password,"12345")

    def test_save_account(self):
        self.new_account.test_save_account()
        self.assertEqual(len(Account.account_list),1)



if __name__ == "__main__":
    unittest.main()            