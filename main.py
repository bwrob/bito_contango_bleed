import helpers
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    download_data = False
    if download_data:
        codes = helpers.get_ticker_codes(prev=24)
        df = helpers.get_close_data(codes).to_csv('final.csv', index=False)
    else:
        df = pd.read_csv ('final.csv')
    
    print(df.head)
    df.plot(x="Date", y=["BTC-USD", "BTCX21.CME", "BTCZ21.CME"])
    plt.show()
