/*
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:
Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

Example 2:
Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

Constraints:
1 <= num <= 109
*/

class Solution {

    private static class DescComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o1 < o2 ? 1 : -1;
        }
    }

    public int largestInteger(int num) {
        /*
        Descending order priority queue. PQ is implemented as Max Heap, which is
        why it performs so well.
        */
        PriorityQueue<Integer> pqEven = new PriorityQueue<>(new DescComparator());
        PriorityQueue<Integer> pqOdd  = new PriorityQueue<>(new DescComparator());

        List<Boolean> flags = new LinkedList();
        while (num > 0) {
            int t = num % 10;
            num = num / 10;
            if (t % 2 == 0) {
                pqEven.offer(t);
                flags.add(0, true);
            } else {
                pqOdd.offer(t);
                flags.add(0, false);
            }
        }

        int r = 0;
        for (int i = 0; i < flags.size(); i++) {
            int t = flags.get(i) ? pqEven.poll() : pqOdd.poll();
            r = r * 10 + t;
        }
        return r;
    }
}