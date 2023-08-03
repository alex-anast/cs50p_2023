"""
Implement a function called parse that expects a str of HTML as input,
extracts any YouTube URL that's the value of a src attribute of
an iframe element therein, and returns its shorter, shareable youtu.be
equivalent as a str. Expect that any such URL will be in one of
the formats below. Assume that the value of src will be surrounded
by double quotes. And assume that the input will contain no more than
one such URL. If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
"""


import re
import sys


def main():
    try:
        print(parse(input("HTML: ")))
    except:
        sys.exit()


def parse(html: str) -> str:
    if match := re.search(
        pattern=r'.+src="http(?:s)?://(?:www\.)?youtube.com/embed/(\w+)".+',
        string=html,
    ):
        return "https://youtu.be/" + match.group(1)
    return


if __name__ == "__main__":
    main()
