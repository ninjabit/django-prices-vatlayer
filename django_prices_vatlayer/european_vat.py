from decimal import Decimal
from prices import Tax, PriceRange

from .utils import get_tax_for_country


class EuropeanVAT(Tax):
    def __init__(self, country_code, rate_name=None):
        self.country_code = country_code
        self.rate_name = rate_name

    def calculate_tax(self, price_obj):
        vat_rate = get_tax_for_country(self.country_code, self.rate_name)
        if vat_rate is None:
            return Decimal(0)
        return (vat_rate * price_obj.gross) / 100

    def __repr__(self):
        return 'EuropeanVat(%s, %s)' % (self.country_code, self.rate_name)


def apply_vat(country_code, price, rate_name=None):
    country_vat = EuropeanVAT(country_code, rate_name)
    return country_vat.apply(price)


def get_price_with_vat(country_code, price, rate_name=None):
    if isinstance(price, PriceRange):
        min_price = apply_vat(country_code, price.min_price, rate_name)
        max_price = apply_vat(country_code, price.max_price, rate_name)
        return PriceRange(min_price, max_price)
    return apply_vat(country_code, price, rate_name)
