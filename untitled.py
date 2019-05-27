# coding: utf-8
"""Train tickets query via command-line.
   火车票通过命令行查询。
Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets beijing shanghai 2016-08-25
"""
from docopt import docopt

def cli():
    """command-line interface 命令行接口"""
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    cli()