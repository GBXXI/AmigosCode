
// In computer science, selection sort is an in-place comparison sorting <br>
// algorithm. It has an O time complexity, which makes it inefficient on large <br>
// lists, and generally performs worse than the similar insertion sort. Selection <br>
// sort is noted for its simplicity and has performance advantages over more <br>
// complicated algorithms in certain situations, particularly where auxiliary <br>
// memory is limited. The algorithm divides the input list into two parts: a <br>
// sorted sublist of items which is built up from left to right at the front of <br>
// the list and a sublist of the remaining unsorted items that occupy the rest of <br>
// the list. Initially, the sorted sublist is empty and the unsorted sublist is <br>
// the entire input list. The algorithm proceeds by finding the smallest element <br>
// in the unsorted sublist, exchanging it with the leftmost unsorted element, and <br>
// moving the sublist boundaries one element to the right.<br>
// <footer>Wikipedia</footer>

// Data.
// const data = [4, 9, 3, 6, 2];
const data = [80, 324, 2, 3, 5, 2, 4, 3, 15, 2, 19];

function amc_solution(list_){
    for(var outer_index = 0; outer_index < list_.length; outer_index++){

        var min_index = outer_index;        

        for(var inner_index = (outer_index + 1); inner_index < list_.length; inner_index++){

            if (list_[inner_index] < list_[min_index]) {
                
                min_index = inner_index;    
                       
            }                        
        }
        var temp = list_[outer_index];
                list_[outer_index] = list_[min_index];
                list_[min_index] = temp;     
    }
    return list_;
}


console.log(amc_solution(data));
