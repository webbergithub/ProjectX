import unittest

#5 Main functions in main.py 
def length(lyrics_content):
    return len((lyrics_content.split()))

def love_song(lyrics_content,keywords):
    return len(keywords.intersection(lyrics_content.split()))

def mood(lyrics_content,keywords):
    return len(keywords.intersection(lyrics_content.split()))

def kid_safe(lyrics_content,keywords):
    return len(keywords.intersection(lyrics_content.split()))

def complexity(lyrics_content):
    return len(set(lyrics_content.split()))


        
    
class TestStringMethods(unittest.TestCase):  # inherit from TestCase

    # Each test is a method
    def test_length(self):  # name each test "test_<somthing>"
        self.assertEqual(length("this is a test"), 4)

    def test_love_song(self):
        self.assertEqual(love_song("i love you so much",{"love","i"}), 2)

    def test_mood(self):
        self.assertEqual(mood("i love you so much",{"so","much"}), 2)
    
    def test_kid_safe(self):
        self.assertEqual(kid_safe("shark doo doo doo",{"doo"}), 1)
    
    def test_complexity(self):
        self.assertEqual(complexity("shark doo doo doo"), 2)


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
# Run each test in suite
unittest.TextTestRunner().run(suite)


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
# Run each test in suite
unittest.TextTestRunner().run(suite)