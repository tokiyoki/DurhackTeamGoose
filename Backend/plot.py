import matplotlib.pyplot as plt, matplotlib.dates as mdates
import seaborn as sns
import pandas as pd


def plot_graph(working_directory, csv_name,table, date_type, price_type, y_axis):
    legend = ""
    df = pd.read_csv(working_directory + 'fy19-23/' + csv_name)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
    # data_type = 'Y', 'M', 'D'
    # price_type = 'High', 'Low', 'Avg'
    if price_type == 'High':
        d = df.groupby(pd.Grouper(key='Date', freq=date_type))[price_type].max()
        table['Highest Price'] = d
        legend = 'Highest Price'
    elif price_type == 'Low':
        d = df.groupby(pd.Grouper(key='Date', freq=date_type))[price_type].min()
        table['Lowest Price'] = d
        legend = 'Lowest Price'
    else:
        d = df.groupby(pd.Grouper(key='Date', freq=date_type))[['Open','High','Low','Close']].mean().iloc[:,:].mean(axis=1)
        table['Average Price'] = d
        legend = 'Average Price'

    table["Date"] = table.index

    sns.set(rc={'axes.facecolor': '#242526',
                'axes.labelcolor':'#F6F5EE',
                # 'axes.edgecolor':'#242526',
                'axes.linewidth':0.5,
                "axes.spines.top":'False',
                "axes.spines.right": 'False',
                'xtick.color':'#F6F5EE',
                'ytick.color':'#F6F5EE',
                'grid.color': '#242526',
                'figure.facecolor': '#242526',
                'text.color':'#F6F5EE'})
    sns.set_palette(["#ffac00"])
    #print(pd.melt(table, ['Date']))
    sns.lineplot(x='Date', y='value', hue='variable',data=pd.melt(table, ['Date']))
    plt.legend(labels=[legend])
    if date_type == 'M':
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
        plt.xlabel("Month")
    elif date_type == 'Y':
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.xlabel("Year")
    else:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
        plt.xlabel("Date")
        plt.xticks(rotation=6) 
    plt.ylabel(y_axis)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=260))

    new_file_name = "figure.png"
    plt.savefig(working_directory + new_file_name)
    plt.close()
    return new_file_name


#plot_graph('EURUSD.csv', table, 'Y', 'High')
#plot_graph('EURUSD.csv', table, 'Y', 'Low')