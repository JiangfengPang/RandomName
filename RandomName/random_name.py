# import MainWindow
# import random
#
# class RandomName(MainWindow):
#     def __init__(self):
#
#     def start(self):
#         # 开始点名
#         if self.ui.pushButton.text() == '开始点名':
#             self.ui.pushButton.setText('幸运儿挑选中...')
#             self.count = 0
#             self.timer = self.startTimer(100)  # 每1ms刷新显示一次随机的名字
#         # 停止点名
#         elif self.ui.pushButton.text() == '幸运儿挑选中...':
#             self.ui.pushButton.setText('开始点名')
#             self.killTimer(self.timer)
#             name = random.choice(self.name_list)
#             self.ui.lineEdit.setText(name)
#
#     def timerEvent(self, event):
#         # 定时器事件：随机一个名字，并在屏幕上显示
#         if self.count < 15:
#             self.count += 1
#             name = random.choice(self.name_list)
#             self.ui.lineEdit.setText(name)
#             # 居中显示文本
#             self.ui.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
#             # 获取当前调色板的对象
#             palette = self.ui.lineEdit.palette()
#             palette.setColor(QPalette.Text, QColor(self.random_color()))
#             # 将更改后的调色板设置为QLineEdit对象的调色板
#             self.ui.lineEdit.setPalette(palette)
#         else:
#             self.ui.pushButton.setText('开始点名')
#             self.killTimer(self.timer)
#             name = random.choice(self.name_list)
#             self.ui.lineEdit.setText(name)