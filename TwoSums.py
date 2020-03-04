class Solution:
    def twoSum(self, nums, target):
        number_dict = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in number_dict:
                number_dict[num] = i
            else:
                return [number_dict[n], i]



def main():
    var = Solution()
    ip_target = int(input('Enter target element to check : '))
    try:
        ip_list = []
        while True:
            ip_list.append(int(input()))
    except:
        print(ip_list,ip_target)
    print(var.twoSum(ip_list, ip_target))

main()