import dns.resolver
import dns.reversename

def ip2server():
    ip = input('Enter ur IP address here: ')
    try:
        addr = dns.reversename.from_address(ip)

        answers = dns.resolver.resolve(addr, "PTR")

        for rdata in answers:
            print(f'Hostname is: {rdata.target}')

    except dns.resolver.NXDOMAIN:
        print(f'No register found for the {ip}')
    except Exception as e:
        print(f'Unexpected error: {e}')

