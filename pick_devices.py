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
        self.current_string = ""
        self.init_view()

    def keyEevent(self, event):
        print("event.char = [{}]".format(event.char))
        print("event.keycode = 0x%08x" %event.keycode)

        if len(event.char) > 1:
            print("bad key char, skip")
            return

        if event.char.isalpha() or event.char.isdigit():
            self.current_string += event.char
            return

        if event.char == '\r':
            print("current_string: {}".format(self.current_string))
            self.show_device(self.current_string)
        elif event.char == ' ':
            self.clear_screen()

        self.current_string = ""

    def show_device(self, asset_number):
        info = self.compare_device(asset_number)
        info = info+'\r\n'+"扫码时间：" + get_current_time()
        self.content_label.configure(text=info)

    def clear_screen(self):
        self.content_label.configure(text="")

    def init_view(self):
        self.window.geometry('800x400')
        self.title_label = tk.Label(window, text='设备信息', font=('Arial', 20), width=10, height=3)
        self.title_label.pack()
        self.content_label = tk.Label(window, text='请扫描设备资产编码！!', font=('Arial', 18), width=300, height=9)
        self.content_label.pack()
        self.window.bind("<Key>", self.keyEevent)

    def compare_device(self, asset_numb):
        device_info = '查不到!'
        for row in self.received_list:
            if asset_numb.upper().__eq__(row.get('asset_numb')):
                device_info = 'TOP：' + str(row.get('top')) + '\r\n' + \
                                   '所属云：' + row.get('cloud') + '\r\n' + \
                                   '资产编号：' + row.get('asset_numb') + '\r\n' + \
                                   '物品名称：' + row.get('goods_name')
                break
        return device_info


if __name__ == '__main__':
    # 实例化object，建立窗口window
    window = tk.Tk()
    window.title('WeTest 设备分拣仪')
    PickDevices(window)
    # 主窗口循环显示
    window.mainloop()
