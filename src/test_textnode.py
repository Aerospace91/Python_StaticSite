import unittest

from textnode import TextNode, text_node_to_html_node

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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("hello world", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "hello world")

    def test_bold(self):
        node = TextNode("hello world", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "hello world")
    
    def test_italic(self):
        node = TextNode("hello world", "italic")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "hello world")

    def test_code(self):
        node = TextNode("hello world", "code")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "hello world")
    
    def test_link(self):
        node = TextNode("hello world", "link", url="https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "hello world")
        self.assertEqual(html_node.props["href"], "https://boot.dev")

    def test_image(self):
        node = TextNode("hello world", "image", url="https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://boot.dev", "alt": "hello world"},
        )



if __name__ == "__main__":
    unittest.main()