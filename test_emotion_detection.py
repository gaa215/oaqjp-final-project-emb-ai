from emotion_detection import emotion_detector
from emotion_detection import emotion_predictor
import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_predictor(self):
        result_1 = emotion_predictor(emotion_detector("I am happy this happened"))
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_predictor(emotion_detector("I am very angry."))
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_predictor(emotion_detector("I am feeling disgusted here"))
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        result_4 = emotion_predictor(emotion_detector("I am feeling sad for it"))
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_predictor(emotion_detector("I have fear if it is not completed."))
        self.assertEqual(result_5['dominant_emotion'], 'fear')
unittest.main()

