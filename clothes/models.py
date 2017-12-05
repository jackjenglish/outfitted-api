from django.db import models

# Create your models here.
ITEM_GROUPS=(("hoodie","Hoodie"),("boots","Boots"),("leatherjacket","Leather Jacket"),("skirt","Skirt"),("desertboots","Desert Boots"),("sunglasses","Sunglasses"),("sweatshirt","Sweatshirt"),("cap","Cap"),("wovenbelt","Woven Belt"),("boatshoes","Boat Shoes"),("chelsea","Chelsea Boots"),("shoes","Shoes"),("chinos","Chinos"),("leathershoes","Leather Shoes"),("trainers","Trainers"),("tshirt","T-Shirt"),("poloshirt","Polo Shirt"),("bomber","Bomber"),("windbreaker","Windbreaker"),("jeans","Jeans"),("shirt","Shirt"),("belt","Belt"))
ITEM_COLORS=(("pink","Pink"),("beige","Beige"),("white;blue","White and Blue"),("black","Black"),("Blue","Blue"),("brown","Brown"),("grey","Grey"),("navy","Navy"),("red","Red"),("white","White"),("green","Green"))

class ItemSize(models.Model):
	size = models.CharField(max_length=25)

class Item(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=7,decimal_places=2)	
	brand = models.CharField(max_length=50)
	size = models.ManyToManyField(ItemSize,null=True,blank=True)
	srclink = models.CharField(max_length=150)
	itemGroup = models.CharField(max_length=60,choices=ITEM_GROUPS,blank=False)
	color =models.CharField(max_length=30,choices=ITEM_COLORS,blank=True)
	gender = models.CharField(max_length=30,choices=(("male","Male"),("female","Female")),blank=False)
	def __lt__(self,other):
		return self.price< other.price

	def __str__(self):
		return "%s: %s, %s"%(self.id,self.name,self.itemGroup)

#Item Category:


class ItemImage(models.Model):
	imgsrc = models.CharField(max_length=100)
	item = models.ForeignKey(Item,on_delete=models.CASCADE)

	def __str__(self):
		return "%s: %s"%(self.id,self.imgsrc)

class Outfit(models.Model):
    imgsrc = models.CharField(max_length=100, blank=True, default='')
    items = models.ManyToManyField(Item)
    gender = models.CharField(max_length=30,choices=(("male","Male"),("female","Female")),blank=False)
    def __str__(self):
        return "%s: %s"%(self.id,self.imgsrc)




