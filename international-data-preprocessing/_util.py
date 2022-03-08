def check_single_row(row, msg):
	if row.shape[0] < 1:
		raise ValueError(msg)
	# unlikely to happen unless someone tampered with /data
	if row.shape[0] > 1:
		raise RuntimeError("Module data has been corrupted")