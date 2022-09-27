def insert_item(values, start: int, end: int):
	done = False
	cur = end
	more_to_search = (cur != start)

	while more_to_search and done is False:
		if values[cur] < values[cur - 1]:
			tmp = values[cur]
			values[cur] = values[cur - 1]
			values[cur - 1] = tmp
			cur -= 1
			more_to_search = (cur != start)
		else:
			done = True

def insertion_sort(values):
	for i in range(len(values)):
		insert_item(values, 0, i)
