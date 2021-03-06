"""返回规范个格式的 table"""

from prettytable import PrettyTable
from colorama import init, Fore

class Formats(object):
    def __init__(self, datas, options):
        self.datas = datas
        self.options = options

    def format_data(self):
        """返回规范的 table"""
        ptable = PrettyTable()
        header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()
        ptable._set_field_names(header)
        for train in self.datas:
            ptable.add_row(['1','2','3','4','5','6','7','8','9','10'])
            # trains = train.get('queryLeftNewDTO')
            # if trains is not None and trains != '':
            #     initial = trains['station_train_code'].lower()[0]
            #     if not self.options or initial in self.options:
            #         ptable.add_row([trains['station_train_code'], Fore.GREEN 
            #             + "%s -> %s" % (trains['from_station_name'], 
            #             trains['to_station_name']) + Fore.RESET, 
            #             Fore.RED + "%s -> %s" % (trains['start_time'], trains['arrive_time']) 
            #             + Fore.RESET, trains['lishi'], trains['zy_num'], trains['ze_num'], 
            #             trains['rw_num'], trains['yw_num'], trains['yz_num'], trains['wz_num']])
        print(ptable)
        return ptable