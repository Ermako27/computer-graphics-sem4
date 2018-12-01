/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>
#include "qcustomplot.h"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGraphicsView *graphicsView;
    QLineEdit *lineEdit;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QLabel *label_3;
    QLabel *label_4;
    QLineEdit *lineEdit_3;
    QLineEdit *lineEdit_4;
    QLabel *label_5;
    QLabel *label_6;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QRadioButton *radioButton_3;
    QRadioButton *radioButton_4;
    QRadioButton *radioButton_5;
    QWidget *gridLayoutWidget_2;
    QGridLayout *gridLayout_2;
    QRadioButton *radioButton_6;
    QRadioButton *radioButton_8;
    QRadioButton *radioButton_7;
    QRadioButton *radioButton_9;
    QRadioButton *radioButton_10;
    QWidget *gridLayoutWidget_3;
    QGridLayout *gridLayout_3;
    QRadioButton *radioButton_13;
    QRadioButton *radioButton_12;
    QRadioButton *radioButton_11;
    QRadioButton *radioButton_14;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QCustomPlot *widget;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QLineEdit *lineEdit_5;
    QLabel *label_12;
    QLineEdit *lineEdit_6;
    QLabel *label_11;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1237, 1000);
        MainWindow->setMinimumSize(QSize(1000, 1000));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));
        graphicsView->setGeometry(QRect(20, 10, 491, 471));
        graphicsView->setMinimumSize(QSize(400, 400));
        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(870, 20, 91, 31));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(850, 20, 16, 16));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(850, 60, 16, 16));
        lineEdit_2 = new QLineEdit(centralWidget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(869, 60, 91, 31));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(980, 20, 16, 16));
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(980, 60, 16, 16));
        lineEdit_3 = new QLineEdit(centralWidget);
        lineEdit_3->setObjectName(QStringLiteral("lineEdit_3"));
        lineEdit_3->setGeometry(QRect(1000, 20, 91, 31));
        lineEdit_4 = new QLineEdit(centralWidget);
        lineEdit_4->setObjectName(QStringLiteral("lineEdit_4"));
        lineEdit_4->setGeometry(QRect(1000, 60, 91, 31));
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(530, 150, 81, 31));
        QFont font;
        font.setUnderline(true);
        label_5->setFont(font);
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(650, 150, 81, 31));
        label_6->setFont(font);
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(531, 180, 91, 141));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        radioButton = new QRadioButton(gridLayoutWidget);
        radioButton->setObjectName(QStringLiteral("radioButton"));

        gridLayout->addWidget(radioButton, 0, 0, 1, 1);

        radioButton_2 = new QRadioButton(gridLayoutWidget);
        radioButton_2->setObjectName(QStringLiteral("radioButton_2"));

        gridLayout->addWidget(radioButton_2, 1, 0, 1, 1);

        radioButton_3 = new QRadioButton(gridLayoutWidget);
        radioButton_3->setObjectName(QStringLiteral("radioButton_3"));

        gridLayout->addWidget(radioButton_3, 2, 0, 1, 1);

        radioButton_4 = new QRadioButton(gridLayoutWidget);
        radioButton_4->setObjectName(QStringLiteral("radioButton_4"));

        gridLayout->addWidget(radioButton_4, 3, 0, 1, 1);

        radioButton_5 = new QRadioButton(gridLayoutWidget);
        radioButton_5->setObjectName(QStringLiteral("radioButton_5"));

        gridLayout->addWidget(radioButton_5, 4, 0, 1, 1);

        gridLayoutWidget_2 = new QWidget(centralWidget);
        gridLayoutWidget_2->setObjectName(QStringLiteral("gridLayoutWidget_2"));
        gridLayoutWidget_2->setGeometry(QRect(650, 180, 91, 141));
        gridLayout_2 = new QGridLayout(gridLayoutWidget_2);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        radioButton_6 = new QRadioButton(gridLayoutWidget_2);
        radioButton_6->setObjectName(QStringLiteral("radioButton_6"));

        gridLayout_2->addWidget(radioButton_6, 0, 0, 1, 1);

        radioButton_8 = new QRadioButton(gridLayoutWidget_2);
        radioButton_8->setObjectName(QStringLiteral("radioButton_8"));

        gridLayout_2->addWidget(radioButton_8, 2, 0, 1, 1);

        radioButton_7 = new QRadioButton(gridLayoutWidget_2);
        radioButton_7->setObjectName(QStringLiteral("radioButton_7"));

        gridLayout_2->addWidget(radioButton_7, 1, 0, 1, 1);

        radioButton_9 = new QRadioButton(gridLayoutWidget_2);
        radioButton_9->setObjectName(QStringLiteral("radioButton_9"));

        gridLayout_2->addWidget(radioButton_9, 3, 0, 1, 1);

        radioButton_10 = new QRadioButton(gridLayoutWidget_2);
        radioButton_10->setObjectName(QStringLiteral("radioButton_10"));

        gridLayout_2->addWidget(radioButton_10, 4, 0, 1, 1);

        gridLayoutWidget_3 = new QWidget(centralWidget);
        gridLayoutWidget_3->setObjectName(QStringLiteral("gridLayoutWidget_3"));
        gridLayoutWidget_3->setGeometry(QRect(530, 20, 305, 112));
        gridLayout_3 = new QGridLayout(gridLayoutWidget_3);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        radioButton_13 = new QRadioButton(gridLayoutWidget_3);
        radioButton_13->setObjectName(QStringLiteral("radioButton_13"));

        gridLayout_3->addWidget(radioButton_13, 2, 0, 1, 1);

        radioButton_12 = new QRadioButton(gridLayoutWidget_3);
        radioButton_12->setObjectName(QStringLiteral("radioButton_12"));

        gridLayout_3->addWidget(radioButton_12, 1, 0, 1, 1);

        radioButton_11 = new QRadioButton(gridLayoutWidget_3);
        radioButton_11->setObjectName(QStringLiteral("radioButton_11"));

        gridLayout_3->addWidget(radioButton_11, 0, 0, 1, 1);

        radioButton_14 = new QRadioButton(gridLayoutWidget_3);
        radioButton_14->setObjectName(QStringLiteral("radioButton_14"));

        gridLayout_3->addWidget(radioButton_14, 3, 0, 1, 1);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(850, 110, 261, 41));
        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(850, 250, 261, 41));
        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(529, 350, 251, 41));
        widget = new QCustomPlot(centralWidget);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(850, 350, 401, 181));
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(560, 400, 111, 16));
        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(560, 420, 281, 16));
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(560, 440, 251, 16));
        label_10 = new QLabel(centralWidget);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(560, 460, 251, 16));
        pushButton_4 = new QPushButton(centralWidget);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(530, 480, 291, 51));
        pushButton_5 = new QPushButton(centralWidget);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(20, 510, 351, 41));
        lineEdit_5 = new QLineEdit(centralWidget);
        lineEdit_5->setObjectName(QStringLiteral("lineEdit_5"));
        lineEdit_5->setGeometry(QRect(850, 190, 81, 31));
        label_12 = new QLabel(centralWidget);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(850, 170, 59, 14));
        lineEdit_6 = new QLineEdit(centralWidget);
        lineEdit_6->setObjectName(QStringLiteral("lineEdit_6"));
        lineEdit_6->setGeometry(QRect(1010, 190, 81, 31));
        label_11 = new QLabel(centralWidget);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(1010, 170, 67, 17));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1237, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "image", nullptr));
#ifndef QT_NO_TOOLTIP
        MainWindow->setToolTip(QString());
#endif // QT_NO_TOOLTIP
        label->setText(QApplication::translate("MainWindow", "X1", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "Y1", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "X2", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Y2", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "\320\246\320\262\320\265\321\202 \321\204\320\276\320\275\320\260", nullptr));
        label_6->setText(QApplication::translate("MainWindow", "\320\246\320\262\320\265\321\202 \320\273\320\270\320\275\320\270\320\270", nullptr));
        radioButton->setText(QApplication::translate("MainWindow", "\320\247\320\265\321\200\320\275\321\213\320\271", nullptr));
        radioButton_2->setText(QApplication::translate("MainWindow", "\320\221\320\265\320\273\321\213\320\271", nullptr));
        radioButton_3->setText(QApplication::translate("MainWindow", "\320\227\320\265\320\273\320\265\320\275\321\213\320\271", nullptr));
        radioButton_4->setText(QApplication::translate("MainWindow", "\320\232\321\200\320\260\321\201\320\275\321\213\320\271", nullptr));
        radioButton_5->setText(QApplication::translate("MainWindow", "\320\241\320\270\320\275\320\270\320\271", nullptr));
        radioButton_6->setText(QApplication::translate("MainWindow", "\320\247\320\265\321\200\320\275\321\213\320\271", nullptr));
        radioButton_8->setText(QApplication::translate("MainWindow", "\320\227\320\265\320\273\320\265\320\275\321\213\320\271", nullptr));
        radioButton_7->setText(QApplication::translate("MainWindow", "\320\221\320\265\320\273\321\213\320\271", nullptr));
        radioButton_9->setText(QApplication::translate("MainWindow", "\320\232\321\200\320\260\321\201\320\275\321\213\320\271", nullptr));
        radioButton_10->setText(QApplication::translate("MainWindow", "\320\241\320\270\320\275\320\270\320\271", nullptr));
        radioButton_13->setText(QApplication::translate("MainWindow", "\320\221\321\200\320\265\320\267\320\265\320\275\321\205\320\265\320\274(\321\201 \321\206\320\265\320\273\321\213\320\274\320\270 \321\207\320\270\321\201\320\273\320\260\320\274\320\270)", nullptr));
        radioButton_12->setText(QApplication::translate("MainWindow", "\320\221\321\200\320\265\320\267\320\265\320\275\321\205\320\265\320\274(\321\201 \320\264\320\265\320\271\321\201\321\202\320\262\320\270\321\202. \321\207\320\270\321\201\320\273\320\260\320\274\320\270)", nullptr));
        radioButton_11->setText(QApplication::translate("MainWindow", "\320\246\320\224\320\220", nullptr));
        radioButton_14->setText(QApplication::translate("MainWindow", "\320\221\321\200\320\265\320\267\320\265\320\275\321\205\320\265\320\274 (\321\203\321\201\321\202\321\200\320\260\320\275\320\265\320\275\320\270\320\265 \321\201\321\202\321\203\320\277\320\265\320\275\321\207\320\260\321\202\320\276\321\201\321\202\320\270)", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "\320\237\320\276\321\201\321\202\321\200\320\276\320\270\321\202\321\214 \320\273\320\270\320\275\320\270\321\216", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "\320\237\320\276\321\201\321\202\321\200\320\276\320\270\321\202\321\214 \320\267\320\262\320\265\320\267\320\264\321\203", nullptr));
        pushButton_3->setText(QApplication::translate("MainWindow", "\320\223\321\200\320\260\321\204\320\270\320\272 \320\262\321\200\320\265\320\274\320\265\320\275\320\270", nullptr));
        label_7->setText(QApplication::translate("MainWindow", "1- \320\246\320\224\320\220", nullptr));
        label_8->setText(QApplication::translate("MainWindow", "2- \320\221\321\200\320\265\320\267\320\275\321\205\320\265\320\274 (\320\264\320\265\320\271\321\201\321\202\320\262\320\270\321\202\320\265\320\273\321\214\320\275\321\213\320\265)", nullptr));
        label_9->setText(QApplication::translate("MainWindow", "3- \320\221\321\200\320\265\320\267\320\275\321\205\320\265\320\274 (\321\206\320\265\320\273\321\213\320\265)", nullptr));
        label_10->setText(QApplication::translate("MainWindow", "4- \320\221\321\200\320\265\320\267\320\275\321\205\320\265\320\274 \321\201\320\276 \321\201\320\263\320\273\320\260\320\266\320\270\320\262\320\260\320\275\320\270\320\265\320\274", nullptr));
        pushButton_4->setText(QApplication::translate("MainWindow", "\320\232\320\276\320\273\320\270\321\207\320\265\321\201\321\202\320\262\320\276 \321\201\321\202\321\203\320\277\320\265\320\275\320\265\320\272 \320\276\321\202 \321\203\320\263\320\273\320\260 \320\275\320\260\320\272\320\273\320\276\320\275\320\260", nullptr));
        pushButton_5->setText(QApplication::translate("MainWindow", "\320\236\321\207\320\270\321\201\321\202\320\270\321\202\321\214 \320\276\320\272\320\275\320\276", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "\320\250\320\260\320\263", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "\320\264\320\270\320\260\320\274\320\265\321\202\321\200", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
