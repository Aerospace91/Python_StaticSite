import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()