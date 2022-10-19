class Transaction(object):
    def __init__(self, txn):
        name, time, amount, city = txn.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        
    def __str__(self):
        return "{},{},{},{}".format(self.name, self.time, self.amount, self.city)


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        for i in range(len(transactions)):
            transactions[i] = Transaction(transactions[i])
            
        
        result = []
        for i in range(len(transactions)):
            if int(transactions[i].amount) > 1000:
                result.append(transactions[i])
                continue
            
            for j, t in enumerate(transactions):
                if j == i:
                    continue                
                if transactions[i].name == transactions[j].name and transactions[i].city != transactions[j].city and abs(transactions[i].time - transactions[j].time) <= 60:
                    result.append(transactions[i])
                    break
        
        return [r.__str__() for r in result]
                
                
                
            
            
            