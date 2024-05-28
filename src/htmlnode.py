class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        result = ""
        if self.props == None:
            return result
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value assigned for leaf node")
        elif not self.tag:
            return f'{self.value}'
         
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

