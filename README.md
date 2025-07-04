# MCP 天气预警服务

本项目基于 FastMCP，提供中国城市天气/灾害预警信息查询工具，支持通过城市名查询 LocationID 及获取实时气象灾害预警。

## 工具简介
- 查询城市 LocationID
- 获取指定城市或默认龙岗区的气象灾害预警信息

## 工具说明
本项目共包含两个工具，二者有依赖关系：
1. `lookup_city_tool(city: str)`：根据城市中文名查询唯一 LocationID。
2. `get_warning_tool(city: str = "")`：根据 LocationID 查询指定城市或默认龙岗区的气象灾害预警。

**建议先使用 `lookup_city_tool` 获取城市的 LocationID，再将该 ID 作为参数传递给 `get_warning_tool` 查询天气预警。**

## 快速开始

### 1. 克隆项目
```bash
git clone git@github.com:Jayden-hong/MCP_weatherwarning_Server.git
cd MCP_weatherwarning_Server
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置
直接编辑 `config.py`，填写你的和风天气 API 信息，地址：https://dev.qweather.com/：
```python
API_HOST = "你的host地址，可以在控制台-设置中查看你的API Host"
API_KEY = "你的API密钥"
DEFAULT_ID = "101280606"  # 如果有定向查询区域可以设置，我这里默认写了龙岗区的locationid，若更换地区，server的mcp工具描述那里也需要同步修改。
```

### 4. 启动服务
```bash
python3 server.py
```
或使用 procfile：
```bash
# procfile
worker: python3 server.py
```

## 接口说明
- `lookup_city_tool(city: str)`：查询城市 LocationID
- `get_warning_tool(city: str = "")`：获取指定城市的气象灾害预警

## 依赖
- requests
- fastmcp（需提前安装，或根据实际情况添加到 requirements.txt）

## 许可证
MIT 