import xlwings as xw
import pandas as pd
MyBook = xw.Book('msan.xlsx')
MySheet = MyBook.sheets('Порты')
