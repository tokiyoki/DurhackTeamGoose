import matplotlib.pyplot as plt, matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D
import matplotlib.font_manager as fm

custom_font_path = 'digital-7.regular.ttf'
prop = fm.FontProperties(fname=custom_font_path)
plt.rcParams['font.family'] = prop.get_name()
legend_font_prop = fm.FontProperties(fname=custom_font_path)
prop_ticks = fm.FontProperties(fname=custom_font_path)


def plot_graph(working_directory, csv_name, table, date_type, price_types, y_axis):
    plt.switch_backend('Agg')
    print("Starting render")
    legend = ["", "", ""]
    df = pd.read_csv(working_directory + 'fy19-23/' + csv_name)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
    # data_type = 'Y', 'M', 'D'
    # price_type = 'High', 'Low', 'Avg'
    counter = 0

    print("While loop")
    while counter < len(price_types):
        print("Run ", counter)
        if price_types[counter] == 'High':
            d = df.groupby(pd.Grouper(key='Date', freq=date_type))[price_types[counter]].max()
            table[counter]['Highest Price'] = d
            legend[counter] = 'Highest Price'
        elif price_types[counter] == 'Low':
            d = df.groupby(pd.Grouper(key='Date', freq=date_type))[price_types[counter]].min()
            table[counter]['Lowest Price'] = d
            legend[counter] = 'Lowest Price'
        else:
            d = df.groupby(pd.Grouper(key='Date', freq=date_type))[['Open','High','Low','Close']].mean().iloc[:,:].mean(axis=1)
            table[counter]['Average Price'] = d
            legend[counter] = 'Average Price'

        table[counter]["Date"] = table[counter].index
        counter = counter + 1

    print("After while loop")

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

    plt.xlabel("Month", fontproperties=prop, fontsize=15, weight='bold')
    plt.ylabel(y_axis, fontproperties=prop, fontsize=15, weight='bold')

    plt.xticks(fontproperties=prop_ticks, fontsize=12)
    plt.yticks(fontproperties=prop_ticks, fontsize=15)
    
    #sns.set_palette(["#ffac00", "#990000", "#009900"])
    #print(pd.melt(table, ['Date']))
    price_labels = {
        'High': 'Highest Price',
        'Low': 'Lowest Price',
        'Avg': 'Average Price',
    }

    palettes = ["#ffac00", "#FF5E5E", "#029666"]

    legend_labels = []
    legend_colors = []

    counter = 0
    while counter < len(price_types):
        sns.set_palette([palettes[counter]])
        sns.lineplot(x='Date', y='value', hue='variable',data=pd.melt(table[counter], ['Date']))

        # preparing labels
        legend_labels.append(legend[counter])
        legend_colors.append(palettes[counter])

        counter = counter + 1

    legend_objects = [Line2D([0], [0], color=color, lw=2, label=label) for label, color in zip(legend_labels, legend_colors)]

    plt.legend(handles=legend_objects, prop=legend_font_prop, fontsize=15)

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