import datetime
import yfinance as yf
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY
from functools import reduce
import pandas as pd


# 'January': 'F',
# 'February': 'G',
# 'March': 'H',
# 'April': 'J',
# 'May': 'K',
# 'June': 'M',
# 'July': 'N',
# 'August': 'Q',
# 'September': 'U',
# 'October': 'V',
# 'November': 'X',
# 'December': 'Z'
month_code_list = ('F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z')
btc_str = 'BTC-USD'

def get_ticker_codes(date=datetime.date.today(), next=24, prev=0):
    start = date + relativedelta(months=-prev)
    end = date + relativedelta(months=+next)
    # determine all month ends in the period between start and end
    rule = rrule(MONTHLY, dtstart=start, until=end, bymonthday=-1)
    return ["BTC" + month_code_list[date.month - 1] + str(date.year % 100) + ".CME" for date in rule]
    

def get_ticker_close_data(code):
    ticker = yf.Ticker(code)
    history = ticker.history(period='max').reset_index()
    if not history.empty:
        history = history[['Date', 'Close']].rename(columns={'Close': code})
    return history


def get_close_data(ticker_codes):
    data_list = []
    for code in ticker_codes:
        data = get_ticker_close_data(code)
        if not data.empty:
            data_list.append(data)
    futures_frame = reduce(lambda df1, df2: pd.merge(df1, df2, how='outer', on='Date'), data_list)
    bitcoin_frame = get_ticker_close_data(btc_str)
    final_frame = pd.merge(futures_frame, bitcoin_frame, how='left', on='Date')
    final_frame = final_frame.sort_values(by=['Date'], ascending=True)
    return final_frame
