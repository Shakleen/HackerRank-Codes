def fun(s):
    parts = s.split('@')

    if (len(parts) > 1): 
        parts = [parts[0], *(parts[1].split('.'))]
    
        if len(parts) == 3 and all(len(sp) > 0 for sp in parts):
            valid = {chr(i + 65) for i in range(26)}
            valid |= {chr(i + 97) for i in range(26)}
            valid |= {chr(i + 48) for i in range(10)}

            if all([char in valid for char in parts[1]]):
                valid |= {'-', '_'}

                if all([char in valid for char in parts[0]]):
                    return len(parts[2]) <= 3

    return False
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)