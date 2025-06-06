# your code goes here!

import re


class EmailAddressParser:
    regex = re.compile(r"[A-Za-z][A-Za-z0-9]*(\.[A-Za-z0-9]+)*@[A-Za-z0-9]+\.[a-z]{2,}")

    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        strings = re.split(r",|\s", self.email_addresses)

        parsed_emails = set()
        for string in strings:
            if self.regex.fullmatch(string):
                parsed_emails.add(string)
        return sorted(list(parsed_emails))


email_addresses = "john@doe.com, person@somewhere.org"
parser = EmailAddressParser(email_addresses)

print(parser.parse())
