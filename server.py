# server_mcp.py
import json, gzip, requests
from io import BytesIO
from fastmcp import FastMCP
from config import API_HOST, API_KEY, DEFAULT_ID

def decompress(resp):
    try:
        return json.loads(gzip.GzipFile(fileobj=BytesIO(resp.content)).read().decode())
    except:
        return resp.json()

mcp = FastMCP("weather-tools")

def _lookup_city(city: str) -> dict:
    """查询城市 LocationID 的底层实现"""
    params = {"location": city, "range": "cn", "key": API_KEY}
    resp = requests.get(f"{API_HOST}/geo/v2/city/lookup", params=params)
    data = decompress(resp)
    if data.get("code") == "200" and data.get("location"):
        return {"locationId": data["location"][0]["id"]}
    return {"error": f"未找到城市：{city}"}

@mcp.tool
def lookup_city_tool(city: str) -> dict:
    """
    查询城市 LocationID。

    参数：
        city (str): 需要查询的城市中文名，如"上海"。
    返回：
        dict: 查询成功时返回 {"locationId": "城市ID"}，失败时返回 {"error": "错误信息"}
    用途：
        通过城市名称获取用于天气查询的唯一 LocationID。
    """
    return _lookup_city(city)

@mcp.tool
def get_warning_tool(city: str = "") -> dict:
    """
    获取指定城市的天气/灾害预警信息，若用户直接询问天气且未说明具体城市，默认直接查询龙岗区DEFAULT_ID

    参数：
        city (str): 用LocationID查询，若未说明具体城市，直接查询龙岗区DEFAULT_ID。
    返回：
        dict: 
            - 有预警时返回 {"warnings": [预警信息列表]}
            - 无预警时返回 {"message": "无预警"}
            - 查询失败时返回 {"error": "错误信息"}
    用途：
        查询指定城市的气象灾害预警信息。
        - 若用户直接询问天气且未说明具体城市，如”今日有无天气预警“，默认直接查询龙岗区（DEFAULT_ID）无需问用户。
        - 除龙岗外，建议先用lookup_city_tool获取LocationID再查询。
    """
    if city and ("龙岗" in city):
        loc_id = DEFAULT_ID  # 龙岗区
    elif city and ("深圳" in city):
        res = _lookup_city(city)
        if "locationId" not in res:
            return res
        loc_id = res["locationId"]  # 查深圳全市
    elif city:
        res = _lookup_city(city)
        if "locationId" not in res:
            return res
        loc_id = res["locationId"]
    else:
        loc_id = DEFAULT_ID

    resp = requests.get(
        f"{API_HOST}/v7/warning/now",
        params={"location": loc_id, "lang": "zh", "key": API_KEY}
    )
    data = decompress(resp)
    if data.get("code") != "200":
        return {"error": f"API返回错误: {data.get('code')}"}
    ws = data.get("warning", [])
    if not ws:
        return {"message": f"已为你查询{city or '龙岗区'}，当前无预警信息"}
    return {"warnings": [
        {
            "title": w["title"],
            "typeName": w["typeName"],
            "severity": w["severity"],
            "text": w["text"],
            "pubTime": w["pubTime"],
            "startTime": w.get("startTime"),
            "endTime": w.get("endTime"),
        } for w in ws
    ]}

if __name__ == "__main__":
    mcp.run()
