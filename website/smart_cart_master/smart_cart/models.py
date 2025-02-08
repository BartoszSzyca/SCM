from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True, null=False)
    user_name = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255,null=False)

    def __str__(self):
        return f"<id={self.user_name}(email={self.email})"


class FoodModel(models.Model):
    name = models.CharField(max_length=255,unique=True, null=False)
    quantities = models.JSONField(null=False)
    macros = models.JSONField(null=False)
    micros = models.JSONField(null=False)
    storage_conditions = models.CharField(max_length=1000, blank=True,
                                          null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FridgeModel(models.Model):
    food = models.ForeignKey(FoodModel, on_delete=models.CASCADE,
                             related_name="fridge_items")
    quantities = models.IntegerField(null=False)
    purchase_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Fridge item for {self.food.name} with {self.quantities} units"


class ShoppingListModel(models.Model):
    food = models.ForeignKey(FoodModel, on_delete=models.CASCADE,
                             related_name="shopping_list")
    quantities = models.IntegerField(null=False)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return (f"Shopping list item: {self.food.name}, "
                f"Quantity: {self.quantities}, "
                f"Price: {self.price:.2f}")