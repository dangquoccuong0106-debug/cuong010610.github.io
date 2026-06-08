import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

if __name__ == "__main__":
    from bcsfe.cli.main import Main
    try:
        Main().main()
    except KeyboardInterrupt:
        Main.leave()
