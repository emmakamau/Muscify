import unittest
from app.models import Review,User
from app import db

class TestReview(unittest.TestCase):

    def setUp(self):
        self.user_Adele = User(username = 'adele',password = 'stac101', email = 'muscify@test.com')
        self.new_review = Review(track_id=12,track_review='This Track Makes Me Feel Like Dancing',user =self.user_Adele)


    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.track_id,12)
        self.assertEquals(self.new_review.track_review,'This Track Makes Me Feel Like Dancing')
        self.assertEquals(self.new_review.user_id,self.user_Adele)


    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)


    def test_get_review_by_id(self):

        self.new_review.save_review()
        my_reviews = Review.get_reviews(12)
        self.assertTrue(len(my_reviews) == 1)