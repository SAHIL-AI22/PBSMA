def rainaverage(l):
    city_rainfall = {}

    for city, rainfall in l:
        if city in city_rainfall:
            city_rainfall[city].append(rainfall)
        else:
            city_rainfall[city] = [rainfall]

    average_rainfall = [(city, sum(rainfall_list) / len(rainfall_list)) for city, rainfall_list in city_rainfall.items()]
    average_rainfall.sort()

    return average_rainfall

print(rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)]))
print(rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)]))
