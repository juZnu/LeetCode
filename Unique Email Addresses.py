def numUniqueEmails(emails):
    hashmap = dict()
    count = 0
    for email in emails:
        i = 0
        result = ''
        while email[i] != '@':
            if email[i] == '.':
                i += 1
                continue
            elif email[i] == '+':
                i += 1
                break
            else:
                result += email[i]
                i += 1
        while email[i] !='@':
            i += 1
        if not hashmap.get(result+email[i:],0):
            hashmap[result+email[i:]] =  1
            count += 1
    return count
print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))