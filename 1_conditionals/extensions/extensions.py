"""
In a file called extensions.py, implement a program that prompts the user
for the name of a file and then outputs that file's media type
if the file's name ends, case-insensitively, in any of these suffixes:
.gif .jpg .jpeg .png .pdf .txt .zip
If the file’s name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.
"""


def main():
    file_name = input("Give name of the file: ").lower().strip()
    file_type = check_type(file_name)
    print(file_type)


def check_type(fn: str) -> str:
    ending = fn.split(".")[-1]
    match ending:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


if __name__ == "__main__":
    main()
