import markdown_it
from hypothesis import assume, example, given
from hypothesis import strategies as st

import unmarkd


def helper(text: str) -> None:
    md = markdown_it.MarkdownIt()
    value0 = md.render(text)
    unmarked = unmarkd.unmark(html=value0)
    value1 = md.render(unmarked)
    assert value0 == value1, (value0, value1, unmarked)


@given(text=st.text())
# @example(
#    """<ul>
# <li>tb
# <ol>
# <li>i1</li>
# <li>i2</li>
# <li>i3</li>
# </ol>
# </li>
# <li>bb</li>
# </ul>"""
# )
def test_roundtrip_commonmark_unmark(text):
    assume(text.strip() == text)
    helper(text)


# fmt: off
class TestExampleCases:
    # pylint: disable=C0116,R0201,C0321
    def test_example_1(self) -> None:  helper("")
    def test_example_2(self) -> None:  helper("` `")
    def test_example_3(self) -> None:  helper("0\n\n0")
    def test_example_4(self) -> None:  helper("```\n```")
    def test_example_5(self) -> None:  helper("0.")
    def test_example_6(self) -> None:  helper("```")
    def test_example_7(self) -> None:  helper(R"*\**")
    def test_example_8(self) -> None:  helper(R"**\***")
    def test_example_9(self) -> None:  helper(R"`\``")
    def test_example_10(self) -> None: helper(R"-")
    def test_example_11(self) -> None: helper(R">")
    def test_example_12(self) -> None: helper(R"<")
    def test_example_13(self) -> None: helper("*foo `bar* baz`")
    def test_example_14(self) -> None: helper(">>")
    def test_example_15(self) -> None: helper(R"~~\~~~")
    def test_example_16(self) -> None: helper("[link](https://github.com 'GitHub Homepage')")
    def test_example_17(self) -> None: helper("[link](https://github.com)")
    def test_example_18(self) -> None: helper("![img](https://github.com)")
    def test_example_19(self) -> None: helper("""# h1\n## h2\n### h3\n#### h4\n##### h5\n###### h6""")
    def test_example_20(self) -> None: helper("~~Nothing.~~")
# fmt: on
