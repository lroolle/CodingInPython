class MakeHtmlTagClass(object):
    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">\n" \
                   + fn(*args, **kwargs) + "\n</" + self._tag + ">"

        return wrapped


@MakeHtmlTagClass(tag="b", css_class="bold_css")
@MakeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello Be Html: {}".format(name)


print(hello(" HAH "))

# >>> <b class='bold_css'>
#     <i class='italic_css'>
#     Hello Be Html:  HAH 
#     </i>
#     </b>
