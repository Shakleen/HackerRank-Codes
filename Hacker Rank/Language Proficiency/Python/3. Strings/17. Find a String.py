def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        i = string.find(sub_string, start)
        if i != -1: 
            count += 1
            start = i+1
        else: 
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)