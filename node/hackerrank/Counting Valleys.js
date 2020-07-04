// Complete the countingValleys function below.
function countingValleys(n, s) {
    let seaLevel = 0;
    let res = 0;
    let prev = 0;
    for (let i = 0; i<n; i++){
        if (s[i] === "U"){
            seaLevel++;
        } else{
            seaLevel--;
        }
        if (prev <= 0 && seaLevel == 0){
            res++;
        }
        prev = seaLevel
    }
    return res;
}

countingValleys(8,"DDUUUUDD");