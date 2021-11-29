import datetime
import yfinance as yf
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY

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


def get_ticker_codes(date=datetime.date.today(), next=24, prev=0):
    start = date + relativedelta(months=-prev)
    end = date + relativedelta(months=+next)
    dates = [(dt.year, dt.month) for dt in rrule(MONTHLY, dtstart=start, until=end, bymonthday=-1)]
    return ["BTC" + month_code_list[date[1] - 1] + str(date[0] % 100) + ".CME" for date in dates]


def get_ticker_history(ticker_codes):
    history_list = []
    for code in ticker_codes:
        ticker = yf.Ticker(code)
        history = ticker.history(period='max')
        if not history.empty:
            history_list.append(history)
            print("Data loaded for " + code)
    return history_list
