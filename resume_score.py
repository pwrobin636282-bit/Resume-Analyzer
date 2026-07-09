import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('recommendation.csv')
filtered=df['candidate_0001.pdf']
print(filtered)