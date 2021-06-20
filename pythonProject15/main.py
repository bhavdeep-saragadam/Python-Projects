import COVID19Py

covid19 = COVID19Py.COVID19()

covid19 = COVID19Py.COVID19(data_source="jhu")




# This is where you could specify what country you would want.

cont = covid19.getLocationByCountryCode('IN', timelines=True)

print(cont)