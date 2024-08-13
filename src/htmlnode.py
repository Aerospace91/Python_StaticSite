from textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    # Return a string the represents the HTML attributes of the node
    def props_to_html(self):
        props = ""
        for key, value in self.props.items():
            props += f' {key}="{value}"'
        return props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if tag is None and value is None:
            raise ValueError("At least one of tag or value must be specified")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.tag is None:
            return self.value
        elif self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

