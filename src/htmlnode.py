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

    def __eq__(self, other):
        if self.tag == other.tag:
            if self.value == other.value:
                if self.children == other.children:
                    if self.props == other.props:
                        return True
        return False

    def __repr__(self):
        return f'HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value assigned for leaf node")
        elif not self.tag:
            return f'{self.value}'
         
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HtmlNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag argument required for ParentNode")
        elif not self.children:
            raise ValueError("children argument required for ParentNode")

        result = f'<{self.tag}>'
        for child in self.children:
            result += child.to_html()
        result += f'</{self.tag}>'
        return result

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'
