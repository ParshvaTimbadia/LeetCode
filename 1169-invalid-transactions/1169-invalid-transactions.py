class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        result = []
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            if int(amount) > 1000:
                result.append(transactions[i])
                continue
            
            for j, t in enumerate(transactions):
                if j == i:
                    continue
                sname, stime, samount, scity = transactions[j].split(",")
                
                if sname == name and scity != city and abs(int(stime) - int(time)) <= 60:
                    result.append(transactions[i])
                    break
        
        return result
                
                
                
            
            
            