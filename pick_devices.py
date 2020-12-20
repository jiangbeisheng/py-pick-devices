# -*- coding: utf-8 -*-
import threading
import tkinter as tk  # 使用Tkinter前需要先导入
from utils.util import get_received_excel, get_current_time


class PickDevices(object):

    def __init__(self, master=None):
        # 读取5次领用设备表
        self.received_list = get_received_excel('5st_all.xlsx')
        # 初始化显示窗体
        self.window = master
        self.init_view()
        t = threading.Thread(target=self.scanner)
        t.start()

    def init_view(self):
        self.window.geometry('800x400')
        self.title_label = tk.Label(window, text='设备信息', font=('Arial', 20), width=10, height=3)
        self.title_label.pack()
        self.content_label = tk.Label(window, text='请扫描设备资产编码！!', font=('Arial', 18), width=300, height=9)
        self.content_label.pack()

    def scanner(self):
        while True:
            asset_numb = input("请输入：")
            info = self.compare_device(asset_numb)
            info = info+'\r\n'+"扫码时间："+get_current_time()
            self.content_label.configure(text=info)
        pass

    def compare_device(self, asset_numb):
        device_info = '查不到!'
        for row in self.received_list:
            if asset_numb.__eq__(row.get('asset_numb')):
                device_info = 'TOP：' + str(row.get('top')) + '\r\n' + \
                                   '所属云：' + row.get('cloud') + '\r\n' + \
                                   '资产编号：' + row.get('asset_numb') + '\r\n' + \
                                   '物品名称：' + row.get('goods_name')
                break
        return device_info
        pass


if __name__ == '__main__':
    # 实例化object，建立窗口window
    window = tk.Tk()
    window.title('WeTest 设备分拣仪')
    PickDevices(window)
    # 主窗口循环显示
    window.mainloop()
