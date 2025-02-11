import unittest
from emotion_detection import emotion_detector  # Correct import

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector_joy(self):
        result = emotion_detector("I am happy this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        result = emotion_detector("I am very angry.")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        result = emotion_detector("I am feeling disgusted here")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_emotion_detector_sadness(self):
        result = emotion_detector("I am feeling sad for it")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        result = emotion_detector("I have fear if it is not completed.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()