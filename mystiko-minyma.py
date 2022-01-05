import argparse

import insert
import randstring
import retrive

projectDescription = """2 layered encryption to hide away the secret text and decrypt the same with the secret key"""
parser = argparse.ArgumentParser(description=projectDescription, prog="Mytiko-Minyama", usage="%(prog)s [options]")

parser.add_argument("--input", "-i", help="Input file to work on")
parser.add_argument("--output", "-o", help="Name of output file if exists any", default="minyma.png")
parser.add_argument("--base", "-b", help="User defined key 2 layer encryption", default="GodOfMischief")
parser.add_argument("--message", "-m", help="Message need to put into image")
parser.add_argument("--key", "-k", dest="key", help="28 Char key generated during encryption", action="store")
parser.add_argument("--copy", "-c", dest="copy", action=argparse.BooleanOptionalAction, default=True, help="copy generated key to clipboard, if any")
parser.add_argument('--version', "-v", action='version', version='%(prog)s v0.0.0alpha')
parser.add_argument("--tell", "-t", dest="tell", help="Encrypt the message into input file", action="store_true")
parser.add_argument("--listen", "-l", dest="listen", help="Check for the file if there is message hidden", action="store_true")
args = parser.parse_args()


def helpParser():
    parser.parse_args(["-h"])


def tellMessge(arguments: argparse.Namespace):
    if not (arguments.input and arguments.message):
        print("Missing input file or message")
        helpParser()
    else:
        if not arguments.base:
            print("Base key not given, using default \"GodOfMischief\"")
        if not arguments.output:
            print("output file not given, using default \"minyma.png\"")
        key = randstring.randstring()
        i = insert.Inserter()
        i.insert(arguments.message, key, arguments.input, arguments.output, arguments.base)
        print("key = "+key)
        print("told successfully")


def listenMessage(arguments: argparse.Namespace):
    if not (arguments.input and arguments.key):
        print("Missing input file or key")
        helpParser()
    else:
        r = retrive.Retrive()
        message = r.retriver(arguments.key, arguments.input, arguments.base)
        print("secrect is "+message)


def validate(arguments: argparse.Namespace):
    if (arguments.tell and arguments.listen) or ((not arguments.tell) and (not arguments.listen)):
        print("Have to tell or listen, no in between")
        helpParser()
    else:
        if arguments.tell:
            tellMessge(arguments)
        else:
            listenMessage(arguments)


validate(args)
