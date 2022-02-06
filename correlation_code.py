import pandas as pd

history_itemA = pd.read_csv("history_itemA.csv")
history_itemB = pd.read_csv("history_itemB.csv")
lyon_weather = pd.read_csv("lyon2019.csv")
bordeaux_weather = pd.read_csv("bordeaux2019.csv")
lille_weather = pd.read_csv("lille2019.csv")
marseille_weather = pd.read_csv("marseille2019.csv")

features = ['MAX_TEMPERATURE_C', 'MIN_TEMPERATURE_C', 'WINDSPEED_MAX_KMH', 'PRECIP_TOTAL_DAY_MM',
            'HUMIDITY_MAX_PERCENT', 'VISIBILITY_AVG_KM', 'PRESSURE_MAX_MB', 'CLOUDCOVER_AVG_PERCENT']


# this function for calculation correlation coefficient of every item in the features list with sales of item A and B
def correlation(weather_city, item_history):
    list_of_correlation_coefficient = []
    for item in features:
        correlation_calculation = item_history['SALES'].corr(weather_city[item])
        list_of_correlation_coefficient.append(correlation_calculation)

    return list_of_correlation_coefficient


correlation_itemA_dict = {'features': features,
                          'Item A_Bordeaux': correlation(bordeaux_weather, history_itemA),
                          'Item A_lille': correlation(lille_weather, history_itemA),
                          'Item A_lyon': correlation(lyon_weather, history_itemA),
                          'Item A_marseille': correlation(marseille_weather, history_itemA),

                          }

correlation_itemB_dict = {'features': features,
                          'Item B_Bordeaux': correlation(bordeaux_weather, history_itemB),
                          'Item B_lille': correlation(lille_weather, history_itemB),
                          'Item B_lyon': correlation(lyon_weather, history_itemB),
                          'Item B_marseille': correlation(marseille_weather, history_itemB),
                          }
