from davidkhala.http_request import Request


class API(Request):
    def __init__(self, ak):
        super().__init__()
        self.ak = ak

    def request(self, url, method: str, params: dict = None, data=None, json=None) -> dict:
        return super().request(url, method,
                               {"output": "json", "ak": self.ak} | params,
                               data, json,
                               )

    def geocoding(self, address):
        base_url = "http://api.map.baidu.com/geocoding/v3/"
        r = self.request(f"{base_url}", method="GET", params={"address": address})
        assert r["status"] == 0
        return r["result"]

    def get_location(self, address):
        r = self.geocoding(address)
        return r["location"]