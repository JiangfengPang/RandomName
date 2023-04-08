import random
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self, pygame):
        super().__init__()
        # 动态加载ui 文件
        self.ui = uic.loadUi("ui/main.ui")
        self.ui.show()
        # 加载音乐
        # 初始化pygame
        self.pygame.mixer.init()
        self.sound = pygame.mixer.Sound("music/bcg.wav")

        # 打开本地名单
        self.ui.actiondaoru.triggered.connect(self.file_open)
        self.toolbar = self.addToolBar('！！！')
        # self.toolbar.addAction(openFile)

        # 拟用名单
        self.name_list = []
        # 实例化一个计时器
        self.timer = QTimer()
        # 添加计数器和最大次数
        self.count = 0
        # 点击按钮链接到 start
        self.ui.pushButton.clicked.connect(self.start)

        self.r = random.randint(1, 10)

    def play_sound(self):
        self.sound.play()

    def file_open(self):
        """
        打开学生名单
        “,“逗号用于分隔同时被赋值的两个变量。下划线’_'用作占位符，表示你不需要在代码中使用第二个值。
        在这种情况下，它被用来忽略由函数QFileDialog.getOpenFileName()返回的第二个值。
        """
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt, *.csv);;All Files (*)")
        if fileName:
            with open(fileName, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.rstrip('\n')
                    self.name_list.append(line)
        print(self.name_list)

    def random_color(self):
        """生成随机颜色"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # 为了保证颜色可见性，可以将三个颜色通道的值加起来，判断它们是否大于某个阈值
        if 0 <= r + g + b <= 400:
            return '#{:02X}{:02X}{:02X}'.format(r, g, b)
        else:
            return self.random_color()

    def start(self):
        # 开始点名
        if self.ui.pushButton.text() == '开始点名':
            self.ui.pushButton.setText('幸运儿挑选中...')
            self.count = 0
            self.timer = self.startTimer(100)  # 每1ms刷新显示一次随机的名字

        # 停止点名
        elif self.ui.pushButton.text() == '幸运儿挑选中...':
            self.ui.pushButton.setText('开始点名')
            self.killTimer(self.timer)
            name = random.choice(self.name_list)
            self.ui.lineEdit.setText(name)

    def timerEvent(self, event):
        """定时器事件：随机一个名字，并在屏幕上显示"""
        if self.count < 15:
            self.count += 1
            # 播放音效
            self.play_sound()
            name = random.choice(self.name_list)
            self.ui.lineEdit.setText(name)

            # 居中显示文本
            self.ui.lineEdit.setAlignment(QtCore.Qt.AlignCenter)

            # 获取当前调色板的对象
            palette = self.ui.lineEdit.palette()
            palette.setColor(QPalette.Text, QColor(self.random_color()))
            # 将更改后的调色板设置为QLineEdit对象的调色板
            self.ui.lineEdit.setPalette(palette)
        else:
            self.ui.pushButton.setText('开始点名')
            self.killTimer(self.timer)
            name = random.choice(self.name_list)
            self.ui.lineEdit.setText(name)


app = QApplication(sys.argv)
# 初始化主窗口对象
window = MainWindow()
sys.exit(app.exec_())
