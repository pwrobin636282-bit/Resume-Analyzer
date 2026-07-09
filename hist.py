'''import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('recommendations.csv')

plt.hist(df['Match Percentage'], bins=10, color='Red', edgecolor='Black')
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('recommendation.csv')

plt.xlabel("Recommended Jobs")
plt.ylabel("No. of applications")
plt.bar(Recommended Job , Match Count, color='Red')
plt.show()