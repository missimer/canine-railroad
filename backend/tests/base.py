from unittest import TestCase
from app import app, db

class BaseTestCase(TestCase):
  def setUp(self):
    self.app = app.test_client()
    self.db = db
    self.db.drop_all()
    self.db.create_all()
