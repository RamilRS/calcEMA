import pandas as pd
import mplfinance as mpf # для вывода графика

# расчет скользящей EMA
def calculate_ema(prices, N, smoothing=2):
    # N - период EMA
    # формула расчета EMA:
    # EMA = price * k + EMA(-1) * ( 1 − k )
    # price - текущая цена
    # EMA(-1) - значение EMA на предыдущем баре
    # k = smoothing / (1 + N) - весовой коэффициент, где
    # smoothing - константа, влияющая на расчет k, по умолчанию 2

    ema = [float('NaN') for _ in range(N-1)] # добавляем признаки отсутствия информации для N-1 первых периодов
    ema.append(sum(prices[:N]) / N) # расчитываем и добавляем первое значение EMA
    for price in prices[N:]:
      k = (smoothing / (1 + N))
      ema.append((price * k) + ema[-1] * (1 - k))
    return ema

# загружаем тиковые данные и преобразуем в свечи в нужный таймфрейм
def LoadPrices(fname,tf="1D"): # tf в формате 5min,15min,1h,1D и т.п.
    df = pd.read_csv(fname)
    df['TS'] = pd.to_datetime(df['TS'], format='%Y-%m-%d %H:%M:%S.%f')
    df = df.set_index('TS')
    data = df['PRICE'].resample(tf).ohlc().dropna()
    return data


if __name__ == '__main__':
    data = LoadPrices("C:\\Users\\ramil\\Downloads\\prices.csv\\prices.csv")
    ema = calculate_ema(data.close, 14)
    emaline = mpf.make_addplot(ema)
    mpf.plot(data, addplot=emaline, type='candle', style='charles')
