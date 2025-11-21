def field(items, *args):
    assert len(args) > 0
    for item in items:
        if item is None:
            continue
        if len(args) == 1:
            if args[0] in item and item[args[0]] is not None:
                yield item[args[0]]
        else:
            d = {}
            flag = False
            for key in args:
                if key in item and item[key] is not None:
                    d[key] = item[key]
                    flag = True
            if flag:
                yield d

# goods = [
#     {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#     {'title': 'Диван для отдыха', 'color': 'black'}
# ]
# print(list(field(goods, 'title')))
#
# print(list(field(goods, 'title', 'price')))

