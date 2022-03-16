def check_single_row(row, msg):
	"""Checks whether the provided list of rows has only 1 element.

	Args:
		row: the list of rows.
		msg: the error message to raise if there are no rows found.

	Raises:
		ValueError: if no rows are found.
		RuntimeError: if more than one row is found.
	"""
	if row.shape[0] < 1:
		raise ValueError(msg)
	# unlikely to happen unless someone tampered with /data
	if row.shape[0] > 1:
		raise RuntimeError("Module data has been corrupted")