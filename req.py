import requests

r = requests.get("https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2")

print(r.content)
print(help(r))