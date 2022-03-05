# Returns the public IP address of the current host.


import urllib.request


def ip():
    return urllib.request.urlopen("https://api.ipify.org/").read().decode("utf-8")


def main():
    print(ip())


if __name__ == "__main__":
    main()
