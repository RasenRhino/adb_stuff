import shodan
SHODAN_API_KEY = "your_key"
api = shodan.Shodan(SHODAN_API_KEY)
try:
# Search Shodan
    results = api.search('Android Debug Bridge')
# Show the results
#    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print(result['ip_str'])
#        print(result['data'])
#        print('')
except shodan.APIError as e:
    print(e)

