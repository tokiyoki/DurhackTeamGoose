import matplotlib.pyplot as plt, matplotlib.dates as mdates
import seaborn as sns
import pandas as pd

df = pd.read_csv('fy19-23/EURUSD.csv')
df['Date']=pd.to_datetime(df['Date'],format='%Y%m%d')


def plot_graph(df, date_type, price_type):
    # data_type = 'Y', 'M', 'D'
    # price_type = 'High', 'Low', 'Avg'
    if price_type == 'High':
        d = df.groupby(pd.Grouper(key='Date', freq=date_type))[price_type].max().to_frame()
        d.columns = ["Price"]
    elif price_type == 'Low':
        d = df.groupby(pd.Grouper(key='Date', freq=date_type))[price_type].min().to_frame()
        d.columns = ["Price"]
    else:
        d = df.groupby(pd.Grouper(key='Date', freq=date_type))[['Open','High','Low','Close']].mean().iloc[:,:].mean(axis=1).to_frame()
        d.columns = ["Price"]
    sns.set(rc={'axes.facecolor': '#242526',
                'axes.labelcolor':'#F6F5EE',
                # 'axes.edgecolor':'#242526',
                'axes.linewidth':0.5,
                "axes.spines.top":'False',
                "axes.spines.right": 'False',
                'xtick.color':'#F6F5EE',
                'ytick.color':'#F6F5EE',
                'grid.color': '#242526',
                'figure.facecolor': '#242526'})
    sns.set_palette(["#ffac00"])
    sns.lineplot(data=d, x="Date", y="Price")
    if date_type == 'M':
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
    elif date_type == 'Y':
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    else:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=260))
    plt.savefig("figure.png")


plot_graph(df, 'Y', 'Avg')