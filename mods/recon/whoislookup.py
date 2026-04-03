import whois
from colorama import init, Fore, Style

init(autoreset=True)

def whois_look():
    domain = input('Enter domain or IP to lookup: ')
    whois_result = whois.whois(domain)
    print(Fore.GREEN + Style.BRIGHT + f'''Results for {domain} are
        Domain: {whois_result.domain_name}
        Registrar: {whois_result.registrar}
        Created in: {whois_result.creation_date}
        Expires in {whois_result}
        Person: {whois_result.name}
        Updated: {whois_result.updated_date}
        Status: {whois_result.status}
''')


