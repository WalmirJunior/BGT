import pyqtgraph as pg
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication

def generate_chart(logs):
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    w = QWidget()
    layout = QVBoxLayout()
    plot = pg.PlotWidget(title="Ganho Diário")
    dates = [l[1] for l in logs]  # pegar coluna date
    gains = [l[4] for l in logs]  # pegar coluna ganho (gold_end - gold_start)
    plot.plot(list(range(len(gains))), gains, pen=pg.mkPen(color='magenta', width=2))

    # Ajusta ticks do eixo X com as datas (pra ficar legível, mostra só algumas datas)
    ticks = [(i, dates[i]) for i in range(len(dates)) if i % max(1, len(dates)//10) == 0]
    plot.getPlotItem().getAxis('bottom').setTicks([ticks])

    layout.addWidget(plot)
    w.setLayout(layout)
    w.resize(600, 400)
    w.show()
    # pra garantir que a janela não seja destruída
    plot.app = w
