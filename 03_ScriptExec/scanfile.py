def scanner(name, function):
    list(function(line) for line in open(name, 'r'))


