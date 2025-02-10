import unittest
from emotion_detection import emotion_detector, predict_emotions

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result_1 = predict_emotions(emotion_detector("I am happy this happened"))
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = predict_emotions(emotion_detector("I am very angry."))
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = predict_emotions(emotion_detector("I am feeling disgusted here"))
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        result_4 = predict_emotions(emotion_detector("I am feeling sad for it"))
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = predict_emotions(emotion_detector("I have fear if it is not completed."))
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
