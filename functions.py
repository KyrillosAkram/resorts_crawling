
################################'''functions'''#################################

def fetch_results(search_term, number_results, language_code='en'):
	assert isinstance(search_term, str), 'Search term must be a string'
	assert isinstance(number_results, int), 'Number of results must be an integer'
	escaped_search_term = search_term.replace(' ', '+')
	google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
	response = requests.get(google_url, headers=USER_AGENT)
	response.raise_for_status()
	return search_term, response.text

def average(lst):
    avr=0
    for i in lst:
        avr=avr+int(i)
    return avr/len(lst)

def similarity_average(raw,reference):
    patterns=reference.split(' ')
    return average([pattern in raw for pattern in patterns])

def desired_link(lst,reference):
    avrs=[similarity_average(link,reference) for link in lst]
    return lst[lst.index(max(lst))]

################################################################################