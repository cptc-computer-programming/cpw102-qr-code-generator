def get_input(prompt: str) -> str:
    """Repeat the prompt until nonblank input is entered. Return the stripped text."""
    raise NotImplementedError


def png_filename(filename: str) -> str:
    """Keep a .png suffix in any letter case, or append .png."""
    raise NotImplementedError


def save_qr(content: str, filename: str) -> None:
    """Save a PNG encoding the exact content at the supplied filename."""
    raise NotImplementedError


def main() -> None:
    """Ask for content and filename, save the QR code, and report the filename."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
