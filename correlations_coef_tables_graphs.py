import pandas as pd
import matplotlib.pyplot as pyplot
from matplotlib import style
from correlation_code import correlation_itemA_dict, correlation_itemB_dict
from correlation_code import lyon_weather, bordeaux_weather, marseille_weather
from correlation_code import history_itemA, history_itemB


correlation_itemA_table = pd.DataFrame(correlation_itemA_dict)
correlation_itemB_table = pd.DataFrame(correlation_itemB_dict)


print(correlation_itemA_table)
print(correlation_itemB_table)

correlation_itemA_table.to_excel("Table_A.xlsx")
correlation_itemB_table.to_excel("Table_B.xlsx")


style.use("ggplot")

# graph of Max Temperature and sales of item B
pyplot.scatter(bordeaux_weather["MAX_TEMPERATURE_C"], history_itemB["SALES"])
pyplot.xlabel("MAX_TEMPERATURE_C of bordeaux")
pyplot.ylabel("SALES of item B")
pyplot.show()

# graph of Max Temperature and sales of item A
pyplot.scatter(bordeaux_weather["MAX_TEMPERATURE_C"], history_itemA["SALES"])
pyplot.xlabel("MAX_TEMPERATURE_C of bordeaux")
pyplot.ylabel("SALES of item A")
pyplot.show()

# graph of Wind speed and sales of item B
pyplot.scatter(lyon_weather["WINDSPEED_MAX_KMH"], history_itemB["SALES"])
pyplot.xlabel("WINDSPEED_MAX_KMH of Lyon")
pyplot.ylabel("SALES of item B")
pyplot.show()

# graph of cloud cover average percent and sales of item A
pyplot.scatter(marseille_weather["CLOUDCOVER_AVG_PERCENT"], history_itemA["SALES"])
pyplot.xlabel("CLOUDCOVER_AVG_PERCENT of marseille")
pyplot.ylabel("SALES of item A")
pyplot.show()
