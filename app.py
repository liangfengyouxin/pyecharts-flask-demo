from random import randrange
from flask import Flask, render_template
import json
import ccxt
import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Kline


app = Flask(__name__, static_folder="templates")

global time_change

time_change = '4h'

def bar_base() -> Kline:
    exchane = ccxt.okex()
    kline_BTC = exchane.fetch_ohlcv('BTC/USDT', timeframe=time_change)
    df_BTC = pd.DataFrame(kline_BTC, dtype='float')
    df_BTC[0] = pd.to_datetime(df_BTC[0], unit='ms')  # 转换为想要的时间
    date = df_BTC[0].tolist()
    list_BTC_USDT = np.array(df_BTC[[1, 4, 3, 2]]).tolist()

    c = (
        Kline()
        .add_xaxis(date)
        .add_yaxis('BTC', list_BTC_USDT)
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            xaxis_opts=opts.AxisOpts(is_scale=True),
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        )
    )
    return c


def aar_base() -> Kline:
    exchane = ccxt.okex()
    kline_LTC = exchane.fetch_ohlcv('LTC/USDT', timeframe=time_change)
    kline_ETH = exchane.fetch_ohlcv('ETH/USDT', timeframe=time_change)
    kline_BCH = exchane.fetch_ohlcv('BCH/USDT', timeframe=time_change)
    kline_BSV = exchane.fetch_ohlcv('BSV/USDT', timeframe=time_change)

    df_LTC = pd.DataFrame(kline_LTC, dtype='float')
    df_ETH = pd.DataFrame(kline_ETH, dtype='float')
    df_BCH = pd.DataFrame(kline_BCH, dtype='float')
    df_BSV = pd.DataFrame(kline_BSV, dtype='float')

    df_LTC[0] = pd.to_datetime(df_LTC[0], unit='ms')
    df_ETH[0] = pd.to_datetime(df_ETH[0], unit='ms')
    df_BCH[0] = pd.to_datetime(df_BCH[0], unit='ms')
    df_BSV[0] = pd.to_datetime(df_BSV[0], unit='ms')

    date = df_LTC[0].tolist()

    list_lTC_USDT = np.array(df_LTC[[1, 4, 3, 2]]).tolist()
    list_ETH_USDT = np.array(df_ETH[[1, 4, 3, 2]]).tolist()
    list_BCH_USDT = np.array(df_BCH[[1, 4, 3, 2]]).tolist()
    list_BSV_USDT = np.array(df_BSV[[1, 4, 3, 2]]).tolist()

    c = (
        Kline()
        .add_xaxis(date)
        .add_yaxis('LTC', list_lTC_USDT)
        .add_yaxis('ETH', list_ETH_USDT)
        .add_yaxis('BCH', list_BCH_USDT)
        .add_yaxis('BSV', list_BSV_USDT)

        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            xaxis_opts=opts.AxisOpts(is_scale=True),
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        )
    )
    return c


def car_base() -> Kline:
    exchane = ccxt.okex()
    kline_ETC = exchane.fetch_ohlcv('ETC/USDT', timeframe=time_change)
    kline_XRP = exchane.fetch_ohlcv('XRP/USDT', timeframe=time_change)
    kline_EOS = exchane.fetch_ohlcv('EOS/USDT', timeframe=time_change)
    kline_TRX = exchane.fetch_ohlcv('TRX/USDT', timeframe=time_change)

    df_ETC = pd.DataFrame(kline_ETC, dtype='float')
    df_XRP = pd.DataFrame(kline_XRP, dtype='float')
    df_EOS = pd.DataFrame(kline_EOS, dtype='float')
    df_TRX = pd.DataFrame(kline_TRX, dtype='float')

    df_ETC[0] = pd.to_datetime(df_ETC[0], unit='ms')
    df_XRP[0] = pd.to_datetime(df_XRP[0], unit='ms')
    df_EOS[0] = pd.to_datetime(df_EOS[0], unit='ms')
    df_TRX[0] = pd.to_datetime(df_TRX[0], unit='ms')

    date = df_ETC[0].tolist()

    list_ETC_USDT = np.array(df_ETC[[1, 4, 3, 2]]).tolist()
    list_XRP_USDT = np.array(df_XRP[[1, 4, 3, 2]]).tolist()
    list_EOS_USDT = np.array(df_EOS[[1, 4, 3, 2]]).tolist()
    list_TRX_USDT = np.array(df_TRX[[1, 4, 3, 2]]).tolist()

    c = (
        Kline()
        .add_xaxis(date)
        .add_yaxis('ETC', list_ETC_USDT)
        .add_yaxis('XRP', list_XRP_USDT)
        .add_yaxis('EOS', list_EOS_USDT)
        .add_yaxis('TRX', list_TRX_USDT)

        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            xaxis_opts=opts.AxisOpts(is_scale=True),
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        )
    )
    return c

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options()

@app.route("/aarChart")
def get_aar_chart():
    c = aar_base()
    return c.dump_options()

@app.route("/carChart")
def get_car_chart():
    c = car_base()
    return c.dump_options()


if __name__ == "__main__":
    app.run()