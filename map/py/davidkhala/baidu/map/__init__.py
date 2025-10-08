from davidkhala.http_request import Request


class API(Request):
    def __init__(self, ak):
        super().__init__()
        self.ak = ak

    def request(self, url, method: str, params: dict = None, data=None, json=None) -> dict:
        r = super().request(url, method,
                            {"output": "json", "ak": self.ak} | params,
                            data, json,
                            )
        if r["status"] != 0:
            raise Exception(r["message"])
        return r

    def geocoding(self, address: str):
        base_url = "http://api.map.baidu.com/geocoding/v3/"
        r = self.request(f"{base_url}", method="GET", params={"address": address})
        return r["result"]

    def place(self, address: str, *, region='中国', page_num=0, **kwargs):
        """
        https://lbs.baidu.com/faq/api?title=webapi/guide/webservice-placeapiV3/interfaceDocumentV3#%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92%E5%8C%BA%E5%9F%9F%E6%A3%80%E7%B4%A2
        """
        base_url = "https://api.map.baidu.com/place/v3/region"
        r = self.request(f"{base_url}", method="GET", params={
            "query": address,
            "region": region,
            "page_size": 20,
            'page_num': page_num,
            **kwargs,
        })

        return r['results'], r['total']

    def suggest(self, address: str, *, region='中国'):
        """
        https://lbs.baidu.com/faq/api?title=webapi/guide/webservice-placeapiV3/interfaceDocumentV3#%E5%9C%B0%E7%82%B9%E8%BE%93%E5%85%A5%E6%8F%90%E7%A4%BA
        可作为轻量级地点检索服务单独使用
        return up to 10 results
        """
        base_url = "https://api.map.baidu.com/place/v3/suggestion"
        r = self.request(f"{base_url}", method="GET", params={
            "query": address,
            "region": region,
        })
        return r['results']
