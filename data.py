################################'''data'''#################################
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
scope      = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
data_header= ['recomendation_rank','resort_name','resort_rate','price_with_off','price_without_off','resort_site','resort_email']
data       = []
data.append(data_header)
email_pattern=r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+'

###########################################################################