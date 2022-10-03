def min_index(values, start: int, end: int):
	index = start
	for i in range(start + 1, end, 1):
		if values[i] < values[index]:
			index = i
	return index

def selection_sort(values):
	end_idx = len(values)
	for i in range(0, end_idx, 1):
		m_index = min_index(values, i, end_idx)
		tmp = values[i]
		values[i] = values[m_index]
		values[m_index] = tmp
