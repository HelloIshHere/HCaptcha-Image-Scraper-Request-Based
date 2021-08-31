import requests

class ImageScraper():

    def __init__(self, host, sitekey, proxy):
        self.host = host
        self.sitekey = sitekey
        self.proxy = proxy
        self.s =  requests.Session()
        self.c_value = None
        self.v_value = "b1129b9"
        self.hl = "en"

    def c_value_getter(self):

        c_value_params = {

            "host" : self.host,
            "sitekey" : self.sitekey,
            "sc": "1",
            "swa" : "1",
        }

        c_value_headers = {
            'Host' : 'hcaptcha.com',
            'Connection' : 'keep-alive',
            'Cache-Control' : 'no-cache',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'Content-Type' : 'application/json; charset=utf-8',
            'Accept' : '*/*',
            'Sec-GPC' : '1',
            'Origin' : 'https://newassets.hcaptcha.com',
            'Sec-Fetch-Site' : 'same-site',
            'Sec-Fetch-Mode' : 'cors',
            'Sec-Fetch-Dest' : 'empty',
            'Referer' : 'https://newassets.hcaptcha.com/',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'en-US,en;q=0.9',
        }

        c_value_request = self.s.get("https://hcaptcha.com/checksiteconfig", headers = c_value_headers, params = c_value_params)
        self.c_value = c_value_request.json()['c']
        print(self.c_value)


    def start(self):
        self.c_value_getter()

captcha = ImageScraper('raffle.bstn.com',
                        '03196e24-ce02-40fc-aa86-4d6130e1c97a',
                        'NaN').start()

