from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
# Create your tests here.

class TestUser(TestCase):
    
    def test_createUserAndProfileValid(self):
        username = "testUser70"
        password = "newPass22"
        print("\n\nTestCase 1.1: Create Valid User and Profile Test:")
        print("---------------------------------")
        print("Creating user...")
        user1 = User(username=username, password=password)
        user1.save()
        print("Searching for matching Profile...")
        record = Profile.objects.get(user=user1).user

        self.assertTrue(user1.username)
        self.assertTrue(user1.password)
        self.assertEqual(record.username, user1.username)
        self.assertEqual(record.password, user1.password)
        print("==================================\n\n")

    def test_createUserAndProfileInvalidPassword(self):
        username = "testUser70"
        print("\n\nTestCase 1.2: Create User Without Password Test:")
        print("---------------------------------")
        print("Creating user...")
        user1 = User(username=username)
        user1.save()
        
        print("Checking for username and password...")
        print("Raising assertion error...")
        self.assertTrue(user1.username)
        self.assertRaises(AssertionError, self.assertTrue, user1.password)
        print("==================================\n\n")

    def test_createUserAndProfileInvalidUsername(self):
        password = "newPass22"
        print("\n\nTestCase 1.2: Create User Without Username Test:")
        print("---------------------------------")
        print("Creating user...")
        user1 = User(password=password)
        user1.save()
        
        print("Checking for username and password...")
        print("Raising assertion error...")
        self.assertRaises(AssertionError, self.assertTrue, user1.username)
        self.assertTrue(user1.password)
        
        print("==================================\n\n")

    def test_makeChangesToNewProfile(self):
        print("\n\nTestCase 2.1: Make Changes to New Profile Test:")
        print("---------------------------------")
        print("Creating user...")
        user1 = User(username="testUser70", password="newPass22")
        user1.save()
        print("Searching for matching Profile...")
        record = Profile.objects.get(user=user1)

        self.assertTrue(user1.username)
        self.assertTrue(user1.password)
        self.assertEqual(record.user.username, user1.username)
        self.assertEqual(record.user.password, user1.password)

        print("Inserting changes to profile...")
        record.firstName = "Bob"
        record.lastName = "Barley"
        record.weight = 200
        print("Checking for data save in profile...")
        self.assertTrue(record.firstName)
        self.assertTrue(record.lastName)
        self.assertTrue(record.weight)
        print("Checking for equal saved value to intended value...")
        self.assertListEqual(["Bob", "Barley", 200], [record.firstName, record.lastName, record.weight])
        print("==================================\n\n")

    def test_makeBadChangesToNewProfile(self):
        print("\n\nTestCase 2.2: Make Changes to New Profile Test:")
        print("---------------------------------")
        print("Creating user...")
        user1 = User(username="testUser70", password="newPass22")
        user1.save()
        print("Searching for matching Profile...")
        record = Profile.objects.get(user=user1)

        self.assertTrue(user1.username)
        self.assertTrue(user1.password)
        self.assertEqual(record.user.username, user1.username)
        self.assertEqual(record.user.password, user1.password)

        print("Inserting bad changes to profile...")
        record.firstName = "Bob"
        record.lastName = "Barley"
        record.weight = "200"
        print("Checking for data save in profile...")
        self.assertTrue(record.firstName)
        self.assertTrue(record.lastName)
        self.assertTrue(record.weight)
        print("Checking for incorrect datatype...")
        self.assertNotEqual(200, record.weight)
        print("==================================\n\n")
    
    def test_makeChangesToProfileFields(self):
        print("\n\nTestCase 2.1: Make Changes to New Profile Test:")
        print("---------------------------------")
        print("Creating user...")
        user1 = User(username="testUser70", password="newPass22")
        user1.save()
        print("Searching for matching Profile...")
        record = Profile.objects.get(user=user1)

        self.assertTrue(user1.username)
        self.assertTrue(user1.password)
        self.assertEqual(record.user.username, user1.username)
        self.assertEqual(record.user.password, user1.password)

        print("Inserting changes to profile...")
        record.firstName = "Bob"
        record.lastName = "Barley"
        record.weight = 200
        print("Checking for data save in profile...")
        self.assertTrue(record.firstName)
        self.assertTrue(record.lastName)
        self.assertTrue(record.weight)
        print("Checking for equal saved value to intended value...")
        self.assertListEqual(["Bob", "Barley", 200], [record.firstName, record.lastName, record.weight])
        print("Editing profile fields...")
        record.lastName = "Marley"
        record.weight = 190
        print("Checking for equal saved value to intended value...")
        self.assertListEqual(["Bob", "Marley", 190], [record.firstName, record.lastName, record.weight])
        print("==================================\n\n")