from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'heropowers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ("-hero.heropowers", "-power.heropowers",)

    @validates("strength")
    def validate_strength(self, key, strength):
        if strength not in ["Strong", "Weak", "Average"]:
            raise ValueError(
                "Strength must be one of the following values: 'Strong', 'Weak', 'Average'")
        return strength

    def __repr__(self):
        return f'''HeroPower {self.strength}'''
