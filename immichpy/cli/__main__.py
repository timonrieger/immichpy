try:  # pragma: no cover
    from .main import app
except ImportError:  # pragma: no cover
    import sys

    message = 'To use the immichpy command, install the "cli" extra. See https://immichpy.timonrieger.de/cli/getting-started/ for more information.'
    print(message, file=sys.stderr)
    sys.exit(1)


def main() -> None:  # pragma: no cover
    app()
