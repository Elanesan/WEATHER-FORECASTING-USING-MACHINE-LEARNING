import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random


data = pd.read_csv("/content/seattle-weather.csv")

X = data[["temp_max", "temp_min", "wind"]]  
y = data["weather"]  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


model = GaussianNB()


model.fit(X_train, y_train)

y_pred = model.predict(X_test)  

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


new_temp_max = float(input("Enter Maximum Temperature(Fahrenheit) for new data: "))
new_temp_min = float(input("Enter Minimum Temperature(Fahrenheit) for new data: "))
new_wind = float(input("Enter Wind Speed measured in miles per hour for new data: "))


new_data = [[new_temp_max, new_temp_min, new_wind8]] 
prediction = model.predict(new_data)

print("Predicted:", prediction[0])  
if prediction[0] == 0:
    print("Rain")
elif prediction[0]==1:
    print("Sun")
elif prediction[0]==2:
  print("Drizzle")
elif prediction[0]==3:
  print("Snow")  
else:
  print("Fog")
