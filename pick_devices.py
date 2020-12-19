# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入

from utils.util import get_received_excel


class PickDevices(object):
    def __init__(self, master=None):
        # 读取5次领用设备表
        self.received_list = get_received_excel('5st_all.xlsx')
        # 初始化显示窗体
        self.window = master
        self.window.geometry('800x400')
        self.title_label = tk.Label(window, text='设备信息', font=('Arial', 20), width=10, height=3)
        self.title_label.pack()
        self.asset_numb = 'init'
        self.compare_device()

    def compare_device(self):
        # 伪代码：通过扫码枪获取资产编号
        # self.asset_numb = get_asset_numb()
        if self.asset_numb is 'init':
            self.content_label = tk.Label(window, text='请扫描设备资产编码！!', font=('Arial', 18), width=100, height=7)
            self.content_label.pack()
        else:
            for row in self.received_list:
                if self.asset_numb.__eq__(row.get('asset_numb')):
                    self.device_info = 'TOP：' + str(row.get('top')) + '\r\n' + \
                                       '所属云：' + row.get('cloud') + '\r\n' + \
                                       '资产编号：' + row.get('asset_numb') + '\r\n' + \
                                       '物品名称：' + row.get('goods_name')

                    self.content_label.configure(text=self.device_info)
        # 测试模拟扫码使用，正式请删除
        self.asset_numb = 'TKMB2010057X'
        # 隔一秒执行一次该方法
        self.window.after(1000, self.compare_device)
        pass


if __name__ == '__main__':
    # 实例化object，建立窗口window
    window = tk.Tk()
    window.title('WeTest 设备分拣仪')
    PickDevices(window)
    # 主窗口循环显示
    window.mainloop()
