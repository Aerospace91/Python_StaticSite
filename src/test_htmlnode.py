import unittest
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "world", [TextNode("hello", "text", url="https://boot.dev")], {"href": "https://boot.dev", "target": "_blank"})
        node2 = HTMLNode("div", "world", [TextNode("hello", "text", url="https://boot.dev")], {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("div", "world", [TextNode("hello", "text", url="https://boot.dev")], {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode("div", "world", [TextNode("hello", "text", url="https://boot.dev")], {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(div, world, [TextNode(hello, text, https://boot.dev)], {'href': 'https://boot.dev', 'target': '_blank'})")

    def test_to_html(self):
        node = LeafNode("div", "world")
        self.assertEqual(node.to_html(), "<div>world</div>")
    
    def test_to_html2(self):
        node = LeafNode("div", "world", {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<div href="https://boot.dev" target="_blank">world</div>')

if __name__ == "__main__":
    unittest.main()