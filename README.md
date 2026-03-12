# AI_Project
all about ai 

## 使用 uv 管理
- 创建/更新虚拟环境并安装依赖：
```
uv sync
```
- 运行脚本（示例）：
```
uv run python ai/claude_demo.py
```
- 添加依赖：
```
uv add <package>
```
- 升级并刷新锁文件：
``` 
uv lock --upgrade
```
- 固定 Python 版本（可选）：
``` 
uv python pin 3.11
```
- 在需要时激活虚拟环境：
```
source .venv/bin/activate
```
