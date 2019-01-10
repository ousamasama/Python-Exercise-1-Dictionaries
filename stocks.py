
stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak", 'GE':'General Electric' }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]

#problem 1
#Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. 
#This is the basic relational database join algorithm between two tables.
for key, value in stockDict.items():
    # print("key", key)
    # print("value", value)
    for single_item in purchases:
        if key == single_item[0]:
            math = single_item[1] * single_item[3]
            print("I purchased " + key + " stock for $" + str(math))
            # print(key, single_item[0])
            # print(math)

# for single_item in purchases:
#     print(single_item[0])

#problem 2
#Create a second purchase summary that which accumulates total investment by ticker symbol.
#In the above sample data, there are two blocks of GE.
#These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. 
#The program makes one pass through the data to create the dict.
#A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

stock_list = ()
for key in stockDict.keys():
    ticker = "------ " + key + " ------"
    print(ticker)
    for single_item in purchases:
        if key == single_item[0]:
            # print(single_item)
            stock_list += single_item
            print(single_item)

#joes way
stock_dict = {'GM': 'General Motors',
              'CAT': 'Caterpillar',
              'EK': "Eastman Kodak",
              'GE': "General Electric"
              }

purchases = [('GE', 100, '10-sep-2001', 48),
             ('GM', 200, '11-sep-2007', 35),
             ('CAT', 100, '1-apr-1999', 24),
             ('GM', 50, '4-apr-1987', 53),
             ('EK', 450, '37-apr-1987', 13),
             ('GE', 200, '1-jul-1998', 56)]

# 1) We want individual output like this:
# I purchased General Electric stock on 10 - sep - 2001 for $4800
# 2) While also building up a collection we can loop over that contains each company and all the purchases we made of that company's stock
# report = {
#     "GE": [('GE', 100, '10-sep-2001', 48), ('GE', 200, '1-jul-1998', 56)],
#     "CAT": [('CAT', 100, '1-apr-1999', 24)]
# }
# so we can loop over that and generate a readable report in the terminal
report = {}
for purchase in purchases:
  abbrev = purchase[0]
  full_name = stock_dict[abbrev]
  no_of_shares = purchase[1]
  purch_date = purchase[2]
  purch_price = purchase[3]
  full_purchase_price = no_of_shares * purch_price
  print(f"I purchased {full_name} stock on {purch_date} for ${full_purchase_price}.")

  try:
    report[abbrev].append(purchase)
  except KeyError:
    report[abbrev] = list()
    report[abbrev].append(purchase)

for abbrev, purchases_list in report.items():
  print(f"-------{abbrev}-------")
  total_portfolio_stock_value = 0
  for purchase in purchases_list:
    total_portfolio_stock_value += purchase[1] * purchase[3]
    print(f"     {purchase}")
  print(f"Total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")