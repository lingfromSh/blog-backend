import os


# loading settings
class Config:
    SECRET_KEY = os.urandom(32)
    BASE_DIR = os.path.abspath(os.environ["PWD"])
    MAIL_SERVER = "imap.163.com"
    MAIL_PROT = 993
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
