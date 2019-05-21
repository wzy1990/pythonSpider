import requests

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        print(url)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        headers = {'User_Agent': user_agent}
        sessions = requests.session()
        sessions.headers = headers
        response = sessions.get(url, allow_redirects=True)

        if response.status_code != 200:
            return None

        return response.text