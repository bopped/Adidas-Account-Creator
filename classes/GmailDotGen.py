#Credit doprdele

class GmailDotEmailGenerator:
  def __init__(self, email):
    self.__username__, self.__domain__ = email.split('@')
  def generate(self):
    return self.__generate__(self.__username__, self.__domain__)
  def __generate__(self, username, domain):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@" + domain)
    return emails
