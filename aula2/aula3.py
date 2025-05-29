import pandas as pd
import numpy as np

caminho = ("../data/(2) notas_pisa.csv")

df = pd.read_csv(caminho, sep=",")

print(df)