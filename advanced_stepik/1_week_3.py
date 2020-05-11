n = int(input())

a = list(map(lambda i: i.split(), [str(input()) for i in range(n)]))
namespaces = {
    'global': {'vars':[],
               'parent': ''}
}

def get(namespace, var):
    if var in namespaces[namespace]['vars']:
        return var
    else:
        get()


for command in a:
    if command[0] == 'create':
        if command[-1] in namespaces:
            namespaces[command[1]] = {'vars': [],
                                      'parent': []}
            namespaces[command[-1]]['parent'] = (command[1])
        else:
            namespaces[command[1]] = {'vars':[],
                                   'parent':[]}
    if command[0] == 'add':
        namespaces[command[1]]['vars'].append(command[-1])
    # if command[0] == 'get':





print(namespaces)