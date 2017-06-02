"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None
        self.christmas = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.christmas == True:
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    # def is_christmas(self):

    #     if self.christmas == True:
    #         base_price = base_price * 1.5

    #     return base_price

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty)

        self.order_type = "domestic"
        self.tax = 0.08

        #return AbstractMelonOrder.__init__(self, species)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        super(InternationalMelonOrder, self).__init__(species, qty)
      
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17
        
        if qty < 10:
            base_price = 8




    def get_country_code(self):
        """Return the country code."""

        return self.country_code
