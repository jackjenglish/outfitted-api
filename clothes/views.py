from clothes.models import Item,ItemImage,Outfit
from clothes.serializers import OutfitSerializer,ItemSerializer,ItemImageSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import json

def getOutfitData(outfit):
    outfitData = {"id":outfit.id,"imgsrc":outfit.imgsrc,"gender":outfit.gender}
    items = outfit.items.all()
    itemGroups,selected,selectedIndices=[],[],[]
    normalPrice,minPrice,maxPrice=0,0,0

    for item in items:
        itemData = ItemSerializer(item).data
        selected.append(itemData['id'])
        normalPrice+=float(itemData['price'])

        groupItems = sorted(Item.objects
            .filter(itemGroup__iexact=itemData["itemGroup"])
            .filter(color__iexact=itemData["color"])
            .filter(gender__iexact=itemData["gender"]))
        selectedIndices.append(groupItems.index(item))

        group =[]
        groupPrices = [item.price for item in groupItems]
        curMin=min(groupPrices)
        curMax=max(groupPrices)

        for i in groupItems:
            images = i.itemimage_set.all()
            groupItemData = ItemSerializer(i).data
            groupItemData['images'] = [image.imgsrc for image in images]
            group.append(groupItemData)

        itemGroups.append(group)
        minPrice+=curMin
        maxPrice+=curMax

    outfitData["indices"] = selectedIndices
    outfitData["pricing"] = {"min":int(minPrice),"normal":int(normalPrice),"max":int(maxPrice)}
    outfitData["selected"] = selected
    outfitData["data"] = itemGroups
    return outfitData

class OutfitItemsDetail(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Outfit.objects.get(pk=pk)
        except Outfit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        outfit = self.get_object(pk)
        return Response(getOutfitData(outfit))


class OutfitPage(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request,gender,page, format=None):
        itemsPerPage=8
        upperBound=int(page) * itemsPerPage
        lowerBound=(int(page)-1) * itemsPerPage
        outfits = Outfit.objects.all().filter(gender__iexact=gender)[lowerBound:upperBound]
        jsonOutfits=[getOutfitData(o) for o in outfits]
        return Response(jsonOutfits)

class OutfitList(generics.ListCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(OutfitList, self).get_serializer(*args, **kwargs)

class OutfitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(ItemList, self).get_serializer(*args, **kwargs)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ItemImgList(generics.ListCreateAPIView):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(ItemImgList, self).get_serializer(*args, **kwargs)

class ItemImgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



