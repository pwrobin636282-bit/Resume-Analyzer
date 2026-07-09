import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('recommendations.csv')
#print(df)

#print(df["Recommended Job"].head())

#print(df['Recommended Job'].value_counts().head())
'''print(df['Match Percentage'].mean())
print(df['Match Percentage'].max())
print(df['Match Percentage'].min())
filtered_rows=df[(df['Match Percentage']>=80)]
print(filtered_rows)
filtered=df[(df['Match Percentage']<40)]
print(filtered)'''

#Doing something which I even dont know
all_skills=[]
filtered_data=df['Recommended Job']
for i in filtered_data:
    skills=i.split(",")
    
    for sk in skills:
        sk=sk.strip()
        all_skills.extend(skills)
    

skill=pd.Series(all_skills)
print(skill)
shit=skill.value_counts().head(10)
print(shit)

plt.xlabel("Recommended Jobs")
plt.ylabel("Number of Recommendations")
plt.figure(figsize=(10,6))
plt.bar(shit.index, shit.values, color='red')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''import matplotlib.pyplot as plt 
plt.hist(df['Match Percentage'], bins = 10, color='Red', edge_color='Black')
plt.show()'''



