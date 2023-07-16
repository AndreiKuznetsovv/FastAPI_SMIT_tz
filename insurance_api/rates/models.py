from tortoise import fields
from tortoise.models import Model


class Rate(Model):
    """
    The Rate model
    """

    id = fields.IntField(pk=True)
    #: this is a cargo type
    cargo_type = fields.CharField(max_length=30, null=False)
    #: this is an actual rate
    actual_rate = fields.FloatField(null=False)
    #: this is a date when rate was uploaded
    date = fields.DateField(null=False)

    def __repr__(self):
        return f"Rate('{self.date}', '{self.actual_rate}')"
