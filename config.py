#This file stores database settings & secret key.
# config.py
# ------------------------------------
# This file holds all configurations
# like Secret Key, Database connection
# details, Email settings, Razorpay keys etc.
# ------------------------------------




SECRET_KEY = "abc@12"   # used for sessions

# MySQL Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "lakshmi@12"  # keep empty if no password
DB_NAME = "smartcart"

# Email SMTP Settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'blakshmi1422@gmail.com'
MAIL_PASSWORD = 'gpvs uxka szth vhpt'   # Gmail App Password

RAZORPAY_KEY_ID = "rzp_test_RrsgFPhAz3hlwf"
RAZORPAY_KEY_SECRET = "zO0HqGcLJ5B6PjYTVg7Cpu7B"
