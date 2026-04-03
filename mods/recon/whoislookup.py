import whois

def whois_look():
    domain = input('Enter domain or IP to lookup: ')
    whois_result = whois.whois(domain)
    print(f'Result for {domain} is {whois_result}')

