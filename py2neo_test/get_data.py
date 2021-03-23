
import pandas as pd



class Datas():
    def __init__(self):
        self.path = 'Invoice_data_Demo.xls'
        self.datas = pd.read_excel(self.path,header=0,encoding = 'utf-8')

    def pd_data(self):
        buy_key = [str(data) for data in self.datas['购买方名称']]
        sell_key = [str(data) for data in self.datas['销售方名称']]
        money_key = [str(data) for data in self.datas['金额']]

        return {'sell_key':sell_key,'buy_key':buy_key,'money_key':money_key}




if __name__ == '__main__':
    datas = Datas()
    all_datas = datas.pd_data()
    print(all_datas)