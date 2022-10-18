class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        hMap = {}
        
        for email in emails:
            localName, domainName = email.split("@")
            
            #ProcessLocalName
            local = []
            for i in range(len(localName)):
                if localName[i] == ".":
                    continue
                elif localName[i] == "+":
                    break
                local.append(localName[i])
            
            uniqueEmail = "".join(local) +"@"+ domainName
            
            if uniqueEmail not in hMap:
                hMap[uniqueEmail] = []
            hMap[uniqueEmail].append(email)
        
        return len(hMap.keys())
            