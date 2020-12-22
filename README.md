# YFinAPI

YFinAPI is a REST API through which you can access Yahoo! finance data provided by YFinance library.

## REST API

The REST API to the YFinAPI is described below.

## Get stock info for given ticker

### Params

**ticker** - Ticker name from Yahoo! finance

### Request

`GET /fin/info/?ticker=AMZN`

    curl -i -H 'Accept: application/json' http://localhost:7000/fin/?ticker=AMZN

### Response

```json
{
	"tickerInfo": {
		"zip": "98109-5210",
		"sector": "Consumer Cyclical",
		"fullTimeEmployees": 1125300,
		"longBusinessSummary": "Amazon.com, Inc. engages in the retail...",
		"city": "Seattle",
		"phone": "206-266-1000",
		"state": "WA",
		"country": "United States",
		"companyOfficers": [],
		"website": "http://www.amazon.com",
		"maxAge": 1,
		"address1": "410 Terry Avenue North",
		"industry": "Internet Retail",
		"previousClose": 3201.65,
		"regularMarketOpen": 3200.01,
		"twoHundredDayAverage": 3095.0464,
		"trailingAnnualDividendYield": null,
		"payoutRatio": 0,
		"volume24Hr": null,
		"regularMarketDayHigh": 3226.9666,
		"navPrice": null,
		"averageDailyVolume10Day": 4069633,
		"totalAssets": null,
		"regularMarketPreviousClose": 3201.65,
		"fiftyDayAverage": 3154.9194,
		"trailingAnnualDividendRate": null,
		"open": 3200.01,
		"toCurrency": null,
		"averageVolume10days": 4069633,
		"expireDate": null,
		"yield": null,
		"algorithm": null,
		"dividendRate": null,
		"exDividendDate": null,
		"beta": 1.201049,
		"circulatingSupply": null,
		"startDate": null,
		"regularMarketDayLow": 3166,
		"priceHint": 2,
		"currency": "USD",
		"trailingPE": 93.74247,
		"regularMarketVolume": 3532504,
		"lastMarket": null,
		"maxSupply": null,
		"openInterest": null,
		"marketCap": 1608704065536,
		"volumeAllCurrencies": null,
		"strikePrice": null,
		"averageVolume": 4681029,
		"priceToSalesTrailing12Months": 4.6234436,
		"dayLow": 3166,
		"ask": 3203.5,
		"ytdReturn": null,
		"askSize": 800,
		"volume": 3532504,
		"fiftyTwoWeekHigh": 3552.25,
		"forwardPE": 70.60515,
		"fromCurrency": null,
		"fiveYearAvgDividendYield": null,
		"fiftyTwoWeekLow": 1626.03,
		"bid": 3202.02,
		"tradeable": false,
		"dividendYield": null,
		"bidSize": 900,
		"dayHigh": 3226.9666,
		"exchange": "NMS",
		"shortName": "Amazon.com, Inc.",
		"longName": "Amazon.com, Inc.",
		"exchangeTimezoneName": "America/New_York",
		"exchangeTimezoneShortName": "EST",
		"isEsgPopulated": false,
		"gmtOffSetMilliseconds": "-18000000",
		"quoteType": "EQUITY",
		"symbol": "AMZN",
		"messageBoardId": "finmb_18749",
		"market": "us_market",
		"annualHoldingsTurnover": null,
		"enterpriseToRevenue": 4.699,
		"beta3Year": null,
		"profitMargins": 0.04994,
		"enterpriseToEbitda": 37.404,
		"52WeekChange": 0.7856386,
		"morningStarRiskRating": null,
		"forwardEps": 45.41,
		"revenueQuarterlyGrowth": null,
		"sharesOutstanding": 500889984,
		"fundInceptionDate": null,
		"annualReportExpenseRatio": null,
		"bookValue": 164.89,
		"sharesShort": 3020596,
		"sharesPercentSharesOut": 0.006,
		"fundFamily": null,
		"lastFiscalYearEnd": 1577750400,
		"heldPercentInstitutions": 0.58671004,
		"netIncomeToCommon": 17376999424,
		"trailingEps": 34.202,
		"lastDividendValue": null,
		"SandP52WeekChange": 0.15055776,
		"priceToBook": 19.444357,
		"heldPercentInsiders": 0.1455,
		"nextFiscalYearEnd": 1640908800,
		"mostRecentQuarter": 1601424000,
		"shortRatio": 0.64,
		"sharesShortPreviousMonthDate": 1604016000,
		"floatShares": 427783024,
		"enterpriseValue": 1634843623424,
		"threeYearAverageReturn": null,
		"lastSplitDate": 936230400,
		"lastSplitFactor": "2:1",
		"legalType": null,
		"lastDividendDate": null,
		"morningStarOverallRating": null,
		"earningsQuarterlyGrowth": 1.967,
		"dateShortInterest": 1606694400,
		"pegRatio": 2.52,
		"lastCapGain": null,
		"shortPercentOfFloat": 0.0070999996,
		"sharesShortPriorMonth": 3138429,
		"impliedSharesOutstanding": null,
		"category": null,
		"fiveYearAverageReturn": null,
		"regularMarketPrice": 3200.01,
		"logo_url": "https://logo.clearbit.com/amazon.com"
	}
}
```

## Get historical data for given ticker

### Params

**1. ticker**: Ticker name from Yahoo! finance

**2. period**: Data period to get historical data

- Valid periods are : _“1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”_

**3. interval**: Data interval to get historical data

- Valid intervals are : _“1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”_

### Request

`GET /fin/hist/?ticker=AAPL&period=5d&interval=1d`

    curl -i -H 'Accept: application/json' http://localhost:7000/fin/?ticker=AAPL&period=5d&interval=1d

### Response

```json
{
	"tickerHist": {
		"index": [
			"2020-12-15,00:00:00",
			"2020-12-16,00:00:00",
			"2020-12-17,00:00:00",
			"2020-12-18,00:00:00",
			"2020-12-21,00:00:00"
		],
		"columns": [
			"Open",
			"High",
			"Low",
			"Close",
			"Volume",
			"Dividends",
			"Stock Splits"
		],
		"data": [
			[124.34, 127.9, 124.13, 127.88, 157572300, 0, 0],
			[127.41, 128.37, 126.56, 127.81, 98208600, 0, 0],
			[128.9, 129.58, 128.04, 128.7, 94359800, 0, 0],
			[128.96, 129.1, 126.12, 126.66, 192541500, 0, 0],
			[125.02, 128.31, 123.45, 128.23, 120093700, 0, 0]
		]
	}
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
