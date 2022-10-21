class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        
        # 10 - (3 - 0)= 7 -> remaining diff
        # 7 - (7 - 3) = 4 -> remaining diff. 
        # 4 - (12 - 7) = -1 -> remianing diff. if remaining diff < 0 current level tax.
        
        last_tax_slot = 0
        taxes = 0
        for index, tax in enumerate(brackets):
            diff = tax[0] - last_tax_slot
            percentage = tax[1]
            
            if income - diff  < 0:
                break
            
            income -= diff
            taxes += diff*(percentage/100)

            last_tax_slot = tax[0]
        
        if income > 0:
            taxes += income*(percentage/100)
            income = 0
        
        return taxes
            
        