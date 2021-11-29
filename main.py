import helpers

if __name__ == '__main__':
    codes = helpers.get_ticker_codes(prev=24)
    historical_data = helpers.get_ticker_history(codes)
    for df in historical_data:
        print(df.head)
