import yaml
from pyowm import OWM
with open("config.yaml",'r') as dbconfig:
    cfg = yaml.load(dbconfig)

#test config file read
owm_details = cfg['owm']
api_key = owm_details['api_key']
owm = OWM(api_key)
obs = owm.weather_history_at_place("Paris, France", start=1397426401,end=1398635589)

# obs = owm.weather_at_place('Paris, France')
print obs
w = obs.get_weather()
# w.set_reference_time(1397935723506L)
print w.get_clouds()
print w.get_wind()
print w.get_humidity()
print w.get_pressure()
print w.get_temperature()
print w.get_status()