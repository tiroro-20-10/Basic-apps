from PyQt5 import QtWidgets, QtGui, QtCore, uic

operand = None
operation = None
pending = False
click_point = False


class FQMessageBox(QtWidgets.QMessageBox):
    def paintEvent(self, e: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        grad = QtGui.QLinearGradient(QtCore.QPoint(0, 0),
                                     QtCore.QPoint(self.rect().width(),
                                                   self.rect().height()))
        grad.setColorAt(0 / 6, QtGui.QColor(255, 0, 0))
        grad.setColorAt(1 / 6, QtGui.QColor(255, 127, 0))
        grad.setColorAt(2 / 6, QtGui.QColor(255, 255, 0))
        grad.setColorAt(3 / 6, QtGui.QColor(0, 255, 0))
        grad.setColorAt(4 / 6, QtGui.QColor(0, 0, 255))
        grad.setColorAt(5 / 6, QtGui.QColor(75, 0, 130))
        grad.setColorAt(6 / 6, QtGui.QColor(148, 0, 211))
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(grad)
        painter.drawRect(self.rect())


def CR_CR():
    CR = QtWidgets.QMessageBox()
    CR.setIcon(QtWidgets.QMessageBox.Critical)
    CR.setWindowTitle("XD")
    CR.setText("Result too large\nPress F...")
    CR.move(Form.geometry().center() - QtCore.QPoint(85, 90))

    yes_button = CR.addButton('F', QtWidgets.QMessageBox.YesRole)
    yes_button.clicked.disconnect()
    yes_button.clicked.connect(F_F)

    CR.F_sh = QtWidgets.QShortcut(QtGui.QKeySequence("f"), CR)
    CR.F_sh.activated.connect(F_F)

    CR.F_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), CR)
    CR.F_sh.activated.connect(CR.close)

    CR.F_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Space"), CR)
    CR.F_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), CR)
    CR.F_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), CR)

    CR.show()
    CR.exec()


def F_F():
    F = FQMessageBox()
    F.setWindowTitle(":|:")
    F.setText("Gradient\nQMB)))")

    F.move(Form.geometry().center() - QtCore.QPoint(50, 50))
    F.show()
    F.exec()


def click_on_point(point):
    def inner():
        global click_point
        display = Form.display_1
        text = Form.display_1.text()
        if not click_point:
            display.setText(text + point)
            click_point = True
    return inner


def click_on_number(digit):
    def inner():
        global pending
        global click_point
        display = Form.display_1
        text = Form.display_1.text()
        if text == '0' or pending:
            display.setText(digit)
            pending = False
            click_point = False
        elif click_point and pending:
            display.setText(text + digit)
            pending = False
        else:
            display.setText(text + digit)
    return inner

def click_on_zero(zeros):
    def inner():
        global pending
        global click_point
        display = Form.display_1
        text = Form.display_1.text()
        if pending:
            display.setText('0')
            click_point = False
            pending = False
        elif text != '0':
            display.setText(text + zeros)

    return inner

def do_operation():
    global operand
    global operation
    global pending
    global click_point

    try:
        if operation:
            Form.display_2.setText(Form.display_2.text() + Form.display_1.text())
            result = float(operation(operand, float(Form.display_1.text())))
            Form.display_1.setText(str(result))
    except ZeroDivisionError:
        Form.display_1.setText("Can't divide by zero!")
    except OverflowError:
        CR_CR()
        Form.pushButton_clear.click()


    operand = None
    operation = None
    pending = True
    click_point = True

def click_on_action(action):
    def inner():
        global pending
        global operand
        global operation
        display = Form.display_1
        if not operand:
            Form.display_2.setText(Form.display_2.text() + Form.display_1.text())
        if operand:
            do_operation()
        operation = action
        try:
            operand = float(display.text())
        except ValueError:
            operand = None
            operation = None
        pending = True
    return inner

def clear():
    def inner():
        global operand
        global operation
        global pending
        global click_point
        Form.display_1.setText('0')
        Form.display_2.setText('')
        operand = None
        operation = None
        pending = False
        click_point = False
    return inner

def clean_entry():
    def inner():
        global click_point
        global pending
        Form.display_1.setText('0')
        pending = False
        click_point = False
    return inner

def clear_arrow():
    def inner():
        global click_point
        text = Form.display_1.text()
        if text[-1:] == '.':
            click_point = False
        if len(text) == 1:
            Form.display_1.setText('0')
        else:
            Form.display_1.setText(text[:-1])
    return inner

def output_display_2(symbol):
    def inner():
        global pending
        if pending:
            Form.display_2.setText(Form.display_2.text() + symbol)
    return inner

def eq_print():
    global pending
    display2 = Form.display_2.text()
    if display2:
        print("Display_2: " + Form.display_2.text() + "=" + Form.display_1.text())
        Form.display_2.setText('')

def plus_minus():
    display_1_text = Form.display_1.text()
    if display_1_text != '0':
        result = -1 * float(display_1_text)
        Form.display_1.setText(str(result))


app = QtWidgets.QApplication([])

Form = uic.loadUi("calc_5.ui")

Form.pushButton_000.clicked.connect(click_on_zero("000"))
Form.pushButton_0.clicked.connect(click_on_zero("0"))
Form.pushButton_1.clicked.connect(click_on_number("1"))
Form.pushButton_2.clicked.connect(click_on_number("2"))
Form.pushButton_3.clicked.connect(click_on_number("3"))
Form.pushButton_4.clicked.connect(click_on_number("4"))
Form.pushButton_5.clicked.connect(click_on_number("5"))
Form.pushButton_6.clicked.connect(click_on_number("6"))
Form.pushButton_7.clicked.connect(click_on_number("7"))
Form.pushButton_8.clicked.connect(click_on_number("8"))
Form.pushButton_9.clicked.connect(click_on_number("9"))
Form.pushButton_point.clicked.connect(click_on_point("."))

Form.pushButton_clear.clicked.connect(clear())
Form.pushButton_arrow.clicked.connect(clear_arrow())
Form.pushButton_clean_entry.clicked.connect(clean_entry())
Form.pushButton_add.clicked.connect(click_on_action(lambda x, y: x + y))
Form.pushButton_sub.clicked.connect(click_on_action(lambda x, y: x - y))
Form.pushButton_mul.clicked.connect(click_on_action(lambda x, y: x * y))
Form.pushButton_div.clicked.connect(click_on_action(lambda x, y: x / y))
Form.pushButton_div_rem.clicked.connect(click_on_action(lambda x, y: x % y))
Form.pushButton_degr.clicked.connect(click_on_action(lambda x, y: x ** y))
Form.pushButton_plus_minus.clicked.connect(plus_minus)
Form.pushButton_eq.clicked.connect(do_operation)


Form.pushButton_add.clicked.connect(output_display_2("+"))
Form.pushButton_sub.clicked.connect(output_display_2("-"))
Form.pushButton_mul.clicked.connect(output_display_2("*"))
Form.pushButton_div.clicked.connect(output_display_2("/"))
Form.pushButton_degr.clicked.connect(output_display_2("^"))
Form.pushButton_div_rem.clicked.connect(output_display_2("%"))
Form.pushButton_eq.clicked.connect(eq_print)

Form.quit_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), Form)
Form.quit_sh.activated.connect(Form.close)

Form.pushButton_000_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+0"), Form)
Form.pushButton_000_sh.activated.connect(Form.pushButton_000.animateClick)

Form.pushButton_0_sh = QtWidgets.QShortcut(QtGui.QKeySequence("0"), Form)
Form.pushButton_0_sh.activated.connect(Form.pushButton_0.animateClick)

Form.pushButton_1_sh = QtWidgets.QShortcut(QtGui.QKeySequence("1"), Form)
Form.pushButton_1_sh.activated.connect(Form.pushButton_1.animateClick)

Form.pushButton_2_sh = QtWidgets.QShortcut(QtGui.QKeySequence("2"), Form)
Form.pushButton_2_sh.activated.connect(Form.pushButton_2.animateClick)

Form.pushButton_3_sh = QtWidgets.QShortcut(QtGui.QKeySequence("3"), Form)
Form.pushButton_3_sh.activated.connect(Form.pushButton_3.animateClick)

Form.pushButton_4_sh = QtWidgets.QShortcut(QtGui.QKeySequence("4"), Form)
Form.pushButton_4_sh.activated.connect(Form.pushButton_4.animateClick)

Form.pushButton_5_sh = QtWidgets.QShortcut(QtGui.QKeySequence("5"), Form)
Form.pushButton_5_sh.activated.connect(Form.pushButton_5.animateClick)

Form.pushButton_6_sh = QtWidgets.QShortcut(QtGui.QKeySequence("6"), Form)
Form.pushButton_6_sh.activated.connect(Form.pushButton_6.animateClick)

Form.pushButton_7_sh = QtWidgets.QShortcut(QtGui.QKeySequence("7"), Form)
Form.pushButton_7_sh.activated.connect(Form.pushButton_7.animateClick)

Form.pushButton_8_sh = QtWidgets.QShortcut(QtGui.QKeySequence("8"), Form)
Form.pushButton_8_sh.activated.connect(Form.pushButton_8.animateClick)

Form.pushButton_9_sh = QtWidgets.QShortcut(QtGui.QKeySequence("9"), Form)
Form.pushButton_9_sh.activated.connect(Form.pushButton_9.animateClick)

Form.pushButton_point_sh = QtWidgets.QShortcut(QtGui.QKeySequence("."), Form)
Form.pushButton_point_sh.activated.connect(Form.pushButton_point.animateClick)


Form.pushButton_clear_sh = QtWidgets.QShortcut(QtGui.QKeySequence("c"), Form)
Form.pushButton_clear_sh.activated.connect(Form.pushButton_clear.animateClick)

Form.pushButton_arrow_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Backspace"), Form)
Form.pushButton_arrow_sh.activated.connect(Form.pushButton_arrow.animateClick)

Form.pushButton_clean_entry_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+c"), Form)
Form.pushButton_clean_entry_sh.activated.connect(Form.pushButton_clean_entry.animateClick)

Form.pushButton_add_sh = QtWidgets.QShortcut(QtGui.QKeySequence("+"), Form)
Form.pushButton_add_sh.activated.connect(Form.pushButton_add.animateClick)

Form.pushButton_sub_sh = QtWidgets.QShortcut(QtGui.QKeySequence("-"), Form)
Form.pushButton_sub_sh.activated.connect(Form.pushButton_sub.animateClick)

Form.pushButton_mul_sh = QtWidgets.QShortcut(QtGui.QKeySequence("*"), Form)
Form.pushButton_mul_sh.activated.connect(Form.pushButton_mul.animateClick)

Form.pushButton_div_sh = QtWidgets.QShortcut(QtGui.QKeySequence("/"), Form)
Form.pushButton_div_sh.activated.connect(Form.pushButton_div.animateClick)

Form.pushButton_div_rem_sh = QtWidgets.QShortcut(QtGui.QKeySequence("%"), Form)
Form.pushButton_div_rem_sh.activated.connect(Form.pushButton_div_rem.animateClick)

Form.pushButton_degr_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Shift+6"), Form)
Form.pushButton_degr_sh.activated.connect(Form.pushButton_degr.animateClick)

Form.pushButton_eq_sh = QtWidgets.QShortcut(QtGui.QKeySequence("="), Form)
Form.pushButton_eq_sh.activated.connect(Form.pushButton_eq.animateClick)

Form.pushButton_eq_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), Form)
Form.pushButton_eq_sh.activated.connect(Form.pushButton_eq.animateClick)

Form.pushButton_eq_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), Form)
Form.pushButton_eq_sh.activated.connect(Form.pushButton_eq.animateClick)

Form.pushButton_plus_minus_sh = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+-"), Form)
Form.pushButton_plus_minus_sh.activated.connect(Form.pushButton_plus_minus.animateClick)


Form.show()

app.exec()
