import argparse

projectDescription = """2 layered encryption to hide away the secret text and decrypt the same with the secret key"""
parser = argparse.ArgumentParser(description=projectDescription, prog="Mytiko-Minyama", usage="%(prog)s [options]")

parser.add_argument("--input", "-i", help="Input file to work on")
parser.add_argument("--output", "-o", help="Name of output file if exists any", default="minyma.png")
parser.add_argument("--base", "-b", help="User defined key 2 layer encryption", default="GodOfMischief")
parser.add_argument("--message", "-m", help="Message need to put into image")
parser.add_argument("--key", "-k", dest="key", help="28 Char key generated during encryption", action="store")
parser.add_argument("--copy", "-c", dest="copy", action=argparse.BooleanOptionalAction, default=True, help="copy generated key to clipboard, if any")
parser.add_argument('--version', "-v", action='version', version='%(prog)s v0.0.0alpha')
args = parser.parse_args()

