# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class ScribbleArea(QtGui.QWidget):
    """
      this scales the image but it's not good, too many refreshes really mess it up!!!
    """
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 20
        self.myPenColor = QtCore.Qt.black
        self.image = QtGui.QImage()
        self.lastPoint = QtCore.QPoint()


    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):
        self.resizeImage(self.image, event.size())
        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        # this resizes the canvas without resampling the image
        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)


##  this resampled the image but it gets messed up with so many events...
        #painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        #painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)




        self.image = newImage

    def print_(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)

        printDialog = QtGui.QPrintDialog(printer, self)
        if printDialog.exec_() == QtGui.QDialog.Accepted:
            painter = QtGui.QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class LoggedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()

        self.label = QtGui.QLabel('6 JE JAKA')
        layout.addWidget(self.label)
        self.setLayout(layout)

class Scribble(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Scribble, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        layout2 = QtGui.QHBoxLayout()

        self.izracunaj = QtGui.QPushButton('IZRACUNAJ')
        self.pobrisi = QtGui.QPushButton('POBRISI')
        layout2.addWidget(self.izracunaj)
        layout2.addWidget(self.pobrisi)

        layout.addLayout(layout2)
        self.scribbleArea = ScribbleArea(self)

        self.slika = self.scribbleArea.image
        self.setWindowTitle("Scribble")
        self.scribbleArea.resize(1500,1500)
        layout.addWidget(self.scribbleArea)
        self.setLayout(layout)

        #self.centralWidget = QtGui.QWidget(self)
    def saveImage(self, fileName, fileFormat):
        visibleImage = self.scribbleArea.image
        #ScribbleArea.resizeImage(visibleImage, self.size())
        import numpy as np
        #visibleImage = QtGui.QImage(visibleImage.scaled(28,28))
        #= QtGui.QPixmap.fromImage(visibleImage)

        #qp.scaled(10,10,QtCore.Qt.KeepAspectRatio)

        from sklearn.externals import joblib
        clf = joblib.load('../Models/RandomForestModel.pkl')
        qrgb = visibleImage.pixel(0, 0)
        #print("QRGB Values: " + str(qrgb))
        # Convert it to QColor
        qrgb_to_QCol = QtGui.QColor(qrgb)
        rgba = qrgb_to_QCol.getRgb()
        #print("RGBA Values: " + str(rgba))
        li_num_width = []
        for i in range(500):
            li_num_width.append(i)

        # Generate a list of numbers for height
        li_num_height = []
        for i in range(500):
            li_num_height.append(i)

        # List for x num
        x = [li_num_width for i in range(len(li_num_height))]
        #print("\nX list is:\n" + str(x))

        # List for y num
        for i in range(len(li_num_height)):
            y = [[i]*len(li_num_width) for i in range(len(li_num_height))]
        #print("\nY list is:\n" + str(y))

        row_el_li = []
        row_el_li_y = []

        # Obtain list numbers for x
        for i in range(len(li_num_height)):
            row = x[i]
            for i in range(len(li_num_width)):
                row_el = row[i]
                #print(row_el)
                row_el_li.append(row_el)

        #print("\nRow Elements list x: \n" + str(row_el_li))

        # Obtain list numbers for y
        for i in range(len(li_num_height)):
            row_y = y[i]
            for i in range(len(li_num_width)):
                row_el_y = row_y[i]
                #print(row_el_y)
                row_el_li_y.append(row_el_y)

        #print("\nRow Elements list y: \n" + str(row_el_li_y))

        # Create a list, which eventualy will hold qrgb values, which is our goal
        qrgb_li = []
        # How many values will the list hold? or How many pixels in the image do we have?
        num_pixels = len(li_num_width) * len(li_num_height)
        #print("\nNumber of Pixels:" + str(num_pixels))

        for i in range(num_pixels):
            #print "Juhj"
            ordered_qrgb = visibleImage.pixel(row_el_li[i], row_el_li_y[i])
            qrgb_li.append(ordered_qrgb)
        #print qrgb_li

        # One more step lets convert from QRGB list to RGBA list, which will lead us to the end of this tutorial
        rgba_li = []

        for i in range(len(qrgb_li)):
            qrgb_li_to_QCol = QtGui.QColor(qrgb_li[i])
            rgba_set = qrgb_li_to_QCol.getRgb()
            rgba_li.append(rgba_set[0])
        for i in range(len(rgba_li)):
            if(rgba_li[i] == 255):
                rgba_li[i] = 0
            else:
                rgba_li[i] = 255


        data = np.zeros((500,500), dtype=np.uint8)
        import scipy.misc as smp
        j = 0
        for i in range(len(rgba_li)):
            if((i%500 == 0) and (i != 0)):
                j += 1
            data[j,(i%500)] = rgba_li[i]
        #img = smp.toimage( data )       # Create a PIL image
        #img.show()
        import scipy
        a = np.array(data, dtype=np.uint8)
        #print(a)
        res = scipy.misc.imresize(a,(28,28), interp="bicubic")
        #print(res)
        img = smp.toimage(res)
        img.show()



        #img = smp.toimage(np.array(tmp) )       # Create a PIL image
        #img.show()


        #
        # print(rgba_li)
        print(res)
        tmp = []
        for i in res:
            for z in i:
                tmp.append(z)
        y_pred = clf.predict([tmp])
        print(y_pred)

        from csv import DictReader
        import collections
        import numpy as np

        import Image
        visibleImage.save(fileName,fileFormat)
        #if visibleImage.save(fileName, fileFormat):
         #   visibleImage.modified = False
#            return True
 #       else:
  #          return False



    def podatki(self):
        from PyQt4 import QtGui, QtCore
        img = self.slika
        if(img == None):
            print "juhej"



class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)


        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.resize(518,566)
        login_widget = Scribble(self)
        login_widget.izracunaj.clicked.connect(lambda : login_widget.saveImage("jusa", "png"))
        login_widget.pobrisi.clicked.connect(lambda : login_widget.scribbleArea.clearImage())
        self.central_widget.addWidget(login_widget)
        login_widget.saveImage("juhje", ".gif")

    def login(self):
        print "juhej"

    def commander (self, arg):
        exec arg




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())
