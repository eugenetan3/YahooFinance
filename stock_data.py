import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

from sys import argv, stdout, stderr, stdin



def main():


    #implement accessory features
    argc = len(argv)

    #implement accessing specific aspects such as closing open etc

    if argc == 2:
        stock = argv[1]
    else:
        stderr("No Stock Provided")
        exit
    last_year = datetime.datetime.now().year - 1
    start_date = datetime.datetime.now().replace(year = last_year)
    end_date = datetime.datetime.now()

    data_frame = web.DataReader(name = stock, data_source='yahoo', start = start_date, end = end_date)


    category = input("What quality of the dataframe would you like to access? (Hi, Lo, Close, Open, Adj Close): ")


    if len(category) > 0:
        printFrame = data_frame[[category]]
        print(printFrame)
    else:
        print(data_frame)

    export_csv = data_frame.to_csv(r'~/export_dataframe.csv', index = None, header=True)





    value = data_frame.iloc[0]['Close']
    print(f"The value pulled is : {value} ")

    close_values = []


    #close_length = data_frame['Close'].len()

    #for i in range(close_length):
    #    close_values.append(data_frame.iloc[i]['Close'])


if __name__ == "__main__":
    main()
