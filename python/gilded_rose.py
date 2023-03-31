# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def is_item_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def is_item_backstage_passes(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_item_aged_brie(self, item):
        return item.name == "Aged Brie"

    def update_quality(self):
        for item in self.items:
            if item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
                if item.quality > 0:
                    if not self.is_item_sulfuras(item):
                        item.quality -= 1
                    if item.name == "Conjured":
                        item.quality -= 1
            else:
                if item.quality < 50:
                    item.quality += 1
                    if self.is_item_backstage_passes(item):
                        if item.sell_in < 11 and item.quality < 50:
                            item.quality += 1
                        if item.sell_in < 6 and item.quality < 50:
                            item.quality += 1
            self.update_sell_in_date(item)
            if item.sell_in < 0:
                if not self.is_item_aged_brie(item):
                    if not self.is_item_backstage_passes(item):
                        if item.quality > 0:
                            if not self.is_item_sulfuras(item):
                                item.quality -= 1
                            if item.name == "Conjured":
                                item.quality -= 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1

    def update_sell_in_date(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

### TODO: create 2 functions for updating quality before sell in date and one for updating quality after sell in date


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
