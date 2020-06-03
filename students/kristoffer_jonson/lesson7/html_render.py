#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

        if kwargs is not None:
            self.attributes = kwargs
        else:
            self.attributes = {}

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=''):
    # loop through the list of contents:
        out_file.write(cur_ind + self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
                out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())
        out_file.write("\n")

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self):
        close_tag = '</{}>'.format(self.tag)
        return close_tag

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind = ''):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file, cur_ind = ''):
    # loop through the list of contents:
        out_file.write(cur_ind + self._open_tag())
        out_file.write(cur_ind + self.indent + self.contents[0])
        out_file.write(cur_ind + self._close_tag())
    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    def render(self, outfile, cur_ind = ''):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(cur_ind + tag)
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h{}'.format(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"

