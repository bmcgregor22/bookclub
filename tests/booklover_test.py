import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        test1 = BookLover('Bill','Bill@gmail.com','Science Fiction')
        test1.add_book("2001 Space Odyssey",2)
        print (test1.book_list)

        #test
        expected = "2001 Space Odyssey"
        message = " The test result is false."
        self.assertEqual(test1.book_list['book_name'].loc[test1.book_list.index[0]], expected)



    def test_2_add_book(self):
         test2 = BookLover('Steve','Steve@gmail.com','Philosophy')
         test2.add_book("The Fountainhead",5)
         test2.add_book("The Fountainhead",5)
         print (test2.book_list)
         result=len(test2.book_list[test2.book_list['book_name'] == "The Fountainhead"])

        #test
         expected = 1
         message = " The Test Result is False"
         self.assertEqual(result,expected)


    def test_3_has_read(self):
        test3 = BookLover('Donald','Donald@gmail.com','Business')
        test3.add_book("The Art of the Deal", 5)
        print (test3.book_list)
        result = test3.has_read("The Art of the Deal")
        message = "Test Result Was not True"

        #test
        expected = True
        self.assertTrue(result,message)

    def test_4_has_read(self):
       test4 = BookLover('Joe','Joe@gmail.com','Politics')
       test4.add_book("My Life in Politics",2)
       print(test4.book_list)
       result = test4.has_read("Atlas Shrugged")

       #test
       expected = False
       self.assertFalse(result, expected)

    def test_5_num_books_read(self):
        test5 = BookLover('Sam',"Sam@gmail.com",'Satire')
        test5.add_book("To Kill a Mocking Bird", 3)
        test5.add_book("Treasure Island", 2)
        print (test5.book_list)

        #test
        expected = 2
        self.assertTrue(test5.num_books_read, expected)

    def test_6_fav_books(self):
       test6 = BookLover("Steven",'steven@gmail.com','History')
       test6.add_book("Seven Habits of Highly Successful People",4)
       test6.add_book("War and Peace", 5)
       test6.add_book("The Art of War", 1)
       test6.add_book("The Sun Also Rises", 2)
       print(test6.fav_books())

       #test
       expected = 2
       self.assertTrue(len(test6.fav_books()),expected)


if __name__ == '__main__':
    unittest.main(verbosity=3)
