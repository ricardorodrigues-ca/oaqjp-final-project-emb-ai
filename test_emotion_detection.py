"""Required live Watson tests. Run only inside the authorized Theia lab."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Validate all five emotions using the course's prescribed statements."""

    def test_prescribed_statements(self):
        """Check each required statement against the actual Watson service."""
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for statement, expected in cases.items():
            with self.subTest(statement=statement):
                self.assertEqual(emotion_detector(statement)["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
