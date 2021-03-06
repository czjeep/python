import requests

requests.packages.urllib3.disable_warnings()

class GetData(object):

    def __init__(self, date, from_station, to_station):
        self.date = date
        self.from_station = from_station
        self.to_station = to_station

    def request_12306(self):
        """requests跟12306拿数据"""
        # 构建URL
        url = 'https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            self.date, self.from_station, self.to_station
        )
        # 添加verify=False参数不验证证书
        r = requests.get(url, verify=False)
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            self.date, self.from_station, self.to_station
        )
        r = requests.get(url, verify=False)
        return r.json()