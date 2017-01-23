from decimal import Decimal
from prices import Tax, PriceRange

from .utils import get_tax_for_country


class EuropeanVAT(Tax):
    def __init__(self, country_code, vat_rate=None, rate_name=None):
        self.country_code = country_code
        self.rate_name = rate_name
        self.vat_rate = vat_rate

    def calculate_tax(self, price_obj):
        if self.vat_rate is None:
            return Decimal(0)
        return (self.vat_rate * price_obj.gross) / 100

    def __repr__(self):
        return 'EuropeanVat(%s, rate_name=%s, vat_rate=%s)' % (
            self.country_code, self.rate_name, self.vat_rate)


def apply_vat(country_code, price, rate_name=None):
    vat_rate = get_tax_for_country(country_code, rate_name)
    country_vat = EuropeanVAT(country_code, vat_rate, rate_name=rate_name)
    return country_vat.apply(price)


def get_price_with_vat(country_code, price, rate_name=None):
    if isinstance(price, PriceRange):
        min_price = apply_vat(country_code, price.min_price, rate_name)
        max_price = apply_vat(country_code, price.max_price, rate_name)
        return PriceRange(min_price, max_price)
    return apply_vat(country_code, price, rate_name)
