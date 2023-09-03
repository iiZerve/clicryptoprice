# clicryptoprice

1) add file to any directory
2) open cmd/powershell/etc
3) cd to file directory
4) type 'py price.py tokenname' for current token price (defaulted to coingecko)
5) If you wish to call prices from specific exchanges, type '--exchanges' followed by your desired exchanges separated by spaces.  for example, to get the price of ethereum on multuple exchanges you could enter 'py price.py eth --exchanges binance coinbase kraken'

If token name is more than one word, use '-' instead of spaces, ie, to get the price of Wrapped Bitcoin, type 'py price.py wrapped-bitcoin'
