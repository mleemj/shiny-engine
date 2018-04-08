import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Practix {

    public int[] insertion_sort(int[] unsorted_lst) {
        for(int indx = 1; indx < unsorted_lst.length; indx++){
            int search_indx = indx;
            int tmp_insertion_value = unsorted_lst[indx];

            while (
                    (search_indx > 0)
                            && (unsorted_lst[search_indx -1] > tmp_insertion_value)
                    ){
                unsorted_lst[search_indx] = unsorted_lst[search_indx -1];
                search_indx -= 1;
            }
            unsorted_lst[search_indx] = tmp_insertion_value;
        }
        return unsorted_lst;
    }


    /**
     * Given ordered list, search term. Returns indx of search term or -1 if not found
     */
    public int bst(int[] ordered_list, int indx_first, int indx_last, int search_term) {
        if (indx_last < indx_first) return -1;

        int indx_mid = (indx_first + indx_last) / 2;

        if ( search_term > ordered_list[indx_mid]) {
            return bst(ordered_list, indx_mid + 1, indx_last, search_term);
        } else if ( search_term < ordered_list[indx_mid]) {
            return bst(ordered_list, indx_first, indx_mid - 1, search_term);
        } else {
            return indx_mid;
        }
    }

    /**
     * Given unordered list, search term. Return indx of search term or -1 if not found
     */
    public boolean unord_search(int[] unordered_lst, int search_term) {
        for(int unord: unordered_lst) {
            if (search_term == unord) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Practix practix = new Practix();
        int[] unordered_list = {100, 10, 30, 500, 120, 500};
        int[] ordered_list = {10, 30, 100, 120, 500};
        int search_term = 120;

        boolean found = practix.unord_search(unordered_list, search_term);
        System.out.println("Unordered list " + found);

        int indx_found = practix.bst(ordered_list, 0, ordered_list.length -1, search_term);
        System.out.println("BST " + indx_found);


        int[] unsorted_lst = {5, 1, 100, 2, 10};
        int[] number = practix.insertion_sort(unsorted_lst);
        List<Integer> collection = Arrays.stream(number).boxed().collect(Collectors.toList());
        collection.stream().forEach((Integer i) -> System.out.print(" " + i));
    }
}
