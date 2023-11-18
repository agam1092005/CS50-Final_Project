import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

homePageURL = "https://agam1092005.github.io/CS50-Final_Project/"
permissonGrant = False

if not permissonGrant:
    class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
        def __init__(self, parent=None):
            global permissonGrant
            super(WebEnginePage, self).__init__(parent)
            self.featurePermissionRequested.connect(self.handleFeaturePermissionRequested)

        @QtCore.pyqtSlot(QtCore.QUrl, QtWebEngineWidgets.QWebEnginePage.Feature)
        def handleFeaturePermissionRequested(self, securityOrigin, feature):
            global permissonGrant
            title = "Permission Request"
            questionForFeature = {
                QtWebEngineWidgets.QWebEnginePage.Geolocation: "Allow {feature} to access your location information?",
            }
            question = questionForFeature.get(feature)
            if question:
                question = question.format(feature=securityOrigin.host())
                if QtWidgets.QMessageBox.question(self.view().window(), title, question) == QtWidgets.QMessageBox.Yes:
                    self.setFeaturePermission(securityOrigin, feature, QtWebEngineWidgets.QWebEnginePage.PermissionGrantedByUser)
                    permissonGrant = True
                else:
                    self.setFeaturePermission(securityOrigin, feature, QtWebEngineWidgets.QWebEnginePage.PermissionDeniedByUser)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setWindowTitle("SyncFusionX")
        self.browser.setPage(WebEnginePage(self.browser))
        self.browser.setUrl(QUrl(homePageURL))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)
        home = QAction("Home", self)
        home.triggered.connect(self.navigate_home)
        back = QAction("Back", self)
        back.triggered.connect(self.browser.back)
        forward = QAction("Forward", self)
        forward.triggered.connect(self.browser.forward)
        reload = QAction("Reload", self)
        reload.triggered.connect(self.browser.reload)
        navbar.addActions([home, back, forward, reload])

        self.url_bar = QLineEdit()
        self.url_bar.setReadOnly(True)
        self.url_bar.setText("SyncFusionX")
        # whenever url is homepageURl then setText to "SyncFusionX"
        self.browser.urlChanged.connect(self.update_barurl)
        navbar.addWidget(self.url_bar)

    def navigate_home(self):
        self.browser.setUrl(QUrl(homePageURL))

    def update_barurl(self, newURL):
        self.url_bar.setText(newURL.toString())


browser = QApplication(sys.argv)
QApplication.setApplicationDisplayName("SyncFusionX")
QApplication.setApplicationName("SyncFusionX")
window = MainWindow()
browser.exec_()
