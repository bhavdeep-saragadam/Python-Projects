import COVID19Py

covid19 = COVID19Py.COVID19()

covid19 = COVID19Py.COVID19(data_source="jhu")


data = covid19.getLatest()

cont = covid19.getLocationByCountryCode('IN', timelines=True)

print(cont)