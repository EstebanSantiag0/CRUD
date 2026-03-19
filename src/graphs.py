import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QToolTip
from PyQt6.QtCore import QPoint
from abc import abstractmethod
from random import randint
import os
import mplcursors

directorio = os.path.dirname(os.path.abspath(__file__))
for i in ["xkcd-script.ttf", "xkcd.otf", "ComicNeue-Regular.ttf", "6680-fontps.ttf"]:
    font_dir = os.path.join(directorio, "assets", "fonts", i)
    fm.fontManager.addfont(font_dir)

colors = [
    # Pasteles
    "#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#FF99CC",
    "#99CCFF", "#FFD700", "#00F7FF", "#DDA0DD", "#F0E68C",
    # Vibrantes
    "#FF4500", "#1E90FF", "#32CD32", "#FF1493", "#FF8C00",
    "#00CED1", "#9400D3", "#FF6347", "#00FA9A", "#4169E1",
    # Intermedios
    "#FF69B4", "#40E0D0", "#FFA500", "#7B68EE", "#3CB371",
    "#FF7F50", "#20B2AA", "#DA70D6", "#6495ED", "#F4A460",
]
def getRandomColors(n):
    randomColors = []
    for i  in range(0, n):
        randomColors.append(colors[randint(0, len(colors)-1)])
    return randomColors

class baseGraph(FigureCanvas):
    def __init__(self, keys, values, labels):
        labels = list(labels)
        for i in range(0, len(labels)):
            labels[i] = str(labels[i])

        with plt.xkcd():
            self.fig, self.ax = plt.subplots(figsize=(4.5, 3),dpi =100)
            self._draw(keys, values, labels)
            self.fig.tight_layout()
        super().__init__(self.fig)

    @abstractmethod
    def _draw(self, keys, values, labels):
        pass

    def update_data(self, keys, values, labels):
        labels = list(labels)
        for i in range(0, len(labels)):
            labels[i] = str(labels[i])

        with plt.xkcd():
            self._draw(keys, values, labels)
            self.fig.tight_layout()
            self.draw()


class barGraph(baseGraph):
    def _draw(self, keys, values, labels):
        self.ax.clear()
        self.bars = self.ax.bar(labels, values, color=getRandomColors(len(labels)))
        self.ax.set_title("Alumnos inscritos por curso")
        self.ax.set_ylabel("Alumnos")
        plt.setp(self.ax.get_xticklabels(), rotation=80)
        self._keys = keys
        self._labels = labels
        self._values = values
        self.fig.canvas.mpl_connect('motion_notify_event', self._on_hover)
        
    def _on_hover(self, event):
        if event.inaxes == self.ax:
            for i, bar, in enumerate(self.bars):
                if bar.contains(event)[0]:
                    QToolTip.showText(
                        self.mapToGlobal(QPoint(int(event.x), self.height() - int(event.y))),
                        f"{self._labels[i]}: {self._keys[i]}\nAlumnos: {self._values[i]}"
                    )
                    return
        QToolTip.hideText()

class pieGraph(baseGraph):
    def _draw(self, keys, values, labels):
        self.ax.clear()
        self.slices, _, _ = self.ax.pie(values, labels = labels, colors = getRandomColors(len(labels)), autopct='%1.1f%%')
        self.ax.set_title("Alumnos por carrera")
        self._keys = keys
        self._labels = labels
        self._values = values
        self.fig.canvas.mpl_connect('motion_notify_event', self._on_hover)
    
    def _on_hover(self, event):
        if event.inaxes == self.ax:
            for i, slice, in enumerate(self.slices):
                if slice.contains(event)[0]:
                    QToolTip.showText(
                        self.mapToGlobal(QPoint(int(event.x), self.height() - int(event.y))),
                        f"{self._labels[i]}: {self._keys[i]}\nAlumnos: {self._values[i]}"
                    )
                    return
        QToolTip.hideText()