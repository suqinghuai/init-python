import os
import subprocess
import sys


def get_project_root():
    """获取项目根目录，兼容打包后的exe文件"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的exe文件
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        # 如果是源码运行
        return os.path.dirname(os.path.abspath(__file__))


# 项目根目录
PROJECT_ROOT = get_project_root()
# 虚拟环境名称
VENV_NAME = "venv"
# 阿里云镜像源
ALIYUN_MIRROR = "https://mirrors.aliyun.com/pypi/simple/"


def create_venv():
    """创建虚拟环境"""
    print("正在创建虚拟环境...")
    venv_path = os.path.join(PROJECT_ROOT, VENV_NAME)
    
    # 检查虚拟环境是否已存在
    if os.path.exists(venv_path):
        print(f"虚拟环境 {VENV_NAME} 已存在，跳过创建步骤")
        return
    
    # 使用uv创建虚拟环境
    try:
        subprocess.run(
            ["uv", "venv", VENV_NAME],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True
        )
        print("虚拟环境创建成功！")
    except subprocess.CalledProcessError as e:
        print(f"创建虚拟环境失败: {e.stderr}")
        sys.exit(1)


def set_aliyun_mirror():
    """在虚拟环境中永久设置阿里云镜像源"""
    print("正在设置阿里云镜像源...")
    
    # 虚拟环境中pip配置文件路径
    pip_ini_path = os.path.join(PROJECT_ROOT, VENV_NAME, "pip.ini")
    
    # 写入pip配置文件
    config_content = f"""[global]
index-url = {ALIYUN_MIRROR}
trusted-host = mirrors.aliyun.com
"""
    
    try:
        with open(pip_ini_path, "w", encoding="utf-8") as f:
            f.write(config_content)
        print("阿里云镜像源设置成功！")
    except Exception as e:
        print(f"设置镜像源失败: {e}")
        sys.exit(1)


def copy_gitignore():
    """复制.gitignore文件"""
    print("正在设置.gitignore文件...")
    gitignore_path = os.path.join(PROJECT_ROOT, ".gitignore")
    
    # 检查.gitignore文件是否已存在
    if os.path.exists(gitignore_path):
        print(".gitignore文件已存在，跳过复制步骤")
        return
    
    # 模板内容（与现有.gitignore文件内容一致）
    gitignore_content = """# Python 通用
__pycache__/
*.py[cod]
*$py.class
*.so

# 虚拟环境
venv/
env/
.venv/
.env/

# 日志
*.log
*.pdb
*.exe

# IDE
.idea/
.vscode/

# PyInstaller
build/
dist/
*.spec

# 配置文件
config.ini"""
    
    try:
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write(gitignore_content)
        print(".gitignore文件创建成功！")
    except Exception as e:
        print(f"创建.gitignore文件失败: {e}")
        sys.exit(1)


def create_requirements():
    """创建requirements.txt文件"""
    print("正在创建requirements.txt文件...")
    requirements_path = os.path.join(PROJECT_ROOT, "requirements.txt")
    
    # 检查requirements.txt文件是否已存在
    if os.path.exists(requirements_path):
        print("requirements.txt文件已存在，跳过创建步骤")
        return
    
    # 写入依赖项
    requirements_content = "pyinstaller\n"
    
    try:
        with open(requirements_path, "w", encoding="utf-8") as f:
            f.write(requirements_content)
        print("requirements.txt文件创建成功！")
    except Exception as e:
        print(f"创建requirements.txt文件失败: {e}")
        sys.exit(1)


def create_readme():
    """创建README.md文件"""
    print("正在创建README.md文件...")
    readme_path = os.path.join(PROJECT_ROOT, "README.md")
    
    # 检查README.md文件是否已存在
    if os.path.exists(readme_path):
        print("README.md文件已存在，跳过创建步骤")
        return
    
    # 写入README内容
    readme_content = """# 项目

## 项目介绍



## 快速开始

### 面向使用者



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
```

## 实现方法



## 版本日志



## 许可证



"""
    
    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("README.md文件创建成功！")
    except Exception as e:
        print(f"创建README.md文件失败: {e}")
        sys.exit(1)


def create_license():
    """创建LICENSE文件"""
    print("正在创建LICENSE文件...")
    license_path = os.path.join(PROJECT_ROOT, "LICENSE")
    
    # 检查LICENSE文件是否已存在
    if os.path.exists(license_path):
        print("LICENSE文件已存在，跳过创建步骤")
        return
    
    # 写入LICENSE内容
    license_content = """The Prosperity Public License 2.0.0
If you follow the rules below, you may do everything with this software that would otherwise infringe either the contributor's copyright in it, any patent claim the contributor can license that covers this software as of the contributor's latest contribution, or both.
You must limit use of this software in any manner primarily intended for or directed toward commercial advantage or private monetary compensation to a trial period of 32 consecutive calendar days. This limit does not apply to use in developing feedback, modifications, or extensions that you contribute back to those giving this license.
Ensure everyone who gets a copy of this software from you, in source code or any other form, gets the text of this license and the contributor, source code, and commercial license contact lines above.
Do not make any legal claim against anyone for infringing any patent claim they would infringe by using this software alone, accusing this software, with or without changes, alone or as part of a larger application.
You are excused for unknowingly breaking rule 1 if you stop doing anything requiring this license within 30 days of learning you broke the rule.
This software comes as is, without any warranty at all. As far as the law allows, the contributor will not be liable for any damages related to this software or this license, for any kind of legal claim.

本软件（及相关文档、资源）仅供个人学习、研究、非商业用途。

以下行为未经书面许可，一律禁止：
1.  任何企业、公司、机构、组织的内部使用、生产环境使用、业务运营使用
2.  用于盈利、收费服务、广告变现、付费 SaaS、付费 API
3.  销售、出租、授权、再分发本软件或其衍生版本以获取利益
4.  将本软件嵌入、集成到商业产品、商业网站、商业服务中
5.  任何形式的商业利用、二次商用、间接商用

个人非商业使用允许：
- 仅限个人学习、测试、研究、非盈利开源项目
- 必须保留此版权声明

免责声明：
本软件按"原样"提供，无任何明示或暗示担保。
作者不对使用本软件造成的任何损失承担责任。

商业授权请联系：[430615396@qq.com]"""
    
    try:
        with open(license_path, "w", encoding="utf-8") as f:
            f.write(license_content)
        print("LICENSE文件创建成功！")
    except Exception as e:
        print(f"创建LICENSE文件失败: {e}")
        sys.exit(1)


def install_pyinstaller():
    """安装pyinstaller库"""
    print("正在安装pyinstaller库...")
    
    # 虚拟环境中的Python解释器路径
    python_exe = os.path.join(PROJECT_ROOT, VENV_NAME, "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        print(f"未找到虚拟环境Python解释器: {python_exe}")
        sys.exit(1)

    # 确保pip可用（uv创建的环境可能不包含pip）
    try:
        subprocess.run(
            [python_exe, "-m", "ensurepip", "--upgrade"],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True
        )
        subprocess.run(
            [python_exe, "-m", "pip", "install", "--upgrade", "pip", "--index-url", ALIYUN_MIRROR, "--trusted-host", "mirrors.aliyun.com"],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"初始化pip失败: {e.stderr}")
        sys.exit(1)
    
    try:
        # 使用虚拟环境中的pip安装pyinstaller
        subprocess.run(
            [python_exe, "-m", "pip", "install", "pyinstaller", "--index-url", ALIYUN_MIRROR, "--trusted-host", "mirrors.aliyun.com"],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True
        )
        print("pyinstaller安装成功！")
    except subprocess.CalledProcessError as e:
        print(f"安装pyinstaller失败: {e.stderr}")
        sys.exit(1)


def press_any_key_to_exit():
    """按任意键退出程序"""
    print("\n按任意键退出...")
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass


def main():
    """主函数"""
    print("开始初始化Python项目...")
    print(f"项目根目录: {PROJECT_ROOT}")
    
    # 1. 创建虚拟环境
    create_venv()
    
    # 2. 设置阿里云镜像源
    set_aliyun_mirror()
    
    # 3. 复制.gitignore文件
    copy_gitignore()
    
    # 4. 创建requirements.txt文件
    create_requirements()
    
    # 5. 创建README.md文件
    create_readme()
    
    # 6. 创建LICENSE文件
    create_license()
    
    # 7. 安装pyinstaller
    install_pyinstaller()
    
    print("\n项目初始化完成！")
    press_any_key_to_exit()


if __name__ == "__main__":
    main()