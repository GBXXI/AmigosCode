

//  It's a sorting algorith, which transport's the values on each itteration

//  Intial list
const L = [13, 40, 50, 50, 90, 18, 30, 50, 30, 70];
console.log(`Our initial list is: ${L}`);

//  List length:
const N = L.length;
//  <ln> 1) We write the range(N-1) which will return also the value N-2 as it's <br>
//         described by the pseudocode.</ln></br>
//  2) We write the range(N-1-i) which will retrun also the value N-2-i.<br>
//  3) If we want the sorting to be in descenting order we pass the conditional<br>
//         as 'if L\[j+1\] > L\[j\]' <br>
//  4) For the tansportation a temporary variable is required.

for (let i = 0; i < L.length - 1; i++){
    for (let j = 0; j < N -1 -i; j++){
        if (L[j] > L[j+1]){
            const tmp = L[j];
            L[j] = L[j+1];
            L[j+1] = tmp;
        }
    }
}

//  Our sorted list is:
console.log(`Our sorted list is: ${L}`);
