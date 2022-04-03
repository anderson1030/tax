import unittest
import app

class test(unittest.TestCase):

    def test_single(self):
        #Result From our app
        result = app.single(200000)
        result2 = app.single(300000)
        result3 = app.single(400000)
        result4 = app.single(500000)
        result5 = app.single(600000)
        result6 = app.single(700000)
        result7 = app.single(800000)
        result8 = app.single(900000)
        result8 = app.single(1000000)
        result9 = app.single(2000000)
        result10 = app.single(3000000)
        result11 = app.single(4000000)
        result12 = app.single(5000000)
        result13 = app.single(10000000)
        result14 = app.single(30000000)
        result15 = app.single(50000000)

        
        #Result From government tax computation
        self.assertEqual(result, 1480)
        self.assertEqual(result2, 9420)
        self.assertEqual(result3, 24500)
        self.assertEqual(result4, 41500)
        self.assertEqual(result5, 58500)
        self.assertEqual(result6, 75500)
        self.assertEqual(result7, 92500)
        self.assertEqual(result8, 126500)
        self.assertEqual(result9, 296500)
        self.assertEqual(result10, 447300)
        self.assertEqual(result11, 597300)
        self.assertEqual(result12, 747300)
        self.assertEqual(result13, 1497300)
        self.assertEqual(result14, 4497300)
        self.assertEqual(result15, 7497300)
    
    def test_married(self):
        #Result From our app
        result = app.married(200000,1000000)
        result2 = app.married(300000,900000)
        result3 = app.married(400000,800000)
        result4 = app.married(500000,700000)
        result5 = app.married(600000,600000)
        result6 = app.married(700000,500000)
        result7 = app.married(800000,400000)
        result8 = app.married(900000,300000)
        result9 = app.married(1000000,200000)
        result10 = app.married(200000,0)
        result11 = app.married(200000,2000)
        result12 = app.married(200000,1000000)
        result13 = app.married(23333,500000)
        result14 = app.married(0,0)
        result15 = app.married(5000000,5000000)


        #Result From government tax computation
        self.assertEqual(result, 127980)
        self.assertEqual(result2, 118920)
        self.assertEqual(result3, 117000)
        self.assertEqual(result4, 117000)
        self.assertEqual(result5, 117000)
        self.assertEqual(result6, 117000)
        self.assertEqual(result7, 117000)
        self.assertEqual(result8, 118920)
        self.assertEqual(result9, 127980)
        self.assertEqual(result10, 0)
        self.assertEqual(result11, 0)
        self.assertEqual(result12, 127980)
        self.assertEqual(result13, 23026)
        self.assertEqual(result14, 0)
        self.assertEqual(result15, 1494600)

if __name__ == '__main__':
    unittest.main()