from xml.etree.ElementTree import Element
import markdown


class MathPattern(markdown.inlinepatterns.Pattern):
    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(self, r'(?<!\\)(\$\$?)(.+?)\2')

    def handleMatch(self, m):
        #node = markdown.util.etree.Element('span class="math"')
        node = Element('span class="math"')
        # node.text = markdown.util.AtomicString(m.group(2) + m.group(3) + m.group(2))
        if m.group(2) == "$$":
            node.text = markdown.util.AtomicString("\[" + m.group(3) + "\]")
        else:
            node.text = markdown.util.AtomicString("\(" + m.group(3) + "\)")
        return node


class MathExtension(markdown.Extension):
#    def extendMarkdown(self, md, md_globals):
#        md.inlinePatterns.add('math', MathPattern(), '<escape')
    def extendMarkdown(self, md):
		# An extension need to tell Markdown about them and ensure that they are run in the proper sequence.
		# We should give "math" a higher priority (185) than 'escape' which has 180 and also begin/end pattern should have lower priority than all others.
		# Links to more info: https://python-markdown.github.io/extensions/api/ and https://github.com/mitya57/python-markdown-math/blob/master/mdx_math.py
        md.inlinePatterns.register(MathPattern(), 'math', 185)
        
