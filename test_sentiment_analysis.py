from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

def func_result(statement):
    return(sentiment_analyzer(statement)['label'])

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(func_result("I love working with Python"), "SENT_POSITIVE")
        self.assertEqual(func_result("I hate working with Python"), "SENT_NEGATIVE")
        self.assertEqual(func_result("I am working with Python"), "SENT_NEUTRAL")
        self.assertEqual(func_result("I am neutral with Python"), "SENT_NEUTRAL")

if __name__ == '__main__':
    unittest.main()