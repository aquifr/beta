# Next Steps

I'll need a way to display the data for a project. So, we need a Project model and
a view to display that to the user.

1. Model
2. URL Route
3. View
	1. Returns in JSON for now


Offering Class Structure

from datetime import datetime, timedelta

class Offering(object):
	title = ''
	short_desc = ''
	long_desc = ''
	offering_creator = ''
	milestones = []
	currently_raised = 0
	num_investors = 0
	date_started = datetime(2017, 1, 1)
	

