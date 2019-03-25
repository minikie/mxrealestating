# Python 샘플 코드 #
import requests

api_key = 'Oh7DEmB%2FqCK%2BnQvU5VEpBpwmy7UHaZSUrvRl8LTlL0AuCaxTD5yFlaZUUTYQgUxwAUqweyWeFJF6zB3qCswM7w%3D%3D'
url = 'http://apis.data.go.kr/1611000/AptListService/getRoadnameAptList'
parameters = '?' + 'ServiceKey=' + api_key +'&loadCode=263802006002' + '&numOfRows=100'
res = requests.get(url + parameters)
print(res.text)
