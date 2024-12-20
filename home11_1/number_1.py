# 1 Фильтрация информации из базы данных
# У вас есть база данных, содержащая информацию о клиентах,
# их заказах и стоимости заказов. Например:
###########################################################
# client_id, order_id, order_cost
# 1, 1, 10.0
# 1, 2, 20.0
# 2, 3, 15.0
# 3, 4, 50.0
# 3, 5, 30.0
# ###########################################################
# Вам нужно выбрать только те заказы,
# стоимость которых больше или равна заданному значению.
# Для этого можно воспользоваться функцией filter.

def filter_orders_by_cost(file_iteration, number):

    row_head = next(file_iteration) # Выдернули шапку c client, order, order_cost
    rows = [row.split(",") for row in file_iteration] # Строки без шапки
    client = [float(row[0].rstrip()) for row in rows] # Стобец client
    order = [float(row[1].rstrip()) for row in rows] # Стобец order
    order_cost = [float(row[2].rstrip()) for row in rows] # Стобец order_cost
    index_string = [i for i, x in enumerate(order_cost)] # Получили все индексы
    need_index = list(filter(lambda x : order_cost[x] >= number, index_string)) # Отсортировали индексы по условию
    print(row_head)           #1
    print(list(rows))         #2
    print(list(client))       #3
    print(list(order))        #4
    print(list(order_cost))   #5
    print(list(index_string)) #6
    print(need_index)         #7

    return [f"{client[i]}, {order[i]}, {order_cost[i]}" for i in need_index]

with open("order.csv", "r") as file:
    result = filter_orders_by_cost(file, 20)
print(result)