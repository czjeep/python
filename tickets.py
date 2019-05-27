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
from stations import stations
from get_data import GetData
import formats

def cli():
    arguments = docopt(__doc__)
    from_station =stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    data = GetData(date, from_station, to_station)
    result = data.request_12306()
    if result['httpstatus'] == 200 and result.get('data') is not None and result.get('data') != '':
        format_result = formats.Formats(result.get('data'), options)
        return format_result.format_data()
    else:
        return result['messages']

if __name__ == '__main__':
    cli()