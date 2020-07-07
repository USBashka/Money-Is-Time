"""Main converter module"""


from forex_python.converter import CurrencyRates


class Converter:
    """Main converter class"""

    def __init__(self, rate: float, currency: str = 'USD'):
        """Create converter with given rate (seconds/currency_unit)"""
        self.rate = rate
        self.currency = currency.capitalize()

    def money_to_time(self, money: float, currency: str):
        """Convert given amount of money to time (sec)"""
        if currency == self.currency:
            time_to_earn = money * self.rate
        else:
            cur_rates = CurrencyRates()
            local_money = cur_rates.convert(currency, self.currency, money)
            time_to_earn = local_money * cur_rate
        return time_to_earn

    def time_to_money(self, time: float, currency: str):
        """Convert given amount of time to money (currency)"""
        if currency == self.currency:
            money = time / self.rate
        else:
            cur_rates = CurrencyRates()
            local_money = cur_rates.convert(currency, self.currency, money)
            time_to_earn = local_money * cur_rate
        return time_to_earn

    def __str__(self):
        return f'Converter({self.rate}sec/{self.currency})'


def main():
    """Module test"""
    print('How much do you earn per hour?')
    answer = input().split(' ')
    converter = Converter(1 / float(answer[0]) * 3600,
                          answer[1] if len(answer) > 1 else 'USD')
    print(converter)
    print()
    print('Type amount of money to convert to time')
    print('')
    while (inp := input()).isdecimal():
        print(f'{round(converter.money_to_time(float(inp), converter.currency))} seconds')


if __name__ == '__main__':
    main()
