from rest_framework import serializers
from clothes.models import Item,ItemImage,Outfit

class ItemSerializer(serializers.ModelSerializer):
	#owner =	serializers.ReadOnlyField(source = 'owner.username')
	class Meta:
		model = Item 
		fields = ('id','name','price','brand','size','color','srclink','itemGroup','gender')

class ItemImageSerializer(serializers.ModelSerializer):
	#owner =	serializers.ReadOnlyField(source = 'owner.username')
	class Meta:
		model = ItemImage
		fields = ('id','imgsrc','item')

class OutfitSerializer(serializers.ModelSerializer):
	#owner =	serializers.ReadOnlyField(source = 'owner.username')
	class Meta:
		model = Outfit
		fields = ('id','imgsrc','items','gender')
