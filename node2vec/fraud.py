import sweetviz as sv

import pandas as pd

df=pd.read_csv('Payments.csv')

my_report = sv.analyze(df)


my_report.show_html()