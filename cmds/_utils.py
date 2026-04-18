import sys
from datetime import datetime
from colorama import init, Fore, Style
from pathlib import Path
import os
import shutil

init(autoreset=True)


class Logger:
    def info(self, msg):
        print(f"{Fore.CYAN}[INFO]\t\t{Style.RESET_ALL} {msg}")

    def success(self, msg):
        print(f"{Fore.GREEN}[SUCCESS]\t{Style.RESET_ALL} {msg}")

    def warning(self, msg):
        print(f"{Fore.YELLOW}[WARNING]\t{Style.RESET_ALL} {msg}")

    def error(self, msg):
        print(f"{Fore.RED}[ERROR]\t\t{Style.RESET_ALL} {msg}", file=sys.stderr)

    def debug(self, msg):
        print(f"{Fore.MAGENTA}[DEBUG]\t\t{Style.RESET_ALL} {msg}")

    def critical(self, msg):
        """不可恢复的错误，直接退出"""
        print(
            f"{Fore.RED}====== [CRITICAL] {msg} ====== {Style.RESET_ALL}",
            file=sys.stderr,
        )
        exit(1)


class Config:
    VIX_HOME = Path(os.getenv("VIX_HOME", "./.vix"))
    VIX_LIBS_PATH = VIX_HOME / "libs"


class VIndexTool:
    def __init__(self, dir_path: Path):
        self.path = dir_path / "vindex.toml"

    def content(self, package_name=None) -> dict[str, object]:
        import tomllib

        if not (self.path).exists():
            log.error(f"包 {package_name} 不存在 vindex.toml 文件!")
            yn = input("是否删除? (y/n)")
            if yn == "y":
                shutil.rmtree(self.path.parent)
                log.warning(f"已删除包 {package_name}")
                exit(0)
            else:
                log.critical(
                    "已保留此包，但它不可用（缺少vindex.toml文件，vpm无法识别它）"
                )

        with open(self.path, "rb") as f:
            return tomllib.load(f)


log = Logger()
