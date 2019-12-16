import ast
import copy

def helper(x, network):
    for tier in network:
        for swaps in tier:
            i = swaps[0]
            j = swaps[1]

            if(x[j] < x[i]):
                temp = x[i]
                x[i] = x[j]
                x[j] = temp

    return x



def sortingNetwork(network, num):
    rn = 2**num
    print("total Colums: " + str(rn) +'\ntotal lines: '+ str(num))
    inp = []
    for i in range(0,rn):
        strlist = list(format(i,'#0' + str(num+2) + 'b')[2:])
        strlist = list(map(int,strlist))
        inp.append(strlist)

    outputlist = copy.deepcopy(inp)
    for x in outputlist:
        x = x.sort()


    for x in inp:
        x = helper(x,network)

    output = []
    for i in range(0,len(inp)):
        if(inp[i] != outputlist[i]):
            test = list(format(i,'#0' + str(num+2) + 'b')[2:])
            print('it breaks here: ' + str(test))
            output.append(test)


    return output


if __name__=="__main__":
    x = open("network.txt","r")
    l = x.read().splitlines()
    y = l[1]
    num =int(l[0])
    x.close()
    network = ast.literal_eval(y)
    output = sortingNetwork(network,num)
    outputFile = 'Looks good'
    print(output)
    if(len(output) > 0):
        outputFile = output[0]
        print("looks like this network is broken check your output.txt")
    else:
        outputFile = "This network is ready to get started"
        print(outputFile)
    outputText = open("output.txt", 'w')
    outputText.write(str(outputFile))
    outputText.close()



