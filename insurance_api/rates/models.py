from tortoise import fields
from tortoise.fields import ForeignKeyField, ForeignKeyRelation
from tortoise.models import Model


class DateUploaded(Model):
    """
    Model for rate's date
    """

    id = fields.IntField(pk=True)
    #: this is a date when rate was uploaded
    date = fields.DateField(null=False, unique=True)
    rates: fields.ReverseRelation["Rate"]

    class Meta:
        table = "date_uploaded"


class CargoType(Model):
    '''
    Model for rate's cargo type
    '''

    id = fields.IntField(pk=True)
    #: this is a cargo type
    cargo_type = fields.CharField(max_length=30, null=False, unique=True)
    rates: fields.ReverseRelation["Rate"]

    class Meta:
        table = "cargo_types"


class Rate(Model):
    """
    The Rate model
    """

    id = fields.IntField(pk=True)
    #: this is an actual rate
    actual_rate = fields.FloatField(null=False)

    #: this is a date when rate was uploaded
    date: ForeignKeyRelation[DateUploaded] = ForeignKeyField(
        model_name="models.DateUploaded",
        related_name="rates",
        on_delete="CASCADE"
    )
    #: this is a cargo type
    cargo_type: ForeignKeyRelation[CargoType] = ForeignKeyField(
        model_name="models.CargoType",
        related_name="rates",
        on_delete="CASCADE"
    )

    def __repr__(self):
        return f"Rate('{self.date}', '{self.actual_rate}')"

    class Meta:
        table = "rates"
        unique_together = (("cargo_type", "date"),)
