def get_input(prompt):
    """Repeat the supplied prompt until input is not empty or whitespace-only.

    Return a string with surrounding whitespace removed, preserving spaces
    and punctuation within the response.
    """
    pass


def png_filename(filename):
    """Return the filename as a string, appending .png only if needed.

    Keep an existing .png extension in any letter case: lab becomes lab.png,
    but lab.PNG stays lab.PNG. Do not prompt for input.
    """
    pass


def save_qr(content, filename):
    """Use qrcode to encode the exact content and save a PNG at filename.

    The filename includes its extension and may include an existing folder.
    Do not prompt or print. Return nothing (None).
    """
    pass


def main() -> None:
    """Use get_input to ask for a URL or message, then an output filename.

    Use png_filename to finalize the filename and save_qr to save the image.
    After saving, print "Saved " followed by the final filename.
    Return nothing (None).
    """
    pass


if __name__ == "__main__":
    main()
