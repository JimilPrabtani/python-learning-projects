import socket 

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain}")
        print(f"IP Address: {ip_address}")
    except socket.gaierror:
        print(f"error: unable to resolve domain {domain}.")

def main():
    domain = input("Enter the domain name to lookup: ")
    dns_lookup(domain)

if __name__ == "__main__":
    main()
