import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        resp = requests.get(url)
        if resp.status_code != 200:
            return {} if return_json else ''  # 特例情况
        return resp.json() if return_json else resp.text  # 正常情况


