import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("hello world", "text", url="https://boot.dev")
        node2 = TextNode("hello world", "text", url="https://boot.dev")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("hello world", "text", url="https://boot.dev")
        node2 = TextNode("hello world", "text")
        self.assertNotEqual(node, node2)

    def test_texttype_not_eq(self):
        node = TextNode("hello world", "text")
        node2 = TextNode("hello world", "bold")
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("hello world", "text")
        node2 = TextNode("hello", "text")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("hello world", "text", url="https://boot.dev")
        self.assertEqual(repr(node), "TextNode(hello world, text, https://boot.dev)")

if __name__ == "__main__":
    unittest.main()