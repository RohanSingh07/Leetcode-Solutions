# start from low and keep finding the numbers in range that satisfy the criteria of ascending
# keep incrementing the first digit from left and in case of 9 add more digit to the number

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        flag = True
        current = low
        current_lis = [i for i in str(current)]
        while current < high:
            for i in range(1,len(current_lis)):
                if current_lis[i-1] == '9':
                    if current_lis[0] == '9':
                        current_lis+=[0]
                        current_lis[0] = '1'
                        for j in range(1,len(current_lis)):
                            current_lis[j]='0'
                    else:
                        current_lis[0] = str(int(current_lis[0])+1)
                    current = int(''.join(current_lis))
                    flag = False
                    break
                    
                else:
                    current_lis[i] = str(int(current_lis[i-1])+1)
            if flag == False:
                flag = True
                continue
            current = int(''.join(current_lis))
            if current<=high and current>=low:
                ans.append(current)
            current_lis[0] = str(int(current_lis[0])+1)          
        return ans
       
