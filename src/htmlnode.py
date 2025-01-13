

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ""
        for prop in self.props:
            html_string += f" {prop}=\"{self.props[prop]}\""
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    # do make a check if the constructor is designed as expected
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            if self.props is not None:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"
