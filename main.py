import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Administrator/Downloads/HR.csv")

sns.set_style(style="whitegrid")
sns.set_context(context="poster", font_scale=0.8)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))

lbs=df["salary"].value_counts().index
explodes=[0.1 if i=="low" else 0 for i in lbs]
plt.pie(df["salary"].value_counts(normalize=True), explode=explodes, labels=lbs, autopct="%1.1f%%", colors=sns.color_palette("Reds"))

# sns.pointplot(x="time_spend_company", y="left", data=df)

# sub_df = df.groupby("time_spend_company").mean()
# sns.pointplot(sub_df.index, sub_df["left"])

#sns.boxplot(x=df["time_spend_company"], saturation=0.75, whis=3)
# f=plt.figure()
# f.add_subplot(1,3,1)
# sns.distplot(df["satisfaction_level"], bins=10)
# f.add_subplot(1,3,2)
# sns.distplot(df["last_evaluation"], bins=10)
# f.add_subplot(1,3,3)
# sns.distplot(df["average_monthly_hours"], bins=10)
# sns.countplot(x="salary", hue="department", data=df)
plt.show()
# plt.title("SALARY")
# plt.xlabel("Salary")
# plt.ylabel("Number")
# plt.xticks(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts().index)
# plt.axis([0,4,0,10000])
# plt.bar(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts(), width=0.5)
# for x,y in zip(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts()):
#     plt.text(x,y,y,ha="center", va="bottom")
# plt.show()