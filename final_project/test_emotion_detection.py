from EmotionDetection.emotion_detection import emotion_detector
import unittest

def func_result(statement):
    return(emotion_detector(statement)['dominant_emotion'])

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(func_result("I am glad this happened"), "joy")
        self.assertEqual(func_result("I am really mad about this"), "anger")
        self.assertEqual(func_result("I feel disgusted just hearing about this"), "disgust")
        self.assertEqual(func_result("I am so sad about this"), "sadness")
        self.assertEqual(func_result("I am really afraid that this will happen"), "fear")

if __name__ == "__main__":
    unittest.main()