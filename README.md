# QR Code Generator

Build a Python program that turns a URL or short message into a QR code you can scan.

Follow the [GitHub setup instructions](GITHUB_SETUP.md) before starting.

## Learning Goals

- Install and use a third-party Python package.
- Write functions with specified inputs and return values.
- Use a loop to collect nonblank input.

## Program File

Complete the starter functions in `make_qr.py`.

## Library Setup

In your project folder, run `python -m pip install -r requirements.txt`. Import `qrcode` in your program. The Usage example shows how to make and save an image. [qrcode documentation](https://pypi.org/project/qrcode/#usage)

## Requirements

Automated tests import `make_qr` and call each function directly. Keep the filename, function names, parameter names and order, and return types exactly as provided. Keep the starter's main guard so importing the module starts no prompts and creates no files.

| Function | Required behavior |
|---|---|
| `get_input(prompt: str) -> str` | Use the supplied prompt each time. Repeat for empty or whitespace-only input. Return the first nonblank response with surrounding whitespace removed. Preserve internal spaces. |
| `png_filename(filename: str) -> str` | If the filename ends in `.png` in any letter case, return it unchanged. Otherwise append `.png`. Use only the supplied string. |
| `save_qr(content: str, filename: str) -> None` | Use `qrcode` to encode the content exactly as supplied. Save a PNG at the given filename, which already includes the extension and may include a folder. Return `None`. |
| `main() -> None` | Call `get_input` twice, first for content and then for the filename. Use `png_filename` and `save_qr`. After saving, print `Saved ` followed by the final filename. Return `None`. |

## Input Assumptions

The content fits in a QR code. The filename is valid and its folder exists. Encode URL characters such as `?`, `&`, and `=` exactly as entered.

## Sample Output

```text
URL or text: https://example.com/?course=python&week=4
Output filename: course
Saved course.png
```

## Check Your Work

- Run `python make_qr.py` with the sample inputs. Scan the image and check that both query parameters are present.
- Try `Meet in lab 204` with the filename `lab.PNG`. Check the exact filename and scan the message.
- Press Enter at either prompt. Confirm that the program asks again.

## Submission

Commit and push to `development`. Review and merge your pull request into `main`, then submit your repository URL in Canvas.
