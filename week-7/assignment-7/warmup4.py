#Use datetime module to print the current date and time in the format "Today is: YYYY-MM-DD HH:MM:SS"

import datetime

from datetime import datetime
now = datetime.now()
print("Today is:", now.strftime("%B %d, %Y"))