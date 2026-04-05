class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i;
        int j;
        vector <int> f;
        int n=nums.size();
        int rem=0;
        for(i=0;i<n;i++){
            rem=target-nums[i];
            for(j=i+1;j<n;j++){
                if(nums[j]==rem){
                    f={i,j};
                    
                    
                }
            }
        }
        return f;
    }
};