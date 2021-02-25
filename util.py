

def load_tickers():

    tickers = []
    with open('config/tickers.txt') as f:
        for line in f:
            for ticker in line.strip().split(', '):
                tickers.append(ticker)
    
    # print (tickers)
    return tickers
