def copy_projects(projects):
	# Your code here
	# for project in projects:
	# 	from_project = project
	for i in range(len(projects)):
		from_project = projects[i]
		print(from_project)
	# from_project = 'A'
	# to_project = 'B'
	# print(f"Copying from {from_project} to {to_project}")

copy_projects(['A', 'B', 'C', 'D', 'E'])
print('\n')
copy_projects(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
print('\n')
copy_projects(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

# Phase 1
# Copy between one project and every other project.
# Phase 2
# The idea is to simulate copying from project A to B, C, D, and E
# then from B to C, D, and E
# from C to D and E
# and finally from D to E
# without ever repeating, or going backwards to a project you've already
# copied between.