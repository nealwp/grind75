from sys import argv

if len(argv) < 2:
   problem_name = input('Problem name:').replace(' ', '-')
else:
    problem_name = argv[1].replace(' ', '-')
 
file_contents = '"""\nProblem:\n\nv1:\n\n"""\n\n\n"""\nResults:\n\n"""'
with open(f'{problem_name}.py', 'w') as file:
    file.write(file_contents)