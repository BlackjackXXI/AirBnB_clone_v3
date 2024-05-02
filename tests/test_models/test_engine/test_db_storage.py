class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
    def allReturnDict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
    def allNoClass(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
    def new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
    def save(self):
        """Test that save properly saves objects to file.json"""


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_get(self):
        """Test that get returns specific object, or none"""
        newState = State(name="New York")
        newState.save()
        newUser = User(email="bob@foobar.com", password="password")
        newUser.save()
        self.assertIs(newState, models.storage.get("State", newState.id))
        self.assertIs(None, models.storage.get("State", "blah"))
        self.assertIs(None, models.storage.get("blah", "blah"))
        self.assertIs(newUser, models.storage.get("User", newUser.id))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_count(self):
        """add new object to db"""
        startCount = models.storage.count()
        self.assertEqual(models.storage.count("Blah"), 0)
        newState = State(name="Montevideo")
        newState.save()
        newUser = User(email="ralexrivero@gmail.com.com", password="dummypass")
        newUser.save()
        self.assertEqual(models.storage.count("State"), startCount + 1)
        self.assertEqual(models.storage.count(), startCount + 2)