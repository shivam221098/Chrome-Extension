import requests
from bs4 import BeautifulSoup


def main():
    # product URL
    url = 'https://www.flipkart.com/samsung-frame-163cm-65-inch-ultra-hd-4k-qled-smart-tv/p/itmbce01823968b5?pid' \
          '=TVSFQQJ8E2XJQEDA&lid=LSTTVSFQQJ8E2XJQEDA1RFDSZ&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1' \
          '=search&fm=SEARCH&iid=en_nHLZePRfXklbnyEHEN4%2Fp9qSjRQEcyooR5hjcx7ZqguVoxpTGeZO8cU1zOR' \
          '%2FjHYB4KFj53RFvbGLefCpXLZC9w%3D%3D&ppt=sp&ppn=sp&ssid=l8zqpz5hpc0000001607693260149&qH=c9a1fdac6e082dd8 '

    request = requests.get(url)

    soup = BeautifulSoup(request.content, "html.parser")

    name_list = soup.find_all('span', attrs={"class": "B_NuCI"})
    price_list = soup.find_all('div', attrs={'class': '_30jeq3 _16Jk6d'})

    for name, price in zip(name_list, price_list):
        print(f"Name: {name.get_text()}, price: {price.get_text()}")


if __name__ == '__main__':
    main()