/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode mid=getmid(head);
        ListNode nxtmid=mid.next;
        mid.next=null;
        ListNode left=sortList(head);
        ListNode right=sortList(nxtmid);
        return merge(left,right);
    }
     
    public static ListNode merge(ListNode l,ListNode r){
        if(l==null)return r;
        if(r==null)return l;
        ListNode head=null,tail=null;
        if(l.val<=r.val){
            head=tail=l;
            l=l.next;
        }else{
            head=tail=r;
            r=r.next;
        }
        while(l!=null && r!=null){
         if(l.val<=r.val){
            tail.next=l;
            tail=l;
            l=l.next;
        }else{
            tail.next=r;
            tail=r;
            r=r.next;
        }
        }
        if(l!=null){
            tail.next=l;
        }else{
            tail.next=r;
        }
        return head;
    }
    public static ListNode getmid(ListNode head){
        ListNode slow=head;
        ListNode fast=head.next;
        while(fast!=null && fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
        }
        return slow;
    } 

}
