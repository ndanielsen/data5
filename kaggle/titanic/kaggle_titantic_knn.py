# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# <codecell>

df = pd.read_csv("train.csv")

# <codecell>

df.describe()

# <codecell>

df.tail(15)

# <codecell>


# <codecell>

### Replacing Embarked by numberic

def f(x):
    if x == "S":
        return 1
    elif x == "C":
        return 2
    elif x == "Q":
        return 3
    else:
        return 0

# <codecell>

df["EmbarkedNum"] = df.Embarked.apply(f)

# <codecell>

df["Sex"] = df.Sex.map({'male':1, "female":2}) ### Replacing Sex is numeric

# <codecell>

pd.scatter_matrix(df)
plt.savefig('scatter_matrix.png', dpi=1000)

# <codecell>

df.groupby(['Pclass', 'Sex', 'Age']).Survived.count().plot(kind="kde")

# <codecell>

df.columns

# <codecell>

df.groupby(['Pclass', 'Sex', 'Parch']).Survived.count().plot(kind='bar')

# <codecell>

df.groupby(['Pclass', 'Sex', 'Embarked']).Survived.mean().plot(kind='bar')

# <codecell>

df.Embarked

# <codecell>

df.describe()

# <codecell>

### Categorizing DF by sex and pclass

df_male = df[df.Sex == 1]

df_female = df[df.Sex == 2]

df_male_poor = df[(df.Sex == 1) & (df.Pclass == 3)]

df_female_poor = df[(df.Sex == 2) & (df.Pclass == 3)]

# <codecell>


# <codecell>

df_male.groupby(['Survived', 'Pclass', 'Parch']).Age.count()

# <codecell>

df.head(1)

# <codecell>

df.columns

# <codecell>

# KNN with K=5
from sklearn.neighbors import KNeighborsClassifier  # import class
from sklearn.cross_validation import train_test_split
from sklearn import metrics

X = df_male[['EmbarkedNum', 'Age', 'Parch', 'Pclass']].fillna(0).values ### 85.5 %
y = df_male.Survived.values


X = df_male_poor[['EmbarkedNum', 'Age', 'Parch', 'Pclass']].fillna(0).values ### 85.05 %
y = df_male_poor.Survived.values


# <codecell>


X = df_female[['Age', 'Parch', 'Pclass', 'Fare']].fillna(0).values # 74.68
y = df_female.Survived.values



# <codecell>

X = df_female_poor[['Pclass', 'EmbarkedNum'].fillna(0).values # 72.22%
y = df_female_poor.Survived.values

# <codecell>

X = df_female_poor[['Pclass', 'Parch', 'Fare']].fillna(0).values # 75%
y = df_female_poor.Survived.values

# <codecell>

def evaluate(train_test_values):
    X_train, X_test, y_train, y_test = train_test_values
    results = []
    
    num = 1
    while num < 100: # definitely refactor this to use xrange (need more coffee next time)
        knn = KNeighborsClassifier(n_neighbors=num)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        score = metrics.accuracy_score(y_test, y_pred)
        results.append((score, num))
        num += 1
    return max(results) 

# <codecell>


# <codecell>

train_test_values = train_test_split(X, y, random_state=2)
evaluate(train_test_values)

# <codecell>


# <codecell>


# <codecell>


