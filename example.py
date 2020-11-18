from volatility.volest import VolatilityEstimator
from volatility.data import DataHelpers

# data
symbol = 'JPM'
bench = '^GSPC'
data_file_path = './tests/JPM.csv'
bench_file_path = './tests/BENCH.csv'
estimator = 'GarmanKlass'


# estimator windows
window = 30
windows = [30, 60, 90, 120]
quantiles = [0.25, 0.75]
bins = 100
density = True

# use the yahoo helper to correctly format data from finance.yahoo.com
data = DataHelpers()
jpm_price_data = data.yahoo_helper(symbol, data_file_path)
spx_price_data = data.yahoo_helper(bench, bench_file_path)

# initialize class
vol = VolatilityEstimator(
    price_data=jpm_price_data,
    estimator=estimator,
    bench_data=spx_price_data
)

# call plt.show() on any of the below...
_, plt = vol.cones(windows=windows, quantiles=quantiles)
_, plt = vol.rolling_quantiles(window=window, quantiles=quantiles)
_, plt = vol.rolling_extremes(window=window)
_, plt = vol.rolling_descriptives(window=window)
_, plt = vol.histogram(window=window, bins=bins, density=density)

_, plt = vol.benchmark_compare(window=window)
_, plt = vol.benchmark_correlation(window=window)

# ... or create a pdf term sheet with all metrics in term-sheets/
vol.term_sheet(
    window,
    windows,
    quantiles,
    bins,
    density
)
