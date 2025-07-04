<p align="center">
  <img src="images/projectcover.png" alt="Project Cover"/>
</p>

> [English version available in README-EN.md](./README-EN.md)

# MCP 天气预警服务

本项目基于 FastMCP，提供中国/全球各城市天气/灾害预警信息查询工具，支持通过城市名查询 LocationID 及获取实时气象灾害预警。

## 工具简介
- 查询城市 LocationID
- 获取指定城市的气象灾害预警信息

## 工具说明
本项目共包含两个工具，二者有依赖关系：
1. `lookup_city_tool(city: str)`：根据城市中文名查询唯一 LocationID。
2. `get_warning_tool(city: str = "")`：根据 LocationID 查询指定城市的气象灾害预警。

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
直接编辑 `config.py`，填写你的和风天气 API 信息，地址：https://dev.qweather.com/
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
- fastmcp

## 在 Cursor 客户端配置 mcp.json

在 Cursor 客户端中本地调用本项目的 MCP 工具服务，可以在 `.cursor/mcp.json` 文件中添加如下配置：

```json
{
  "weather-tools": {
    "command": "/你的路径/bin/python3",
    "args": [
      "/你的/项目/路径/server.py"
    ],
    "env": {}
  }
}
```

- `command`：填写你虚拟环境下的 python 路径（推荐用绝对路径，防止多环境冲突）
- `args`：第一个参数为 server.py 的绝对路径
- `env`：如需传递特殊环境变量可在此设置，通常留空即可

> 建议在 shell 里先激活虚拟环境并加载 .env，再启动 Cursor，这样环境变量会自动传递给 MCP 工具。
