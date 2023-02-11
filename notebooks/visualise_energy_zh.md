Visualising energy usage of Swiss cities
================

# Getting ready

Loading required packages

``` python
import pandas as pd
import seaborn as sns
```

Defining a parameter

This can be used when rendering to pass a different name, in which case
a different city’s data will be visualised.

``` python
df_name = "wi"
```

``` python
# Injected Parameters
df_name = "zh"
```

Loading the kedro vairables, including the data `catalog`

``` python
%load_ext kedro.ipython
```

Load the data

``` python
df = catalog.load(df_name)
df.head()
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #7fbfbf; text-decoration-color: #7fbfbf">                    </span><span style="color: #000080; text-decoration-color: #000080">INFO    </span> Loading data from <span style="color: #008000; text-decoration-color: #008000">'zh'</span> <span style="font-weight: bold">(</span>PickleDataSet<span style="font-weight: bold">)</span><span style="color: #808000; text-decoration-color: #808000">...</span>                          <a href="file://C:\Users\sara\.virtualenvs\energy-JbBSA9-6\lib\site-packages\kedro\io\data_catalog.py" target="_blank"><span style="color: #7f7f7f; text-decoration-color: #7f7f7f">data_catalog.py</span></a><span style="color: #7f7f7f; text-decoration-color: #7f7f7f">:</span><a href="file://C:\Users\sara\.virtualenvs\energy-JbBSA9-6\lib\site-packages\kedro\io\data_catalog.py#343" target="_blank"><span style="color: #7f7f7f; text-decoration-color: #7f7f7f">343</span></a>
</pre>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>gross_energy_kwh</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-02-05 22:45:00+00:00</td>
      <td>27375.0455</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-02-05 22:30:00+00:00</td>
      <td>27615.5835</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-02-05 22:15:00+00:00</td>
      <td>28376.9020</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-02-05 22:00:00+00:00</td>
      <td>28843.4275</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-02-05 21:45:00+00:00</td>
      <td>29377.6460</td>
    </tr>
  </tbody>
</table>
</div>

# Daily energy use over the years

``` python
df['year'] = df['timestamp'].dt.year
df['yday'] = df['timestamp'].dt.day_of_year
df["time_of_day"] = df["timestamp"].dt.time
df["date"] = df["timestamp"].dt.date
df["gross_energy_mwh"] = df["gross_energy_kwh"] / 1000

grouped = df.groupby(["year", "yday"]).sum("gross_energy_kwh").reset_index()

grouped["rolling_avg"] = grouped["gross_energy_kwh"].rolling(window=7).mean()
```

``` python
sns.lineplot(data=grouped, x="yday", y="rolling_avg", hue="year")
```

![](visualise_energy_files/figure-gfm/cell-8-output-1.png)

# Visualise the entire variability with a heatmap-like plot

``` python
df22 = df[df.year == 2022]
```

``` python
from plotnine import ggplot, aes, geom_tile, labs, scale_x_discrete, scale_y_discrete
from mizani.breaks import date_breaks
from mizani.formatters import date_format
import datetime
```

``` python
(ggplot(df22, aes(x="time_of_day", y="date", fill="gross_energy_mwh"))
 + geom_tile()
 + scale_y_discrete(breaks=[datetime.date(2022, 1,1), datetime.date(2022,4,1), datetime.date(2022,7,1), datetime.date(2022,10,1)], labels=["Jan", "Apr", "July", "Oct"], limits=df22.date.unique()[::-1])
  + scale_x_discrete(breaks=[datetime.time(0,0), datetime.time(6,0), datetime.time(12,0), datetime.time(18,0)],
  labels=["00:00", "06:00", "12:00", "18:00"])
 + labs(x = "Time of day", y = "", fill = "energy used per 15min [MWh]", title= "2022")
 )
```

![](visualise_energy_files/figure-gfm/cell-11-output-1.png)

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ggplot:</span><span style="color: #000000; text-decoration-color: #000000"> </span><span style="color: #000000; text-decoration-color: #000000; font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">92578826577</span><span style="color: #000000; text-decoration-color: #000000; font-weight: bold">)</span><span style="font-weight: bold">&gt;</span>
</pre>

scales give a strange error (repr-error 0)
