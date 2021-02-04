from selenium import webdriver
import random




ip = "%s.%s.%s.%s" % (
    random.randrange(1, 200, 20), random.randrange(1, 200, 20), random.randrange(1, 200, 20),
    random.randrange(1, 200, 20))

options = webdriver.ChromeOptions()
options.add_argument(f'X-Forwarded-For="{ip}"')
browser = webdriver.Chrome(options=options)
