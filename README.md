# AI_Project
all about ai 

## 环境变量初始化
```shell
source .env
```

## 使用 uv 管理
- 创建/更新虚拟环境并安装依赖：
```shell
## uv sync 是 uv 进行项目环境管理的核心命令，它将 pip install、pip install -r requirements.txt、pip install -e . 等步骤合并为一个原子操作，并基于锁文件保证了环境的确定性 
# 它的主要作用是将项目的虚拟环境与项目的
# 依赖声明（pyproject.toml）和锁文件（uv.lock）进行同步 
uv sync

# 方法一：激活环境
# 在项目根目录下
source .venv/bin/activate  

# 升级项目所有依赖到最新兼容版本并更新锁文件的命令。
uv lock --upgrade

# 运行脚本
uv run python ai/claude_demo.py

```

## 添加依赖包 推荐方式
```shell
# 添加普通依赖（运行环境所需） ： 1. 将依赖写入 pyproject.toml 的相应部分。2. 解析依赖树，更新 uv.lock 锁文件。 3.自动将新包安装到当前虚拟环境中
uv add requests

# 添加开发依赖（如 pytest、ruff）
uv add --dev pytest

# 添加可选依赖组（extras）
uv add 'langchain[chromadb]'   # 方式一：直接指定 extras
uv add --extra chromadb langchain  # 方式二：将 langchain 的 chromadb extra 添加到主依赖
```




```shell
- 运行脚本（示例）：
uv run python ai/claude_demo.py
 
## 固定 Python 版本（可选）：
uv python pin 3.11

# 在需要时激活虚拟环境：
source .venv/bin/activate
```


```shell
git rm -r --cached .idea
```
