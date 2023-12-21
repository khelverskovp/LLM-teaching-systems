import numpy as np
import matplotlib.pyplot as plt

def plotPriceRetrieval():
    # Character per token
    char_per_token = 4

    # Average characters per page
    char_per_page = 1800

    # Average tokens per page
    tokens_per_page = char_per_page/char_per_token

    # price in kroner per 1000 tokens
    price_per_1000_tokens = 0.01*6.81

    # price per page
    price_per_page = price_per_1000_tokens*(tokens_per_page/1000)

    # plot price as a function of number of pages
    pages = np.arange(1,1000)
    price = pages*price_per_page

    # price of one page
    print(f'Price of one page: {price_per_page} kr')
    
    plt.plot(pages,price)
    plt.xlabel('Number of pages \n [1800 characters per page]', size=12)
    plt.ylabel('Price [kr]', size=12)
    plt.title('Price of retrieval wrt. \n number of pages [per prompt]', size=14)

    # Vertical lines at 200 and 600 pages that stop at the price
    y_low = 200*price_per_page
    y_high = 600*price_per_page
    plt.vlines(x=200, ymin=0, ymax=y_low, color='r', linestyle='--')
    plt.vlines(x=600, ymin=0, ymax=y_high, color='r', linestyle='--')

    # horizontal lines at 200 and 600 pages
    plt.hlines(y=y_low, xmin=0, xmax=200, color='r', linestyle='--')
    plt.hlines(y=y_high, xmin=0, xmax=600, color='r', linestyle='--')

    # write price at 200 and 600 pages on top of the lines
    plt.text(200/2, y_low+1, f'{int(y_low)} kr', size=10, color='r')
    plt.text(600/2, y_high+1, f'{int(y_high)} kr', size=10, color='r')


    # highligt the area between the lines    

    # fit layout
    plt.tight_layout()

    plt.show()



if __name__ == '__main__':
    plotPriceRetrieval()