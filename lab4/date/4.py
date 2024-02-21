from datetime import datetime

date1 = datetime(2024, 2, 15, 12, 0, 0) 
date2 = datetime(2024, 2, 20, 14, 30, 0)

difference_seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", difference_seconds)
