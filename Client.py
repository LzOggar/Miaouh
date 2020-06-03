#!/usr/bin/env python
#-*-coding:utf-8-*-

import tkinter, threading, socket

class Client(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.width, self.height = str(self.winfo_screenwidth()//2), str(self.winfo_screenheight()//2)
        self.title("Miauh - client")
        self.geometry(self.width + "x" + self.height)
        self.resizable(width = False, height = False)

        self.panel_top = tkinter.Frame(self)
        self.panel_top.pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = tkinter.YES)

        self.chat_box = tkinter.Text(self.panel_top, state = tkinter.DISABLED, font = ("Helvetica", 12))
        self.chat_box.pack(fill = tkinter.BOTH, expand = tkinter.YES)

        self.scrollbar = tkinter.Scrollbar(self.chat_box)
        self.scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

        self.chat_box.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.chat_box.yview)

        self.panel_bottom = tkinter.Frame(self)
        self.panel_bottom.pack(side = tkinter.BOTTOM, fill = tkinter.BOTH)

        self.text_var = tkinter.StringVar()
        self.text_tmp = ''

        self.input_text = tkinter.Entry(self.panel_bottom, textvariable = self.text_var)
        self.input_text.pack(fill = tkinter.BOTH)

        self.todo = True
        self.flag = True
        self.host = '127.0.0.1'
        self.port = 15555

        try:
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_client.connect((self.host, self.port))

            self.threadReceive = threading.Thread(target = self.receive)
            self.threadSend = threading.Thread(target = self.send)
            self.threadReceive.start()
            self.threadSend.start()
        except:
            pass

        self.input_text.bind("<Return>", self.display_message)
        self.mainloop()

        try:
            self.socket_client.close()
            self.todo = False
        except:
            pass

    def display_message(self, event):
        if self.flag:
            message = self.text_var.get()
            if message != '':
                self.chat_box.config(state = tkinter.NORMAL)
                self.chat_box.insert(tkinter.END, 'You > ' + message + '\n')
                self.chat_box.config(state = tkinter.DISABLED)

                self.text_var.set('')
                self.text_tmp = message

    def send(self):
        while self.todo:
            if self.flag:
               if self.text_tmp != '':
                    text_to_send = 'Stranger > ' + self.text_tmp
                    self.socket_client.send(text_to_send.encode())
                    self.text_tmp = ''
                    self.flag = False


    def receive(self):
        while self.todo:
            message = self.socket_client.recv(1024)
            if message:
                text_received = message.decode() + '\n'
                self.chat_box.config(state = tkinter.NORMAL)
                self.chat_box.insert(tkinter.END, text_received)
                self.chat_box.config(state = tkinter.DISABLED)

                self.flag = True

Client()
