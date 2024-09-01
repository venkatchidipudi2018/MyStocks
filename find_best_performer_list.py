from nsepython import *

start_date = "26-08-2024"
end_date = "30-08-2024"
series = "EQ"
data = pd.read_csv("C:\\Users\\venka\\Downloads\\Nifty_500.csv")
symbols_list = data["Symbol"].tolist()

# symbols_list = ["aplltd"]
all_stocks_list = []
for c, stock_symbol in enumerate(symbols_list):
    print (c)
    print (stock_symbol)
    df = equity_history(stock_symbol,series,start_date,end_date)
    list_of_vwap_vals = df['VWAP'].to_list()
    old_value = list_of_vwap_vals[0]
    new_value = list_of_vwap_vals[-1]

    # Calculate the percentage change
    percentage_change = ((new_value - old_value) / old_value) * 100
    print (percentage_change)
    all_stocks_list.append((stock_symbol, percentage_change))

filtered_data = [item for item in all_stocks_list if item[1] >= 0]
sorted_filtered_data = sorted(filtered_data, key=lambda x: x[1], reverse=True)

for filtered_data in sorted_filtered_data:
    print (filtered_data)
