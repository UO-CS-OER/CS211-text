"""A simplified version of the
document object model (DOM) structure
used in web browsers and other web
applications.
For Chapter 3, recursion the OO way.
"""

from typing import List


class DOMNode:
    """Abstract base class, defines the interface
    that concrete DOM node classes must conform to.
    """

    def __init__(self):
        raise NotImplementedError("Abstract constructor of DOMNode")


class Tagged(DOMNode):
    def __init__(self, tag: str, children: List[DOMNode] = []):
        self.tag = tag
        self.children = children

    def append(self, node: DOMNode):
        self.children.append(node)

    def __str__(self) -> str:
        """Text form is like HTML source code"""
        parts = [str(part) for part in self.children]
        return f"<{self.tag}> {' '.join(parts)} </{self.tag}>\n"


class Plain(DOMNode):
    """Plain text content is essentially just a string"""

    def __init__(self, text: str):
        self.text = text

    def append(self, text: str):
        self.text += text

    def __str__(self):
        return self.text


page = Tagged("html",
              [Tagged("head", [Tagged("title", [Plain("My Tremendous Novel")])]),
               Tagged("body", [Tagged("h1", [Plain("A Tail of Two Mice")]),
                               Tagged("h2", [Plain("By Little Charley Dickie")]),
                               Tagged("p", [Plain("It was the worst of cats."),
                                            Plain("Like, really bad.  Unbelievably bad.")]),
                               Tagged("h3", [Plain("Copyright 2020 by L.C.D.")])
                               ])  # End of body
               ])  # End of document

print(page)
