// my day one lets start with some easy problems
// from leetcode Q 1108

// Input: address = "1.1.1.1"
// "1[.]1[.]1[.]1"


public class solution1108{

     public static void main(String []args){
        
        String ans = findIP('1.1.1.1');
        
        System.out.println(ans);
     }
     // read the string and once it find . replace with [.]
     public String findIP(String address){
         // I dont know how jova works for reading string lol
         // feel bad
         // I think for my level of programming just read solution
         // I found charAt() would work for read the string
         // give a try
         String adrs = ""; 
         for(int i = 0; i < address.length(); i++){
             if(address.charAt(i) == '.'){
                 adrs = adrs + "[.]"";
             }else{
                 adrs = adrs + address.charAt(i);
             }
         }
         
         return adrs;
         
     }
}

// if know charAt(), this really is a easy question.
// good start

// back to real
// leetcode Q771

class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        for(int scount = 0; scount <S.length(); scount++){
            if(J.indexOf(S.charAt(scount)) != -1){
                count++;
            }
        }
        return count;     
    }
}
