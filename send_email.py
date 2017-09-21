import yagmail
import sys, getopt
import json
def send_email(sender, receiver, headline, message):
    yag = yagmail.SMTP(sender)
    yag.send(receiver, headline, message)


def main(argv):
    try:
        data=json.loads(argv[3])
    except:
        data = argv[3]
    send_email(argv[0], argv[1], argv[2], data)


if __name__ == "__main__":
    main(sys.argv[1:])
