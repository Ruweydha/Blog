import unittest
from app.models import Blogs, User
from app import db

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_ruweydha = User(username='ruweydha', password ='potato', email = 'ruweydhaabdinoor@gmail.com')
        self.new_blog = Blogs(title= 'Technology', content = 'Software development',user_id = self.user_ruweydha.id)

    def tearDown(self):
        Blogs.query.delete() 
        User.query.delete() 

    def test_check_instance_variables(self) :
        self.assertEquals(self.new_blog.title, 'Technology') 
        self.assertEquals(self.new_blog.content, 'Software development')  
        self.assertEquals(self.new_blog.user_id, self.user_ruweydha.id)  

    def test_save_blog(self):
        self.new_blog.save_blog()  
        self.assertTrue(len(Blogs.query.all())>0)  

    def test_get_blog_by_id(self):
        self.new_blog.save_blog() 
        got_blog = Blogs.get_blog(self.user_ruweydha.id) 
        self.assertTrue(len(got_blog)==1) 