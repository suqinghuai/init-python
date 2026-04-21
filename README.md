# init-python

Python项目自动初始化程序 - 一键搭建标准化Python开发环境

## 项目介绍

init-python 是一个自动化工具，用于快速初始化Python项目的开发环境。它能够自动完成虚拟环境创建、依赖管理、项目配置文件生成等一系列繁琐的初始化工作，让开发者能够专注于业务逻辑的开发。

## 功能特性

- **自动创建虚拟环境**: 使用 uv 工具快速创建 Python 虚拟环境
- **配置镜像源**: 自动配置阿里云 PyPI 镜像源，加速依赖包下载
- **生成配置文件**: 自动创建 .gitignore、requirements.txt、README.md、LICENSE 等标准项目文件
- **安装开发工具**: 自动安装 pyinstaller 打包工具
- **智能检测**: 自动检测文件是否已存在，避免覆盖已有配置
- **支持打包**: 可打包为 exe 独立运行，无需 Python 环境

## 快速开始

### 面向使用者

1. **下载程序**
   - 下载 `init.exe` 可执行文件
   - 或克隆项目获取源码

2. **运行初始化**
   ```bash
   # 方式一：直接运行 exe 文件
   init.exe
   
   # 方式二：运行 Python 源码
   python init.py
   ```

3. **等待完成**
   - 程序将自动完成所有初始化步骤
   - 按任意键退出程序

### 面向开发者

```bash
# 克隆项目
git clone <项目地址>

# 进入项目目录
cd <项目目录>

# 激活虚拟环境
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt

# 运行程序
python init.py

# 打包为 exe（可选）
pyinstaller --onefile init.py
```

## 实现方法

### 核心功能

1. **虚拟环境创建**
   - 使用 `uv venv` 命令创建虚拟环境
   - 自动检测虚拟环境是否已存在

2. **镜像源配置**
   - 在虚拟环境中创建 `pip.ini` 配置文件
   - 配置阿里云镜像源和信任主机

3. **文件生成**
   - `.gitignore`: 包含 Python 通用忽略规则
   - `requirements.txt`: 初始依赖包含 pyinstaller
   - `README.md`: 项目文档模板
   - `LICENSE`: Prosperity Public License 2.0.0

4. **依赖安装**
   - 使用虚拟环境中的 pip 安装 pyinstaller
   - 通过阿里云镜像源加速下载

### 技术架构

- **语言**: Python 3.x
- **依赖管理**: uv + pip
- **打包工具**: PyInstaller
- **配置文件**: pip.ini (Windows)

### 项目结构

```
init-python/
├── init.py              # 主程序入口
├── requirements.txt     # 依赖列表
├── .gitignore          # Git 忽略规则
├── LICENSE             # 许可证文件
├── README.md           # 项目文档
├── build/              # PyInstaller 构建目录
├── dist/               # 打包输出目录
│   ├── init.exe        # 可执行文件
│   └── venv/           # 示例虚拟环境
└── venv/               # 虚拟环境（运行后生成）
```

## 版本日志

### v1.0.0 (2026-04-19)
- 初始版本发布
- 支持虚拟环境自动创建
- 支持阿里云镜像源配置
- 支持标准项目文件生成
- 支持 pyinstaller 自动安装
- 支持 exe 打包运行

## 许可证

本软件采用 Prosperity Public License 2.0.0 许可证。

### 使用限制

**禁止行为**（未经书面许可）:
1. 任何企业、公司、机构、组织的内部使用、生产环境使用、业务运营使用
2. 用于盈利、收费服务、广告变现、付费 SaaS、付费 API
3. 销售、出租、授权、再分发本软件或其衍生版本以获取利益
4. 将本软件嵌入、集成到商业产品、商业网站、商业服务中
5. 任何形式的商业利用、二次商用、间接商用

**允许使用**:
- 个人学习、测试、研究、非盈利开源项目
- 必须保留此版权声明

### 商业授权

如需商业使用，请联系: [430615396@qq.com]

### 免责声明

本软件按"原样"提供，无任何明示或暗示担保。作者不对使用本软件造成的任何损失承担责任。